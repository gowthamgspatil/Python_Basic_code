import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return amount * rate

from_currency = input("From currency (e.g. USD): ").upper()
to_currency = input("To currency (e.g. INR): ").upper()
amount = float(input("Amount: "))

converted = convert_currency(from_currency, to_currency, amount)
print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
