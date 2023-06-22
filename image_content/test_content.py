import requests
import os
from datetime import datetime
import json


#application variables
api_address = "172.17.0.2"
api_port = 8000
log_dir = "/home/exam_docker/log/"
log_file = "log.txt"


#test variables
username="alice"
password="wonderland"
versions=["v1", "v2"]
sentences = ["life is beautiful", "that sucks" ]
test_name = "test #3 - content"


#creation of log directory if doesn't exist
if not os.path.isdir(log_dir):
    os.mkdir(log_dir, mode=0o755)


#test execution
if os.environ.get("LOG") == '1':
    with open(log_dir + log_file, 'a') as file:
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +\
                   " : running " + test_name + "\n") 
        for version in versions:
            for sentence in sentences:    
                file.write("   version : " + version + " | sentence : " + sentence + "\n")        
                r = requests.get(
                    url='http://{address}:{port}/{num_version}/sentiment'.format(address=api_address, port=api_port, num_version=version),
                    params= {
                        'username': username,
                        'password': password,
                        'sentence': sentence})
                result = json.loads(r.text)            
                if result['score'] >= 0:
                    file.write('     -> positif \n')
                else:
                    file.write('     -> negatif \n')
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +\
                   " : end of " + test_name + "\n")
        file.write(" --------------------\n")
        file.write("\n")
    file.close()

