import requests

#https://www.eventbrite.com/developer/v3/ todos os endpoints
url_events = "https://www.eventbriteapi.com/v3/events/?token="
key = your-token

r = requests



def get_event(id):
	url_events = "https://www.eventbriteapi.com/v3/events/%s/?token=" %(str(id))
	return url_events + key

def post_event(nome, description):
	evento = {
	  "event.name.html": str(nome),
	  "event.description.html": str(description),
	  "event.start.timezone": "America/Chicago",
	  "event.start.utc": "2018-08-10T18:00:00Z",
	  "event.end.timezone": "America/Chicago",
	  "event.end.utc": "2018-08-12T18:00:00Z",
	  "event.currency": "USD"
	}
	re= r.post(url_events+key, data=evento).json()

	return re

if __name__ == "__main__":
	json = post_event("Teste esse evento","evento importante")
	id = json['id']
	event = get_event(id)

	print(r.get(event).json())


