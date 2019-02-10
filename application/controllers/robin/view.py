# -*- coding:utf-8 -*-
import web
import config as config

class View():
    def __init__(self):
        pass
    
    def GET(self,id_robin):
        robin = config.model_robin.select_id_robin(id_robin) # Selecciona el registro que coincida con el codigo
        return config.render.view_robin(robin) # Envia el registro y renderiza el view.html
        