import json
import requests
PROPUBLICA_API_KEY = "PUT YOUR API KEY HERE BETWEEN THE PARANS"

headers = {"X-API-Key": PROPUBLICA_API_KEY}

api_url = ("https://api.propublica.org/congress/v1/116}/bills/hr195/statements.json") 
#THE URL ABOVE IS A DEFAULT URL SEARCHING FOR STATEMENTS ON A BILL NAMED HR195
#GO TO PROPUBLICA API DOCUMENTATION TO FIND HOW TO MAKE YOUR OWN URL

api_response = requests.get(api_url, headers=headers)


print(api_response.text)
