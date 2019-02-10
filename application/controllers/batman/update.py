# -*- coding:utf-8 -*-
import web
import config as config

class Update:
    def __init__(self):
        pass

    def GET(self, id_batman):
        batman = config.model_batman.select_id_batman(id_batman) # Selecciona el registro que coincida con el id
        return config.render.update_batman(batman) # Envia el registro y renderiza update.html

    def POST(self,id_batman):
        formulario = web.input() # almacena los datos del formulario web
        id_batman = formulario['id_batman'] # almacena el id escrito en el input
        descripcion = formulario['descripcion'] # almacena la descripcion escrita en el input
        version = formulario ['version'] # almacena la version escrito en el input
        aparicion = formulario['aparicion'] # almacena la aparicion escrito en el input
        config.model_batman.update_batman(id_batman,descripcion,version,aparicion) # actualiza los valores
        raise web.seeother('/index_batman') # redirecciona al index

