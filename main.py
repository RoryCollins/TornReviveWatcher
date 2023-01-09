import requests
import webbrowser
from dotenv import dotenv_values

config = dotenv_values(".env")
apiKey = config.get('API_KEY')
factionId = 21368
opponentFactionId = 8076


def is_revivable(user_id):
    return requests.get(f'https://api.torn.com/user/{user_id}?selections=&key={apiKey}').json()['revivable']


class MemberList(object):
    def __init__(self, members):
        self.members = members

    def online_only(self):
        return MemberList([(k, v) for k, v in self.members if v['last_action']['status'] == 'Online'])

    def offline_only(self):
        return MemberList([(k, v) for k, v in self.members if v['last_action']['status'] == 'Offline'])

    def hospitalised_only(self):
        return MemberList([(k, v) for k, v in self.members if v['status']['state'] == 'Hospital'])

    def revivable_only(self):
        return MemberList([(k, v) for k, v in self.members if is_revivable(k)])

    def plus(self, other):
        return MemberList(self.members + other.members)

    def open_in_browser(self):
        for k, v in self.members:
            webbrowser.open(f'https://www.torn.com/profiles.php?XID={k}')


faction = requests.get(f'https://api.torn.com/faction/{factionId}?selections=&key={apiKey}')
faction_targets = MemberList(faction.json()['members'].items()).online_only()

opponent_faction = requests.get(f'https://api.torn.com/faction/{opponentFactionId}?selections=&key={apiKey}')
opponent_targets = MemberList(opponent_faction.json()['members'].items()).offline_only()

faction_targets.plus(opponent_targets)\
    .hospitalised_only()\
    .revivable_only()\
    .open_in_browser()
