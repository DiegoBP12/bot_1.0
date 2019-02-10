# -*- coding:utf-8 -*-
import web
import config as config

class View():
    def __init__(self):
        pass
    
    def GET(self,id_batman):
        batman = config.model_batman.select_id_batman(id_batman) # Selecciona el registro que coincida con el nombre
        return config.render.view_batman(batman) # Envia el registro y renderiza el view.html
        