import requests
import os
from datetime import datetime


api_address = "localhost"
api_port = 8000


username=["alice", "bob"]
password=["wonderland", "builder"]
versions=["v1", "v2"]





        
for version in versions:
    for i in range(len(username)):

                
        r = requests.get(
            url='http://{address}:{port}/{num_version}/sentiment'.format(address=api_address, port=api_port, num_version=version),
            params= {
                'username': username[i],
                'password': password[i],
                'sentence': 'test'})

        status_code = r.status_code            
    
        if status_code == 200:
            print('     -> ' + version + ' - authorization OK\n')
        else:
            print('     -> /!\ ' + version + ' - authorization NOK\n')



