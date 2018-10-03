import requests
import json
token = your-token
url = "http://jaca.herokuapp.com/api/v1/eventos/"
r = requests.get(url, headers={"Authorization":"Token "+ token})

print("consulta na url " + url, r.json())

