from datetime import datetime

def parsea_logico(cadena):
    '''
    Recibe una cadena con 'Si' o 'No', y devuelve True
    en el primer caso, y False en el segundo caso
    '''
    if cadena == 'Si':
        return True
    else:
        return False

def parsea_fecha(cadena):
    '''
    Recibe una cadena con el formato 'día/mes/año',
    y devuelve un objeto datetime con esa información.
    '''
    return datetime.strptime(cadena, "%Y-%m-%d")