import requests
import pandas as pd
import json
import psycopg2
import config
from db_manager import DBManager
import os
from config import logging

logger = logging.getLogger(__name__)

class Api:
        def make_flight_api_request(self,**params):
         final_url = config.url
         final_url += '/'.join(str(params[key]) for key in params)
         print(final_url)
         response = requests.get(final_url)
         if response.status_code == 200:
             data = response.json()
             print(f"API response: {data}") 
             return data
         else:
             print(f"Error making API request: {response.status_code} - {response.text}")
             return None


