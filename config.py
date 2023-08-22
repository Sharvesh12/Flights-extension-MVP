import logging
import os
logging.basicConfig(
    format='%(levelname)s-%(name)s:%(lineno)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level='INFO'
)
logger=logging.getLogger(__name__)

#API headers


#url access token
url_token = 'https://test.api.amadeus.com/v1/security/oauth2/token'

headers_token = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
  'grant_type': 'client_credentials',
  'client_id': 'gmcFxx6JbsPXgRkVtJiltC3C1LBeOEog',
  'client_secret': 'rrqmz3JmvqaAFcGY'
}

#url API flight offers call
url= 'https://test.api.amadeus.com/v2/shopping/flight-offers'
client_id = 'gmcFxx6JbsPXgRkVtJiltC3C1LBeOEog'
client_secret = 'rrqmz3JmvqaAFcGY'

params={
    'originLocationCode': ['BER','FRA'],
    'destinationLocationCode':['DEL','BOM','BLR','MAA'], 
    'departureDate': '2023-10-01', 
    'returnDate' : None,
    'adults':1,
    'children':None,
    'infants':None,
    'travelClass':None,
    'currencyCode':'EUR',
    'maxPrice' : None
    }
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