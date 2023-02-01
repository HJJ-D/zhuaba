def model_search_paging_util(query, page=1, page_size=20):
    data = {
        'meta': {
            'count': query.count(),
            'page': page,
            'page_size': page_size
        }
    }

    if page_size != -1:
        query = query.offset((page - 1) * page_size).limit(page_size)
    data['data'] = query.all()
    return data


def ensure_id_list(l):
    return [item.id if hasattr(item, 'id') else item for item in l if item is not None]
