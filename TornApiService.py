class TornApiService(object):

    def __init__(self, gateway):
        self.gateway = gateway

    def get_user_json(self, user_id):
        return self.gateway.get_user_json(user_id)

    def get_faction_members(self, faction_id):
        return self.gateway.get_faction_json(faction_id)["members"].items()


