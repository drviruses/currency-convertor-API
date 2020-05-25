
def convert(value, convert_from, convert_to):
    import requests
    import json

    url = "https://api.exchangeratesapi.io/latest"
    response = requests.get(url)
    data=response.text
    parsed = json.loads(data)

    currency_base = value * parsed['rates'][convert_to]
    currency_converted = currency_base / parsed['rates'][convert_from]
    return currency_converted
initial_amount = int(input())    
print(convert(initial_amount, 'GBP', 'INR'))  # convert(initial, from , to)
