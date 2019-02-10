# -*- coding:utf-8 -*-
import web 
import config as config

class Index:
    def __init__(self):
        pass

    def GET(self):
        robin = config.model_robin.select_robin().list() # selecciona todos los registros de robins
        return config.render.index_robin(robin) # Envia todos los registros y renderiza index.html


