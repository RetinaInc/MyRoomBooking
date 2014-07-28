#!/usr/bin/env python
#encoding=utf-8

import json

from config import settings
render = settings.render

class List:
  def GET(self):
    data =  [
        {
            'title': 'Event1',
            'start': '2014-07-29 01:00:00'
        },
        {
            'title': 'Event2',
            'start': '2014-07-30'
        }
     ]
    data = json.dumps(data)
    return render.eventList(data=data)
