import requests
import os
from datetime import datetime
import json


api_address = "exam_docker_network"
api_port = 8000


username="alice"
password="wonderland"
versions=["v1", "v2"]
sentences = ["life is beautiful", "that sucks" ]





        
for version in versions:


    for sentence in sentences:          
        r = requests.get(
            url='http://{address}:{port}/{num_version}/sentiment'.format(address=api_address, port=api_port, num_version=version),
            params= {
                'username': username,
                'password': password,
                'sentence': sentence})

        # status_code = r.status_code            

        # if status_code == 200:
        #     print('     -> ' + version + ' - authorization OK\n')
        # else:
        #     print('     -> /!\ ' + version + ' - authorization NOK\n')

        print(r.text)

        result = json.loads(r.text)
        if result['score'] > 0 :
            print('positif')
        else:
            print('negatif')






