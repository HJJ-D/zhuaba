from contextlib import contextmanager

from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import asc, desc, orm


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


db = SQLAlchemy(query_class=BaseQuery)


class Base(db.Model):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}
    fields = []

    @orm.reconstructor
    def __init__(self):
        self._fields = self.fields

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return self._fields

    def hide(self, *keys):
        fields = self._fields.copy()
        for key in keys:
            if key in fields:
                fields.remove(key)
        self._fields = fields
        return self

    def show(self, *keys):
        fields = self._fields.copy()
        for key in keys:
            if key not in fields:
                fields.append(key)
        self._fields = fields
        return self

    @classmethod
    def get_by_id(cls, id_):
        return cls.query.get(id_)

    @classmethod
    def create(cls, **kwargs):
        base = cls()
        with db.auto_commit():
            for key, value in kwargs.items():
                if value is not None:
                    if hasattr(cls, key):
                        try:
                            setattr(base, key, value)
                        except:
                            pass
            db.session.add(base)
        return base

    def modify(self, **kwargs):
        with db.auto_commit():
            for key, value in kwargs.items():
                if hasattr(self, key):
                    try:
                        setattr(self, key, value)
                    except:
                        pass

    def delete(self):
        with db.auto_commit():
            db.session.delete(self)

    @classmethod
    def search(cls, enable_fuzzy=None, **kwargs):
        from app.utils.model import model_search_paging_util
        if enable_fuzzy is None:
            enable_fuzzy = set()
        res = cls.query
        for key, value in kwargs.items():
            if value is not None:
                if hasattr(cls, key):
                    if isinstance(value, str) and key in enable_fuzzy:
                        val = value.replace('\\', '\\\\')
                        val = val.replace('%', '\\%')
                        res = res.filter(getattr(cls, key).like('%' + val + '%'))
                    elif isinstance(value, list):
                        res = res.filter(getattr(cls, key).in_(value))
                    else:
                        res = res.filter(getattr(cls, key) == value)
        if kwargs.get('order'):
            for key, value in kwargs['order'].items():
                if hasattr(cls, key):
                    if value == 'asc':
                        res = res.order_by(asc(getattr(cls, key)))
                    if value == 'desc':
                        res = res.order_by(desc(getattr(cls, key)))

        page = kwargs.get('page') if kwargs.get('page') else 1
        page_size = kwargs.get('page_size') if kwargs.get('page_size') else 20
        return model_search_paging_util(res, page, page_size)

    @classmethod
    def search_all(cls, **kwargs):
        kwargs['page_size'] = -1
        return cls.search(**kwargs)

    @classmethod
    def count(cls, **kwargs):
        res = cls.query
        for key, value in kwargs.items():
            if value is not None:
                if hasattr(cls, key):
                    if isinstance(value, list):
                        res = res.filter(getattr(cls, key).in_(value))
                    else:
                        res = res.filter(getattr(cls, key) == value)
        return res.count()

    @classmethod
    def has(cls, **kwargs):
        return cls.count(**kwargs) > 0
