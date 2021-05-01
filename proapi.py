import json
import requests
PROPUBLICA_API_KEY = "hSgyc8zlknHEQtBBNflRDt9obUHIKEqaUqi8yei"

headers = {"X-API-Key": PROPUBLICA_API_KEY}


api_url = ("https://api.propublica.org/congress/v1/116}/bills/hr195/statements.json")


api_response = requests.get(api_url, headers=headers)


print(api_response.text)
