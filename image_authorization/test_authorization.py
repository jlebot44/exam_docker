import requests
import os
from datetime import datetime


#application variables
api_address = "172.17.0.2"
api_port = 8000
log_dir = "/home/exam_docker/log/"
log_file = "log.txt"


#tests variables
test_name = "test #2 - autorization"
username=["alice", "bob"]
password=["wonderland", "builder"]
versions=["v1", "v2"]


#creation of log directory if doesn't exist
if not os.path.isdir(log_dir):
    os.mkdir(log_dir, mode=0o755)


#test execution
if os.environ.get("LOG") == '1':
    with open(log_dir + log_file, 'a') as file:
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +\
                   " : running " + test_name + "\n") 

        for i in range(len(username)):

            file.write("   user : " + username[i] + " | password : " + password[i] + "\n")
            for version in versions:            
                r = requests.get(
                    url='http://{address}:{port}/{num_version}/sentiment'.format(address=api_address, port=api_port, num_version=version),
                    params= {
                        'username': username[i],
                        'password': password[i],
                        'sentence': 'test'})

                status_code = r.status_code            
            
                if status_code == 200:
                    file.write('     -> ' + version + ' - authorization OK\n')
                else:
                    file.write('     -> ' + version + ' - /!\ authorization NOK\n')
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +\
                   " : end of " + test_name + "\n")
        file.write(" --------------------\n")
        file.write("\n")
    file.close()

