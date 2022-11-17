from collections import namedtuple, defaultdict
from parsers import *
import csv

HotelBooking = namedtuple("HotelBooking", "hotel, is_canceled, lead_time, arrival_date_year, arrival_date_month, arrival_date_week_number, \
                         arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, meal, country, \
                         market_segment, distribution_channel, is_repeated_guest, previous_cancellations, previous_bookings_not_canceled, \
                        reserved_room_type, assigned_room_type, booking_changes, deposit_type, agent, company, days_in_waiting_list, \
                        customer_type, adr, required_car_parking_spaces, total_of_special_requests, reservation_status, \
                        reservation_status_date")

def lee_datos_hotel(ruta_fichero):
    '''
    Esta función lee un fichero de datos en formato CSV y devuelve una lista de tuplas de tipo HotelBooking.

    Un ejemplo de las líneas del fichero CSV esperado es:
    Resort Hotel,0,342,2015,July,27,1,0,0,2,0,0,BB,PRT,Direct,Direct,0,0,0,C,C,3,No Deposit,NULL,NULL,0,Transient,0,0,0,Check-Out,2015-07-01

    ENTRADA:
        @param ruta_fichero: la ruta del fichero CSV.
        @type ruta_fichero: str

    SALIDA:
        @return: lista de tuplas de tipo HotelBooking.
        @rtype: list(tuple())
    '''
    with open(ruta_fichero, mode='rt', encoding='utf-8') as f:

        lector = csv.reader(f)
        next(lector)

        hoteles = []

        for hotel, is_canceled, lead_time, arrival_date_year, arrival_date_month, arrival_date_week_number, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, meal, country, market_segment, distribution_channel, is_repeated_guest, previous_cancellations, previous_bookings_not_canceled, reserved_room_type, assigned_room_type, booking_changes, deposit_type, agent, company, days_in_waiting_list, customer_type, adr, required_car_parking_spaces, total_of_special_requests, reservation_status, reservation_status_date in lector:
            
            is_canceled = parsea_logico(is_canceled)
            lead_time = int(lead_time)
            arrival_date_year = int(arrival_date_year)
            arrival_date_week_number = int(arrival_date_week_number)
            arrival_date_day_of_month = int(arrival_date_day_of_month)
            stays_in_weekend_nights = int(stays_in_weekend_nights)
            stays_in_week_nights = int(stays_in_week_nights)
            adults = int(adults)
            children = str(children)
            babies = int(babies)
            is_repeated_guest = int(is_repeated_guest)
            previous_cancellations = int(previous_cancellations)
            previous_bookings_not_canceled = int(previous_bookings_not_canceled)
            days_in_waiting_list = int(days_in_waiting_list)
            adr = float(adr)
            required_car_parking_spaces = parsea_logico(required_car_parking_spaces)
            total_of_special_requests = parsea_logico(total_of_special_requests)
            reservation_status_date = parsea_fecha(reservation_status_date)

            t = HotelBooking(hotel, is_canceled, lead_time, arrival_date_year, arrival_date_month, arrival_date_week_number, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, meal, country, market_segment, distribution_channel, is_repeated_guest, previous_cancellations, previous_bookings_not_canceled, reserved_room_type, assigned_room_type, booking_changes, deposit_type, agent, company, days_in_waiting_list, customer_type, adr, required_car_parking_spaces, total_of_special_requests, reservation_status, reservation_status_date)
            '''
            t es una variable que guarda una línea completa y almacena el contenido
            '''
            hoteles.append(t)
    return hoteles

def filtra_por_pais(hoteles, country):
    '''
    Devuelve las tuplas correspondientes a un determinado pais

    ENTRADA:
        @param hoteles: lista de tuplas con información de hoteles
        @type hoteles: list(HotelBooking)
        @param country: siglas del país del que se seleccionarán los registros
        @type country: str
    SALIDA:
        @return: lista de tuplas (country) seleccionadas
        @rtype: list(tuple(str))
    '''
    filtradas = []
    for h in hoteles:
        if country == h.country:
            filtradas.append(h)
    return filtradas

def num_total_adultos(hoteles):
    '''
    Calcula el número total de adultos de los hoteles
    
    ENTRADA: 
       @param hoteles: lista de tuplas con información de hoteles
       @type hoteles: list (HotelBooking)
    SALIDA: 
       @return: número de adultos en el registro de los hoteles.
       @rtype: int
    '''
    suma = 0
    for hotel in hoteles:
        suma += hotel.adults
    return suma

def registro_mas_noches_semana(hoteles):
    '''
    Devuelve la semana con mayor número de noches de entre todos los registros.
    
    ENTRADA:
       @param hoteles: lista de tuplas con la información de los hoteles.
       @type hoteles: list (HotelBooking)
    SALIDA:
       @return: registro con la semana con más noches de alojamiento
       @rtype: list(tuple(str))
    '''
    lista = []
    maximo = max(hoteles, key = lambda h:h.stays_in_week_nights)
    for n in hoteles:
        if n.stays_in_week_nights == maximo.stays_in_week_nights:
            lista.append(n)
    return lista

def mas_tiempo_espera(hoteles, country, n = 3):
    '''     
    Devuelve los tres registros con mayor tiempo de espera.
    
    ENTRADA: 
      @param hoteles: lista de tuplas con información de hoteles
      @type hoteles: list(HotelBooking)
      @param country: siglas del país del que se seleccionarán los registros
      @type country: str
      @param n: número registros a mostrar 
      @type n: int
    SALIDA: 
      @return:  
      @rtype: list(tuple(str))
    '''
    lista_filtrada = filtra_por_pais(hoteles, country)

    return sorted(lista_filtrada, key = lambda h:h.lead_time, reverse = True)[:n]

def agrupar_por_companyia(hoteles):
    '''
    Devuelve un diccionario agrupado por compañías.

    ENTRADA: 
      @param hoteles: lista de tuplas con información de hoteles
      @type hoteles: list(HotelBooking)
    SALIDA: 
      @return:  
      @rtype: list(tuple(str))
    '''

    res = dict()

    for h in hoteles:
        if (not h.company in res):
            res[h.company] = []
        res[h.company].append(h)

    return res