# Torn Revive Command Line Interface

## Alright, What the hell is this?
This is a tool to help with revive contracts, ultimately it's going to be configurable as fuck - so whether you're premium or not, this is gonna help


## Usage
FIRST you need to copy `.env_example` to a file called `.env`, and update the `API_KEY` value with your own

Use `--on` for factions whose ONLINE members you want to revive

Use `--off` for factions whose OFFLINE members you want to revive


`python3 revive.py --on 1234,2345 --off 5678`


## What's coming up?

1. Unit Tests - ain't doing shit else without 'em
2. Exclusions - got some premium-only members but you ain't premium? ignore the fuckers
3. Inclusions - when the contract says only to look for a set list of users