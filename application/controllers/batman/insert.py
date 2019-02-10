import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert_batman() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        id_batman = formulario['id_batman'] # almacena el id escrito en el input
        descripcion = formulario['descripcion'] # almacena la descripcion escrita en el input
        version = formulario ['version'] # almacena la version escrito en el input
        aparicion = formulario['aparicion'] # almacena la aparicion escrito en el input
        config.model_batman.insert_batman(id_batman,descripcion,version,aparicion) # llama al metodo insert_batman y le pasa los datos guardados 
        raise web.seeother('/index_batman') # redirecciona el HTML 
