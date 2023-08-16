import logging
import os

logging.basicConfig(
    format='%(levelname)s-%(name)s:%(lineno)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level='INFO'
)
logger=logging.getLogger(__name__)

#API headers

params={
'api_key' :'64d8ff40c4386061ed958548', 
'departure_airport_code': 'BER',
'arrival_airport_code':'MAA', 
'departureDate': '2023-09-15', 
'arrival_date': '2023-10-15', 
'number_of_adults': '1', 
'number_of_childrens' : '0',
'number_of_infants': '0',
'cabin_class' : 'Economy',
'currency': 'EUR'
}


#url
url='https://api.flightapi.io/roundtrip/'

#working directory
working_dir=os.getcwd()

#DB
pg_credentials={
    'host':'localhost',
    'port':5433,
    'database':'postgres',
    'username':'postgres',
    'password':'Keerthana@123'
}