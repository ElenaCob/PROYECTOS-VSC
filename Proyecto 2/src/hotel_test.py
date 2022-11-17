from hotel import *

def test_filtra_por_pais(registro, country):

    print("===> Test de filtra_por_pais")
    filtro = filtra_por_pais(registro, country)
    print("Leidos", len(filtro), "hoteles en España y son:")
    print("\n".join(str(r) for r in registro[:3]))
    print("###############################################################################################\n")

def test_num_total_adultos(registro):

    print("===> Test de num_total_adultos")
    total_adultos = num_total_adultos(registro)
    print("El numero total de adultos de los hoteles es")
    print("\n", total_adultos)
    print("###############################################################################################\n")

def test_registro_mas_noches_semana(registro):

    print("===> Test de registro_mas_noches_semana")
    mas_noches =  registro_mas_noches_semana(registro)
    print("Registro con mayor número de noches pasadas en la semana:")
    print("\n", mas_noches)
    print("###############################################################################################\n")

def test_mas_tiempo_espera(registro, country, n = 3):

    print("===> Test de mas_tiempo_espera")
    prioridades = mas_tiempo_espera(registro, country, n)
    print("Los registros con más tiempo de espera en Portugal son:")
    print("\n", prioridades)
    print("###############################################################################################\n")

def test_agrupar_por_companyia(registro):

    print("===> Test de agrupar_por_companyia")
    print("Diccionario que agrupa compañías:")
    print("\n".join(str(r) for r in registro[:3]))
    print("###############################################################################################\n")

if __name__=='__main__':
    REGISTRO = lee_datos_hotel("./data/hotel_bookings.csv")

    test_filtra_por_pais(REGISTRO, "ESP")
    test_num_total_adultos(REGISTRO)
    test_registro_mas_noches_semana(REGISTRO)
    test_mas_tiempo_espera(REGISTRO, "PRT")
    test_agrupar_por_companyia(REGISTRO)