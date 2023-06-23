import requests
import os
from datetime import datetime


#application variables
api_address = "api_to_test"
api_port = 8000
log_dir = "/home/exam_docker/log/"
log_file = "log.txt"


#tests variables
test_name = "test #1 - authentication"
username=["alice", "bob", "clementine"]
password=["wonderland", "builder", "mandarine"]


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

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''



#test excecution
date_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

for i in range(len(username)):
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params= {
            'username': username[i],
            'password': password[i]})

    status_code = r.status_code            

    if status_code == 200:
        result = 'SUCCESS'
    else:
        result = 'FAILURE'

    final_result = output.format(test = test_name,
                        date = date_now,
                        user = username[i],
                        password = password[i],
                        status_code = status_code,
                        test_status = result)

    print(final_result) 
    
    if os.environ.get("LOG") == '1':
        with open(log_dir + log_file, 'a') as file:
            file.write(final_result)
            file.close()

