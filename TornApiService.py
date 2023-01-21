import requests
from dotenv import dotenv_values


class TornApiService(object):
    apiKey = dotenv_values(".env").get('API_KEY')

    def get_user_json(self, user_id):
        return requests.get(f'https://api.torn.com/user/{user_id}?selections=&key={self.apiKey}').json()

    def get_faction_json(self, faction_id):
        return requests.get(f'https://api.torn.com/faction/{faction_id}?selections=&key={self.apiKey}').json()
