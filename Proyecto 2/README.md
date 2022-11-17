# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  22/23)
Autor/a: Elena Cobano Cruz;   uvus:KNW9728;

Revisión, reestructuración y adaptación para FP: Nicolás Sánchez


El proyecto tiene como objetivo analizar los datos de un hotel publicados en el dataset de Kaggle. El dataset original tiene 59 columnas, ninguna de las cuales es de tipo fecha. Así que, por una parte, se ha recortado el número de columnas escogiendo sólo 13 de las 59 columnas, y se han añadido dos columnas, una de tipo entero que recoge el dinero que tiene en el banco la persona, y otra columna de tipo fecha, que se ha generado con fechas aleatorias y que representa la fecha en la que se perdió el trabajo.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **hotel.py**: Contiene funciones para explotar los datos sobre pobreza.
    * **hotel_test.py**: Contiene funciones de test para probar las funciones del módulo `hotel.py`. En este módulo está el main
    * **parsers.py**: Contiene funciones de parseo de datos.
* **/data**: Contiene el dataset o datasets del proyecto
    * **hotel_bookings.csv**: Archivo con los datos de pobreza que van a ser explotados.
        
## Estructura del *dataset*

Cada fila del dataset recoge los datos anonimizados de una persona, es decir, no sabemos sus nombre ni sus apellidos. Para cada persona se registran 15 datos. Por lo tanto, el dataset está compuesto por 15 columnas, con la siguiente descripción:

* **hotel**: de tipo str.
* **is_canceled**: de tipo bool.
* **lead_time**: de tipo int.
* **arrival_date_year**: de tipo int.
* **arrival_date_month**: de tipo str.
* **arrival_date_week_number**: de tipo int.
* **arrival_date_day_of_month**: de tipo int.
* **stays_in_weekend_nights**: de tipo int.
* **stays_in_week_nights**: de tipo int.
* **adults**: de tipo int.
* **children**: de tipo int.
* **babies**: de tipo int.
* **meal**: de tipo str.
* **country**: de tipo str.
* **market_segment**: de tipo str.
* **distribution_channel**: de tipo str.
* **is_repeated_guest**: de tipo int.
* **previous_cancellations**: de tipo int.
* **previous_bookings_not_canceled**: de tipo int.
* **assigned_room_type**: de tipo str.
* **booking_changes**: de tipo str.
* **deposit_type**: de tipo str.
* **agent**: de tipo str.
* **company**: de tipo str.
* **days_in_waiting_list**: de tipo int.
* **customer_type**: de tipo str.
* **adr**: de tipo float.
* **required_car_parking_spaces**: de tipo bool.
* **total_of_special_requests**: de tipo bool.
* **reservation_status**: de tipo str.
* **reservation_status_date**: de tipo datetime.


## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

`HotelBooking = namedtuple('hotel','is_canceled, lead_time, arrival_date_year, arrival_date_month, arrival_date_week_number,
                          arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children,
                          babies, meal, country, market_segment, distribution_channel, is_repeated_guest, previous_cancellations, previous_bookings_not_canceled, assigned_room_type, booking_changes, deposit_type, agent, company, days_in_waiting_list, customer_type, adr, required_car_parking_spaces, total_of_special_requests, reservation_status, reservation_status_date')`

en la que los tipos de cada uno de los campos están descritos arriba.

## Funciones implementadas
En este proyecto se han implementado las siguientes funciones, que están clasificadas según los bloques y tipos de funciones que se requieren en cada una de las entregas.
El módulo principal es el módulo hotel.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.
### Módulo hotel

  * **lee_datos_hotel(ruta_fichero)**: lee los datos del fichero csv y devuelve una lista de tuplas de tipo HotelBooking con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en el [módulo `parsers`].

  * **filtra_por_pais(hoteles, country)**: devuelve las tuplas correspondientes a un determinado pais.

  * **num_total_adultos(hoteles)**: calcula el número total de adultos de los hoteles.

  * **registro_mas_noches_semana(hoteles)**: devuelve la semana con mayor número de noches de entre todos los registros.

  * **mas_tiempo_espera(hoteles, country, n = 3)**: devuelve los tres registros con mayor tiempo de espera.

  * **agrupar_por_companyia(hoteles)**: devuelve un diccionario agrupado por compañías.
    
### Módulo hotel_test
En el módulo de pruebas se han definido la siguiente función de pruebas, se usa para probar la función que tiene el mismo nombre (pero sin comenzar por `test\_` del módulo `hotel`. Por ejemplo, la función `test_lee_fichero` prueba la función `lee_fichero`.

* **test_filtra_por_pais(registro, country)**
* **test_num_total_adultos(registro):**
* **test_registro_mas_noches_semana(registro)**
* **test_mas_tiempo_espera(registro, country, n = 3)**
* **test_agrupar_por_companyia(registro)**

### Módulo parsers

Este módulo contiene las siguientes funciones de parseo de datos:

* **parsea_logico(cadena)**: Dada una cadena, devuelve `True` si la cadena contiene el literal 'Si' (independientemente de si está escrtio en mayúsculas o minúsculas); devuelve `False`, si contiene el literal 'No'; y en cualquier otro caso devuelve `None`.
* **parsea_fecha(cadena)**: Dada una cadena, devuelve un objeto datetime con la información de la fecha.