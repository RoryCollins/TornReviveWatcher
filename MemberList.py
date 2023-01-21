import webbrowser


class MemberList(object):
    def __init__(self, apiService, members):
        self.members = members
        self.apiService = apiService

    def is_revivable(self, user_id):
        return self.apiService.get_user_json(user_id)['revivable']

    def new_member_list(self, members):
        return MemberList(self.apiService, members)

    def filter_in(self, filterList):
        return self.new_member_list([(k, v) for k, v in self.members if k in filterList])

    def online_only(self):
        return self.new_member_list([(k, v) for k, v in self.members if v['last_action']['status'] == 'Online'])

    def offline_only(self):
        return self.new_member_list([(k, v) for k, v in self.members if v['last_action']['status'] == 'Offline'])

    def hospitalised_only(self):
        return self.new_member_list([(k, v) for k, v in self.members if v['status']['state'] == 'Hospital'])

    def revivable_only(self):
        return self.new_member_list([(k, v) for k, v in self.members if self.is_revivable(k)])

    def open_if_revivable(self):
        for k, _ in self.members:
            if self.is_revivable(k):
                webbrowser.open(f'https://www.torn.com/profiles.php?XID={k}')
            else:
                print(f"not revivable: {k}")

    def plus(self, other):
        return self.new_member_list(self.members + other.members)

    def print(self):
        for k, _ in self.members:
            print(k)
