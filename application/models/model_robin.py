import config as config # importa el archivo config

db = config.db # crea un objeto del objeto db creado en config 

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_robin():
    try:
        return db.select('robins') # selecciona todos los registros de la tabla de robins
    except Exception as e:
        print "Model select_robin Error ()",format(e.args)
        print "Model select_robin Message {}",format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el id dado
'''
def select_id_robin(id_robin):
    try:
        return db.select('robins', where= 'id_robin=$id_robin', vars=locals())[0] #selecciona el primer registro que coincida con el id
    except Exception as e:
        print "Model select_robin Error ()",format(e.args)
        print "Model select_robin Message {}",format(e.message)
        return None

'''
Metodo para insertar un nuevo registro 
'''
def insert_robin(id_robin,nombre_robin,habilidades,armas):
    try:
        return db.insert('robins',id_robin=id_robin,nombre_robin=nombre_robin,habilidades=habilidades,armas=armas) # inserta un registro en robins
    except Exception as e:
        print "Model insert_robin Error ()",format(e.args)
        print "Model insert_robin Message {}",format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id recibido
'''
def delete_robin(id_robin):
    try:
        return db.delete('robins', where= 'id_robin=$id_robin', vars=locals()) # borra un registro de productos
    except Exception as e:
        print "Model delete_robin Error ()",format(e.args)
        print "Model delete_robin Message {}",format(e.message)
        return None

'''
Metodo para actualizar 
'''
def update_robin(id_robin,nombre_robin,habilidades,armas): # actualiza el registro del producto
    try:
            return db.update('robins',
            nombre_robin=nombre_robin,
            habilidades=habilidades,
            armas=armas,
            where= 'id_robin = $id_robin',
            vars=locals())
    except Exception as e:
        print "Model update_robin Error ()",format(e.args)
        print "Model update_robin Message {}",format(e.message)
        return None

