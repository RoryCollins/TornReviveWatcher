import webbrowser

from TornApiService import get_user_json


def is_revivable(user_id):
    return get_user_json(user_id)['revivable']


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
