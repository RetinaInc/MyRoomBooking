#!/usr/bin/env python
#encoding=utf-8

import json

import web

from config import settings
render = settings.render
db = settings.db

class List:
  def GET(self):
    params = web.input()
    query_data = db.select('booking', params, where="start_time>=$start and end_time<=$end")
    data = []
    for item in query_data:
      params = {'id': item['user_id']}
      user = db.select('user', params, where="id=$id")[0]
      name = user['cn_name']
      title = '{} Booking by {}'.format(item['title'], name)
      event = {
          'title': title,
          'start': str(item['start_time']),
          'end': str(item['end_time']),
          'info': item['info']
          }
      data.append(event)
    data = json.dumps(data)
    return render.eventList(data=data)
