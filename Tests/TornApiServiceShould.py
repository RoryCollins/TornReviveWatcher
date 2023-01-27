import json

from TornApiService import TornApiService


class MockTornApiGateway(object):
    def get_faction_json(self, faction_id):
        f = open("stub_faction_json.json", "r")
        return json.load(f)


def test_get_faction_members():
    gateway = MockTornApiGateway()
    service = TornApiService(gateway)
    members = service.get_faction_members(1234)
    assert len(members) == 100
