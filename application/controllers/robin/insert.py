import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert_robin() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        id_robin = formulario['id_robin'] # almacena el id escrito en el input
        nombre_robin = formulario['nombre_robin'] # almacena el nombre escrito en el input
        habilidades = formulario['habilidades'] # almacena las habilidades escritas en el input
        armas = formulario['armas'] # almacena las armas en el input
        config.model_robin.insert_robin(id_robin,nombre_robin,habilidades,armas) # llama al metodo insert_robin y le paso los datos guardados 
        raise web.seeother('/index_robin') # redirecciona el HTML 
