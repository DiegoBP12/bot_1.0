# -*- coding:utf-8 -*-
import web
import config as config

class Delete():
    def __init__(self):
        pass

    def GET(self, id_batman):
        batman = config.model_batman.select_id_batman(id_batman) # Selecciona el registro que coincida con el id
        return config.render.delete_batman(batman) # Envia el registro y renderiza delete.html

    def POST(self, rfc):
        formulario = web.input() # Crea objeto formulario con los datos enviados con el formulario
        id_batman = formulario['id_batman'] # Obtiene el rfc almacenado en el formulario
        config.model_batman.delete_batman(id_batman) # Borra el registro del nombre seleccionado
        raise web.seeother('/index_batman') # redirecciona raíz