import requests
import json

url = "https://translation.googleapis.com/language/translate/v2?key="
key = ypur-key

data = {
 "q": [
  "Bom dia"
 ],
 "source": "pt-br",
 "target": "en"
}
r = requests.post(url+key, data=json.dumps(data))
print(r.json())

