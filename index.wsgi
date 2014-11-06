#!/usr/bin/env python
#coding:utf-8

import tornado.wsgi
import sae
from main import Application

application = sae.create_wsgi_app(Application())