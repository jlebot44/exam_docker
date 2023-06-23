import requests
import os
from datetime import datetime


#application variables
api_address = "api_to_test"
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


#output template generation
output = '''
============================
    {test}
    {date}
============================

request done at "/permissions"
| username = {user}
| password = {password}
| version = {version}

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''


#test execution
date_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

for i in range(len(username)):
    for version in versions:            
        r = requests.get(
            url='http://{address}:{port}/{num_version}/sentiment'.format(address=api_address, port=api_port, num_version=version),
            params= {
                'username': username[i],
                'password': password[i],
                'sentence': 'test'})

        status_code = r.status_code            
    
        if status_code == 200:
            result = 'SUCCESS'
        else:
            result = 'FAILURE'

        final_result = output.format(test = test_name,
                            date = date_now,
                            user = username[i],
                            password = password[i],
                            version = version,
                            status_code = status_code,
                            test_status = result)
        
        print(final_result) 

        if os.environ.get("LOG") == '1':
            with open(log_dir + log_file, 'a') as file:
                file.write(final_result)
                file.close()

