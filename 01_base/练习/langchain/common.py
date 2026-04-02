import requests

def get_exchange_rate(base: str, target: str) -> str:
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'].get(target)
    return f"1 {base} = {rate} {target}"
print(get_exchange_rate("USD", "EUR"), get_exchange_rate("USD", "JPY"), get_exchange_rate("CNY", "JPY"))