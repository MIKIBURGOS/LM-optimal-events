from random import choice
from opti_event_funcs import *

# DEFAULT VALUES
default_troops = 3200
troop_tier = T4
default_pacts = 7
pact_tier = P4

# BOOSTS
TRAINING_BOOST = 5.3506
MERGING_BOOST = 3.2515

# OTHER REWARDS
ANC_CORE = 100  # REAL PRICE 950
CH_CORE = 3000  # REAL PRICE 7125
BRIGHT_ORB = 1000  # REAL PRICE 2850
BRILLIANT_ORB = 3000  # REAL PRICE 7125
TOKEN = 600  # REAL PRICE 600
HOLY_STARS = 1.5  # REAL PRICE 2
MONSTER_BOOST = 300  # REAL PRICE 1000
ARMY_BOOST_20 = 200  # REAL PRICE 2400

# HOURS OF SIMULATION
HOURS = 1000000


dtp = troop_tier.points * default_troops  # default troop points
dtt = troop_tier.real_time * default_troops  # default training time
ttl = dtt  # Training time left
dpp = pact_tier.points * default_pacts  # default pact points
dmt = pact_tier.real_time * default_pacts  # default merging time
mtl = dmt  # Merging time left

solos = tuple(SOLO.solos_array)
hells = tuple(HELL.hells_array)
objects = tuple(OBJECT.objects_array)
solo_time_left = 0
current_solo = None
current_hell = None
pact_solo = False
pact_hell = False
troop_solo = False
troop_hell = False
spaa = 0  # solo points already achieved


for i in range(HOURS):
    # choose random events
    if solo_time_left == 0:
        spaa = 0  # solo_points_already_achieved
        current_solo = choice(solos)
        solo_time_left = 3
    current_hell = choice(hells)
    pact_solo = current_solo.categories[4] == "1"
    pact_hell = current_hell.categories[4] == "1"
    troop_solo = current_solo.categories[6] == "1"
    troop_hell = current_hell.categories[6] == "1"

    # skip hours when no event has merging nor training
    if pact_solo or pact_hell or troop_solo or troop_hell:
        # calculate if it's worth it to speed up (and do if it is)
        speed_up()

    # prepare for next hour
    solo_time_left -= 1

    ttl -= 3600
    if ttl <= 0:
        spaa += dtp * troop_solo
        ttl += dtt

    mtl -= 3600
    if mtl <= 0:
        spaa += dpp * pact_solo
        mtl += dmt

print(TOTAL_SPEEDUPS_EARNED, TOTAL_SPEEDUPS_USED, (TOTAL_SPEEDUPS_EARNED - TOTAL_SPEEDUPS_USED) / 3600)
