import requests
import os

r = requests.get('http://172.17.0.2:8000/status')

response_dict = r.json
response_header = r.headers
status_code = r.status_code

if os.environ.get("LOG") == 1:
    if status_code == 200:
        with open('/home/exam_docker/response.log', 'a') as file:
            file.write('up\n')
else:
    print("variable LOG != 1")
    print(type(os.environ.get("LOG")))
    print("LOG =", os.environ.get("LOG"))
