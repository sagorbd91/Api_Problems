import requests
import json
from pprint import pprint
apicem_ip = "https://sandboxapicem.cisco.com"
credentials = {"username":"devnetuser", "password":"Cisco123!"}
version = "v1"
# https://sandboxapicem.cisco.com/api/v1/ticket
ticket_url = apicem_ip+ "/api/" + version + "/ticket"
headers = {"content-type":"application/json"}
response = requests.post(url=ticket_url, headers = headers, 
                         data = json.dumps(credentials),
                         verify = True)

print(response.status_code)
r_json = response.json()
