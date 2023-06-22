import requests
import os
from datetime import datetime




api_address = "172.17.0.2"
api_port = 8000


username=["alice", "bob", "clementine"]
password=["wonderland", "builder", "mandarine"]

log_dir = "/home/exam_docker/log/"
log_file = "log.txt"

if not os.path.isdir(log_dir):
    os.mkdir(log_dir, mode=0o755)
    print("creation du dossier")


if os.environ.get("LOG") == '1':
    with open(log_dir + log_file, 'a') as file:
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +\
                   " : running test 1 #authentication\n") 

        for i in range(len(username)):
            file.write("   user : " + username[i] + " | password : " + password[i] + "\n")
            # request=url + "?username=" + username[i] + "&password=" + password[i]
            # r = requests.get(request)

            r = requests.get(
                url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
                params= {
                    'username': username[i],
                    'password': password[i]})

            response_dict = r.json
            response_header = r.headers
            status_code = r.status_code  
            
        
            if status_code == 200:
                file.write('     -> authentication OK\n')
            else:
                file.write('     -> /!\ authentication NOK\n')
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") +\
                   " : end of test 1 #authentication\n")
        file.write(" --------------------\n")
        file.write("\n")

    file.close()

