# -*- coding:utf-8 -*-
import web
import config as config

class Delete():
    def __init__(self):
        pass

    def GET(self, id_robin):
        robin = config.model_robin.select_id_robin(id_robin) # Selecciona el registro que coincida con id
        return config.render.delete_robin(robin) # Envia el registro y renderiza delete.html

    def POST(self, id_robin):
        formulario = web.input() # Crea objeto formulario con los datos enviados con el formulario
        id_robin = formulario['id_robin'] # Obtiene el nombre almacenado en el formulario
        config.model_robin.delete_robin(id_robin) # Borra el registro del codigo seleccionado
        raise web.seeother('/index_robin') # redirecciona raíz