import config as config # importa el archivo config

db = config.db # crea un objeto del objeto db creado en config 

'''
Metodo para seleccionar todos los registros de la tabla Batmans
'''
def select_batman():
    try:
        return db.select('batmans') # selecciona todos los registros de la tabla de batmans
    except Exception as e:
        print "Model select_batman Error ()",format(e.args)
        print "Model select_batman Message {}",format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el id dado
'''
def select_id_batman(id_batman):
    try:
        return db.select('batmans', where= 'id_batman=$id_batman', vars=locals())[0] #selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_batman Error ()",format(e.args)
        print "Model select_batman Message {}",format(e.message)
        return None

'''
Metodo para insertar un nuevo registro 
'''
def insert_batman(id_batman,descripcion,version,aparicion):
    try:
        return db.insert('batmans',id_batman=id_batman,descripcion=descripcion,version=version,aparicion=aparicion) # inserta un registro en batmans
    except Exception as e:
        print "Model insert_batman Error ()",format(e.args)
        print "Model insert_batman Message {}",format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id_batman recibido
'''
def delete_batman(id_batman):
    try:
        return db.delete('batmans', where='id_batman=$id_batman', vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_batman Error ()",format(e.args)
        print "Model delete_batman Message {}",format(e.message)
        return None

'''
Metodo para actualizar el registro
'''
def update_batman(id_batman,descripcion,version,aparicion): # actualiza el registro
    try:
            return db.update('batmans',
            descripcion=descripcion,
            version=version,
            aparicion=aparicion,
            where='id_batman=$id_batman',
            vars=locals())
    except Exception as e:
        print "Model update_batman Error ()",format(e.args)
        print "Model update_batman Message {}",format(e.message)
        return None

