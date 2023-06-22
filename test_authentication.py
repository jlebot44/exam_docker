import requests
import os
from datetime import datetime




# url="http://172.17.0.2:8000/permissions"
url="http://localhost:8000/permissions"
username=["alice", "bob", "clementine"]
password=["wonderland", "builder", "mandarine"]

log_dir = "/home/exam_docker/log/"
log_file = "response.log"

# if not os.path.isdir(log_dir):
#     os.mkdir(log_dir, mode=0o755)
#     print("creation du dossier")



for i in range(len(username)):
    request=url + "?username=" + username[i] + "&password=" + password[i]
    r = requests.get(request)

    response_dict = r.json
    response_header = r.headers
    status_code = r.status_code


    # if os.environ.get("LOG") == '1':
        
    #     with open(log_dir + log_file, 'a') as file:
    #         if status_code == 200:
    #             file.write('up\n')
    #         else:
    #             file.write('down\n')
    #         file.close()

    if status_code == 200:

        print("ok")
    else:
        print("nok")


r = requests.get(
    url='http://localhost:8000/permissions',
    params= {
        'username': 'alic',
        'password': 'wonderland'
    }
)

print("test :", r.status_code)


##2nd test
r = requests.get(
    url='http://localhost:8000/v1/sentiment',
    params= {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'piece of shit'
    }
)

print("second test :", r.status_code)