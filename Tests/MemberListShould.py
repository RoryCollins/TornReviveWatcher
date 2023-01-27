from MemberList import MemberList
import json

from Tests.MockTornApiGateway import MockTornApiGateway
from TornApiService import TornApiService

tornApiService = TornApiService(MockTornApiGateway())
members = tornApiService.get_faction_members(1234)


def test_initialise_with_empty_set():
    member_list = MemberList(None, [])
    assert len(member_list.members) == 0


def test_initialise_with_non_empty_set():
    member_list = MemberList(None, members)
    assert len(member_list.members) == 100


def test_filter_online_members():
    member_list = MemberList(None, members).online_only()
    assert len(member_list.members) == 2


def test_filter_offline_members():
    member_list = MemberList(None, members).offline_only()
    assert len(member_list.members) == 87


def test_filter_hospitalised_members():
    member_list = MemberList(None, members).hospitalised_only()
    assert len(member_list.members) == 3


def test_join_member_lists():
    online_members = MemberList(None, members).online_only()
    offline_members = MemberList(None, members).offline_only()
    union_members = online_members.plus(offline_members)
    assert len(union_members.members) == 89
