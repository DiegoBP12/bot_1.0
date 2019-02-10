# -*- coding:utf-8 -*-
import web 
import config as config

class Home:
    def __init__(self):
        pass

    def GET(self):
        return config.render.index() # Envia todos los registros y renderiza index.html
