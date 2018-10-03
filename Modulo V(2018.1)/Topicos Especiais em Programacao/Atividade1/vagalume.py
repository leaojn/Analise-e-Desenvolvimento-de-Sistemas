import requests
import json
url = "https://api.vagalume.com.br/search.artmus?q=Capital%Inicial%20Vamos%20Fugir&limit=5"

request = requests.get(url)
print(request.json())