from Member import Member


class TornApiService(object):

    def __init__(self, gateway):
        self.gateway = gateway

    def get_user_json(self, user_id):
        return self.gateway.get_user_json(user_id)

    def get_faction_members(self, faction_id):
        result_map = map(
            lambda x: Member(x[0], x[1]["name"], x[1]['status']['state'] == "Hospital", x[1]['last_action']['status']),
            self.gateway.get_faction_json(faction_id)["members"].items())
        return list(result_map)

