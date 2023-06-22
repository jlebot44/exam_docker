import requests
import os

r = requests.get('http://localhost:8000/status')

response_dict = r.json
response_header = r.headers
status_code = r.status_code

if status_code == 200:
    with open('/home/my_folder/response.log', 'a') as file:
        file.write('up\n')
