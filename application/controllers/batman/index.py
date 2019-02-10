# -*- coding:utf-8 -*-
import web 
import config as config

class Index:
    def __init__(self):
        pass

    def GET(self):
        batman = config.model_batman.select_batman().list() # selecciona todos los registros de clientes
        return config.render.index_batman(batman) # Envia todos los registros y renderiza index.html


