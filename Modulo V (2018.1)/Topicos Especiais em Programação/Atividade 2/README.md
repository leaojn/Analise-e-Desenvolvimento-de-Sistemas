## Atividade 2 - TEP-I
1) Nome da API:

	- Eventbrite APIv3 Developer

2) Utilidade:

	- API para criação de eventos e para ajudar na organização

3) Link ou endpoint:

	- Todos os endpoints da API estão descritos neste link: https://www.eventbrite.com/developer/v3/

	- Os endpoints utilizados foram: 
	    - https://www.eventbriteapi.com/v3/events/ID_EVENTO/?token=SEU_TOKEN

	    - https://www.eventbriteapi.com/v3/events/?token=SEU_TOKEN


4) Possíveis recursos:
	- Criação de eventos, alteração, configuração de descontos, pagamentos.
5) Métodos suportados:
 	 - A API suporta requisiçoes GET, POST, DELETE
6) Exemplo(s) em python do método **GET**:
	  ``` python  
	   def get_event(id):
	     url_events = "https://www.eventbriteapi.com/v3/events/%s/?token=" %(str(id))
	     return url_events + key
	   if __name__ == "__main__":
		id = pass-id
		event = get_event(id)
		print(r.get(event).json())
	  ```
   
7) Exemplo(s) em python do pétodo **POST**:
	 ``` python
	    url_events = "https://www.eventbriteapi.com/v3/events/?token="
	    key = your-token

	    evento = {
		  "event.name.html": str(nome),
		  "event.description.html": str(description),
		  "event.start.timezone": "America/Chicago",
		  "event.start.utc": "2018-08-10T18:00:00Z",
		  "event.end.timezone": "America/Chicago",
		  "event.end.utc": "2018-08-12T18:00:00Z",
		  "event.currency": "USD"
		}
		req= r.post(url_events+key, data=evento).json()

	  ```
