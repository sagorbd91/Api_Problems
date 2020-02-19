import requests
import json
from pprint import pprint
apicem_ip = "https://sandboxapicem.cisco.com"
credentials = {"username":"devnetuser", "password":"Cisco123!"}
version = "v1"
# https://sandboxapicem.cisco.com/api/v1/ticket
ticket_url = apicem_ip+ "/api/" + version + "/ticket" # made ticket through variable
headers = {"content-type":"application/json"}
response = requests.post(url=ticket_url, headers = headers, 
                         data = json.dumps(credentials),
                         verify = True)

print(response.status_code)
r_json = response.json()
pprint(r_json)

ticket = r_json['response']['serviceTicket'] # get service ticket from the response
print(ticket)

user_url = apicem_ip + "/api/" + version + "/user"
headers = {"content-type":"application/json", 
            "X-Auth-Token": ticket}

response = requests.get(url=user_url, headers = headers)

print(response.status_code)
r_json = response.json()
pprint(r_json)

username = r_json['response'][0]['username']
print(username)






