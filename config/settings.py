#!/usr/bin/env python
#encoding=utf-8

import web
from web.contrib.template import render_mako
render = render_mako(
        directories=['templates', 'templates/api'],
        input_encoding='utf8',
        output_encoding='utf8',
        )
web.config.debug = True
web.config.cache = False

web.template.Template.globals['render'] = render

db = web.database(dbn='mysql',db='room',user='root',pw='password',host='localhost',port=3306);
