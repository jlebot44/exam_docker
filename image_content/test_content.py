import requests
import os
from datetime import datetime
import json


#application variables
api_address = "api_to_test"
api_port = 8000
log_dir = "/home/exam_docker/log/"
log_file = "log.txt"


#test variables
username="alice"
password="wonderland"
versions=["v1", "v2"]
sentences = ["life is beautiful", "that sucks" ]
expected_result_list = ["positive", "negative"]
test_name = "test #3 - content"


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
| sentence = {sentence}

expected result = {expected_status}
actual restult = {result_status}

==>  {test_status}

'''


#test execution
date_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

for version in versions:
    for sentence, expected_result in zip(sentences, expected_result_list):
        r = requests.get(
            url='http://{address}:{port}/{num_version}/sentiment'.format(address=api_address, port=api_port, num_version=version),
            params= {
                'username': username,
                'password': password,
                'sentence': sentence})
        response = json.loads(r.text)            
        if response['score'] >= 0:
            result_status = "positive"
        else:
            result_status = "negative"

        if result_status == expected_result :
            result = 'SUCCESS'
        else:
            result = 'FAILURE'

        final_result = output.format(test = test_name,
                            date = date_now,
                            user = username,
                            password = password,
                            sentence = sentence,
                            expected_status = expected_result,
                            result_status = result_status,
                            test_status = result)
        
        print(final_result) 

        if os.environ.get("LOG") == '1':
            with open(log_dir + log_file, 'a') as file:
                file.write(final_result)
                file.close()
