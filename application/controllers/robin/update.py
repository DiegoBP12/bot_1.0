# -*- coding:utf-8 -*-
import web
import config as config

class Update:
    def __init__(self):
        pass

    def GET(self, id_robin):
        robin = config.model_robin.select_id_robin(id_robin) # Selecciona el registro que coincida con el nombre
        return config.render.update_robin(robin) # Envia el registro y renderiza update.html

    def POST(self,id_robin):
        formulario = web.input() # almacena los datos del formulario web
        id_robin = formulario['id_robin'] # almacena el id escrito en el input
        nombre_robin = formulario['nombre_robin'] # almacena el nombre escrito en el input
        habilidades = formulario['habilidades'] # almacena las habilidades escritas en el input
        armas = formulario['armas'] # almacena las armas en el input
        config.model_robin.update_robin(id_robin,nombre_robin,habilidades,armas) # actualiza los valores
        raise web.seeother('/index_robin') # redirecciona al index

