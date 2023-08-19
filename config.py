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
'api_key' :'64e0be0b7bb78fb3c7a1de25', 
'departure_airport_code': ['BER','FRA','MUC'],
'arrival_airport_code':['DEL','BOM','BLR','HYD','MAA'], 
'departureDate': None, 
'arrival_date': None, 
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