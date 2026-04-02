import requests

def get_current_weather(location: str) -> str:
    return f"{location} is sunny, 25 degrees Celsius."

def get_exchange_rate(base: str, target: str) -> str:
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'].get(target)
    return f"1 {base} = {rate} {target}"