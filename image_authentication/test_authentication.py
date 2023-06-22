import requests
import os




# url="http://172.17.0.2:8000/permissions"
url="http://localhost:8000/permissions"
username=["alice", "bob", "clementine"]
password=["wonderland", "builder", "mandarine"]



for i in range(len(username)):
    request=url + "?username=" + username[i] + "&password=" + password[i]
    r = requests.get(request)


    response_dict = r.json
    response_header = r.headers
    status_code = r.status_code

    if status_code == 200:
        # with open('/home/my_folder/response.log', 'a') as file:
        #     file.write('up\n')
        print("c'est bon")
    else:
        print("c'est pas bon")
