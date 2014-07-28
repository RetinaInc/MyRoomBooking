#!/usr/bin/env python
#encoding=utf-8

from config import settings
render = settings.render

class List:
    def GET(self):
        data = []
        return render.list(data=data)
