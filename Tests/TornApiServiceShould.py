from Member import Member
from Tests.MockTornApiGateway import MockTornApiGateway
from TornApiService import TornApiService


def test_get_faction_members():
    service = TornApiService(MockTornApiGateway())
    members = service.get_faction_members(1234)
    assert len(members) == 100


def test_parse_json_to_domain_object():
    service = TornApiService(MockTornApiGateway())
    members = service.get_faction_members(1234)
    expected = Member('12', "SandyClaws", False, "Offline")
    assert members[0] == expected
