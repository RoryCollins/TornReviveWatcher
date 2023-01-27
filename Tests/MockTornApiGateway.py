import json


class MockTornApiGateway(object):
    def get_faction_json(self, _):
        f = open("stub_faction_json.json", "r")
        return json.load(f)
