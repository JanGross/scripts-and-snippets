#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

session = requests.Session() #Persistent session because we neeed the PHPSESSID

config_data =  {
    'login':'minzkraut', 'password':'VTVu5DLlTtr5msbfWr0Kx9ZapOx7O5o5U2x5WZAr', # Username and public key
    'cpu_family': '6', 'cpu_model': '60',                                       # Required but dummy data
    'cpu_model_name': 'Intel%28R%29+Core%28TM%29+i5-4670K+CPU+%40+3.40GHz',     # -
    'cpu_cores': '4', 'os': 'windows', 'ram': '16645524', 'bits': '64bit',      # -
    'version': '5.1686'                                                         # Keep this up to date
}

session.post('https://client.sheepit-renderfarm.com/server/config.php', config_data)
result = session.post('https://client.sheepit-renderfarm.com/server/request_job.php')
soup = BeautifulSoup(result.content, 'html.parser')

print(soup.find('stats')['credits_total'])
