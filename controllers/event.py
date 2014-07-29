#!/usr/bin/env python
#encoding=utf-8
import web
from config import settings
render = settings.render
db = settings.db

class Detail:
  def GET(self):
    data = []
    return render.detail(data=data)

class Add:
  def GET(self):
    data = web.input()
    if data.has_key('start') == False:
      data['start'] = ''
    return render.add(data=data)

  def POST(self):
    input = web.input()
    print db.insert('booking', room_id=1, user_id=1, start_time=input['start'],
        end_time=input['end'], title=input['title'], info=input['info'])
    raise web.seeother('/list')
