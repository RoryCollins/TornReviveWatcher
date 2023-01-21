import argparse
import functools

from MemberList import MemberList
from TornApiService import *

parser = argparse.ArgumentParser(description="Tool for revivers to find available targets. Comma separation for "
                                             "multiple contracts, e.g. python3 ./revive.py --on 1234,4321 --off 5678")

parser.add_argument("-n", "--on", help="Comma separated IDs for factions whose online members should be revived")
parser.add_argument("-f", "--off", help="Comma separated IDs for factions whose offline members should be revived")

args = parser.parse_args()

onlineFactions = []
offlineFactions = []

service = TornApiService()


def get_member_list(factionId):
    return MemberList(service, service.get_faction_json(factionId)['members'].items())


if args.on is not None:
    for factionId in args.on.split(","):
        onlineFactions.append(get_member_list(factionId).online_only())

if args.off is not None:
    for factionId in args.off.split(","):
        offlineFactions.append(get_member_list(factionId).offline_only())

targets = functools.reduce(lambda a, b: a.plus(b), onlineFactions + offlineFactions)
targets.hospitalised_only().open_if_revivable()
