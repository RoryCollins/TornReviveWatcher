import requests
from dotenv import dotenv_values

apiKey = dotenv_values(".env").get('API_KEY')


def get_user_json(user_id):
    return requests.get(f'https://api.torn.com/user/{user_id}?selections=&key={apiKey}').json()


def get_faction_json(faction_id):
    return requests.get(f'https://api.torn.com/faction/{faction_id}?selections=&key={apiKey}').json()
