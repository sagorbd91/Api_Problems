import requests
import json
from pprint import pprint
apicem_ip = "https://sandboxapicem.cisco.com"
credentials = {"username":"devnetuser", "password":"Cisco123!"}
version = "V1"
# https://sandboxapicem.cisco.com/api/v1/ticket
ticket_url = apicem_ip
