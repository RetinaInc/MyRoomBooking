pre_fix = 'controllers.'
api_fix = 'api.'

urls = (
        '/', pre_fix + 'index.Index',
        '/list', pre_fix + 'list.List',
        '/api/event_list', api_fix + 'event.List',
        '/api/event_add', api_fix + 'event.Add',
        '/api/event_del', api_fix + 'event.Del',
        )
