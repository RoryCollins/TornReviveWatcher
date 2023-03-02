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
        return self.new_member_list([m for m in self.members if m.user_id in filterList])

    def online_only(self):
        return self.new_member_list([m for m in self.members if m.activity_status == "Online"])

    def offline_only(self):
        return self.new_member_list([m for m in self.members if m.activity_status == "Offline"])

    def hospitalised_only(self):
        return self.new_member_list([m for m in self.members if m.hospitalised])

    def revivable_only(self):
        return self.new_member_list([m for m in self.members if self.is_revivable(m.user_id)])

    def print_if_revivable(self):
        for m in self.members:
            if self.is_revivable(m.user_id):
                print(f"{m.name} [{m.user_id}]")

    def open_if_revivable(self):
        for m in self.members:
            if self.is_revivable(m.user_id):
                webbrowser.open(f'https://www.torn.com/profiles.php?XID={m.user_id}')
            else:
                print(f"not revivable: {m.name} [{m.user_id}]")

    def plus(self, other):
        return self.new_member_list(self.members + other.members)

    def print(self):
        for m in self.members:
            print(f"{m.name} [{m.user_id}]")
