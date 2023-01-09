from MemberList import MemberList
from TornApiService import get_faction_json

factionId = 21368
opponentFactionId = 8076

faction_targets = MemberList(get_faction_json(factionId)['members'].items()).online_only()
opponent_targets = MemberList(get_faction_json(opponentFactionId)['members'].items()).offline_only()

faction_targets.plus(opponent_targets)\
    .hospitalised_only()\
    .revivable_only()\
    .open_in_browser()
