from flask import json, request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999
    data = None

    def __init__(self, msg=None, code=None, error_code=None,
                 data=None, dataname='data'):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        self.data = data
        self.dataname = dataname
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None, scope=None):
        body = {
            'msg': self.msg,
            'code': self.error_code,
            'request': request.method + ' ' + self.get_url_no_param()
        }
        if self.data is not None:
            body[self.dataname] = self.data
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None, scope=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
