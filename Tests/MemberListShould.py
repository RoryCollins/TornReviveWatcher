from MemberList import MemberList
import json

factionJson = open("stub_faction_json.json", "r")
members = json.load(factionJson)['members'].items()


def test_initialise_with_empty_set():
    member_list = MemberList(None, [])
    assert len(member_list.members) == 0


def test_initialise_with_non_empty_set():
    member_list = MemberList(None, members)
    assert len(member_list.members) == 100


def test_filter_online_members():
    f = open("stub_faction_json.json", "r")
    j = json.load(f)
    member_list = MemberList(None, members).online_only()
    assert len(member_list.members) == 3


def test_filter_offline_members():
    f = open("stub_faction_json.json", "r")
    j = json.load(f)
    member_list = MemberList(None, members).offline_only()
    assert len(member_list.members) == 87

