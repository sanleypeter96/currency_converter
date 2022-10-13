import requests
import json

def rate(Source, Destination):
    API_KEY = 'EgowJEA5qBi46PVUYW6vwy8SPx9J5bNa'
    url = f"https://api.apilayer.com/fixer/latest?symbols={Destination}&base={Source}"

    payload = {}
    headers= {
    "apikey": "EgowJEA5qBi46PVUYW6vwy8SPx9J5bNa"
    }

    response = requests.request("GET", url, headers=headers, data = payload).text
    response = json.loads(response)
    return 87
    return response['rates'][Destination]