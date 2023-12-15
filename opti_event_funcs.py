from math import ceil

# TOTAL VARIABLES
TOTAL_SPEEDUPS_USED = 0  # Seconds
TOTAL_SPEEDUPS_EARNED = 0  # Seconds
TOTAL_ENERGY_EARNED = 0  # Energy
TOTAL_GEMS_EARNED = 0  # Gems
TOTAL_OTHER_EARNED = 0  # Gems
TOTAL_REWARDS_EARNED = 0  # Gems
TOTAL_TIMES_SPED_UP = 0  # not even sure this is useful, I created it hoping it could be useful for some V2 improvements


class OBJECT:
    objects_array = []

    def __init__(self, category, order, time, points, t_boost=TRAINING_BOOST, m_boost=MERGING_BOOST):
        OBJECT.objects_array.append(self)
        self.category = category
        self.order = order
        self.time = time
        self.points = points
        if category == "pact":
            self.real_time = self.time / (t_boost + 1)
        elif category == "troop":
            self.real_time = self.time / (m_boost + 1)


class SOLO:
    solos_array = []

    def __init__(self, categories, points, speedups, energy=[0, 0, 0, 0], gems=[0, 0, 0, 0], other=[0, 0, 0, 0]):
        SOLO.solos_array.append(self)
        self.categories = categories
        # binary with 7 numbers, for Building, MH, Tycoon, Labyrinth, Pacts, Research and Training
        # Abbreviations:               (B)    (MH)  (Ty)      (L)      (P)      (R)         (Tr)
        self.points = [0] + points
        self.speedups = [0] + list(j * 60 for j in speedups)
        self.energy = [0] + energy
        self.gems = [0] + gems
        self.other = [0] + other
        self.rewards = [(int(self.speedups[i] / 57.6) + (self.energy[i] * 0.15) + self.gems[i] + self.other[i]) for i in range(len(self.speedups))]
        # speedups and energy transformed into gem values


class HELL:
    hells_array = []

    def __init__(self, categories, points, speedups, energy=[0, 0, 0, 0], gems=[0, 0, 0, 0], other=[0, 0, 0, 0]):
        HELL.hells_array.append(self)
        self.categories = categories
        # binary with 7 numbers, for Building, MH, Tycoon, Labyrinth, Pacts, Research and Training
        # Abbreviations:               (B)    (MH)  (TY)      (L)      (P)      (R)         (TR)
        self.points = [0] + points
        self.speedups = [0] + list(j * 60 for j in speedups)
        self.energy = [0] + energy
        self.gems = [0] + gems
        self.other = [0] + other
        self.rewards = [(int(self.speedups[i] / 57.6) + (self.energy[i] * 0.15) + self.gems[i] + self.other[i]) for i in range(len(self.speedups))]
        # speedups and energy transformed into gem values


# EVENTS, TODO SOME MIGHT BE MISSING
# region
# ONE SOURCE SOLO EVENTS
SB1 = SOLO("1000000", [3100, 7800, 31200], [20, 65, 425], [0, 1000, 3000])
SB2 = SOLO("1000000", [4800, 14400, 48000], [30, 150, 720], [0, 2000, 4000], [0, 0, 100])
SMH1 = SOLO("0100000", [360, 1080, 3600], [30, 90, 285])
SMH2 = SOLO("0100000", [500, 1250, 5000], [30, 90, 300])
STY1 = SOLO("0010000", [900, 2700, 9000], [15, 45, 255])
STY2 = SOLO("0010000", [2400, 7200, 24000], [30, 60, 330])
SL1 = SOLO("0001000", [1900, 4900, 19400], [30, 90, 285])
# TODO SL2 = SOLO("0001000", [0, 0, 24400], [0, 0, 0]) NOT IN FANDOM
SP1 = SOLO("0000100", [5600, 16800, 56000], [20, 35, 200])
SP2 = SOLO("0000100", [7150, 21450, 71500], [20, 45, 210])  # TODO NOT IN FANDOM, SPEEDUP VALUES TO BE CHECKED FOR STAGE 1 AND 2
SR1 = SOLO("0000010", [1500, 4500, 15000], [10, 30, 150], [0, 1000, 3000])
SR2 = SOLO("0000010", [2200, 5500, 22000], [20, 35, 275], [0, 2000, 6000])
STR1 = SOLO("0000001", [3600, 9000, 36000], [10, 60, 300], [0, 1000, 3000])
STR2 = SOLO("0000001", [6000, 18000, 60000], [20, 110, 470], [0, 2000, 6000])

# TWO SOURCE SOLO EVENTS
SPTR1 = SOLO("0000101", [4800, 12000, 48000], [15, 50, 230], [0, 2000, 2000])
SPB1 = SOLO("1000100", [3100, 7800, 31200], [20, 65, 425], [0, 1000, 3000])
# TODO SPR1 = SOLO("0000110", [0, 0, 45000], [0, 0, 0]) NOT IN FANDOM
SPR2 = SOLO("0000110", [4800, 12000, 48000], [20, 35, 275], [0, 2000, 6000])
STRB1 = SOLO("1000001", [6000, 18000, 60000], [20, 110, 470], [0, 2000, 6000])
STRB2 = SOLO("1000001", [6300, 18900, 63000], [20, 80, 200], [0, 2000, 6000])
STRR1 = SOLO("0000011", [4800, 12000, 48000], [15, 50, 230], [0, 2000, 2000])
STRR2 = SOLO("0000011", [6300, 18900, 63000], [20, 80, 200], [0, 2000, 6000])
SBR1 = SOLO("1000010", [3900, 10000, 30000], [20, 80, 500], [0, 2000, 4000])
SBR2 = SOLO("1000010", [4500, 13500, 45000], [20, 80, 560], [0, 2000, 4000], [0, 0, 100])
SLTR1 = SOLO("0001001", [6200, 18600, 62000], [30, 90, 315])
# TODO SLB1 = SOLO("1001000", [0, 0, 45000], [0, 0, 0]) NOT IN FANDOM
SLB2 = SOLO("1001000", [6200, 18600, 62000], [30, 90, 315])
STYP1 = SOLO("0010100", [1300, 3900, 13000], [30, 60, 195])
STYB1 = SOLO("1010000", [1300, 3900, 13000], [30, 60, 195])

# THREE SOURCE SOLO EVENTS
SLTRB1 = SOLO("1001001", [6600, 19800, 66000], [30, 90, 285])
STRBR1 = SOLO("1000011", [3600, 9000, 36000], [10, 60, 300], [0, 1000, 3000])
STRBR2 = SOLO("1000011", [4800, 12000, 48000], [15, 50, 230], [0, 1000, 1000])

# FOUR SOURCE SOLO EVENTS
# TODO SPTRBR1 = SOLO("1000111", [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
SLTRBR1 = SOLO("1001011", [6600, 19800, 66000], [30, 90, 285])

# ONE SOURCE HELL EVENTS
HB1 = HELL("1000000", [23000, 69000, 230000], [60, 435, 1125], [0, 1000, 4000], [0, 0, 800])
HB2 = HELL("1000000", [18500, 66600, 370000], [90, 330, 1770], [0, 1000, 7000], [0, 0, 1800], [0, 0, TOKEN + HOLY_STARS * 200])
HB3W = HELL("1000000", [29500, 106200, 590000], [180, 720, 4320], [0, 1000, 15000], [0, 0, 2200])
HB4CD = HELL("1000000", [33000, 118000, 660000], [180, 720, 4440], [0, 2000, 18000], [0, 0, 2300])
HMH1 = HELL("0100000", [700, 2600, 14300], [25, 70, 190], [0, 0, 0], [0, 0, 600])
HMH2W = HELL("0100000", [900, 3200, 17800], [25, 50, 185], [0, 0, 0], [0, 0, 600])
HMH3CD = HELL("0100000", [1300, 4700, 26000], [130, 155, 320], [0, 0, 0], [0, 0, 900])
HTY1 = HELL("0010000", [6900, 20700, 69000], [0, 45, 225], [0, 0, 0], [0, 0, 400])
HTY2W = HELL("0010000", [12800, 38400, 128000], [0, 90, 465], [0, 0, 0], [0, 0, 800])
HTY3CD = HELL("0010000", [17500, 52500, 175000], [0, 90, 645], [0, 0, 0], [0, 0, 1100])
HL1 = HELL("0001000", [18400, 46000, 230000], [180, 600, 3780], [0, 0, 0], [0, 0, 600])
HL2W = HELL("0001000", [34300, 85800, 343000], [360, 1020, 3420], [0, 0, 0], [0, 0, 800], [0, 0, MONSTER_BOOST + ARMY_BOOST_20])
# TODO HL3CD = HELL("0000000", [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HP1 = HELL("0000100", [29000, 72500, 290000], [15, 75, 510], [0, 0, 0], [0, 0, 600], [0, 0, ANC_CORE])
HP2 = HELL("0000100", [43000, 107500, 430000], [15, 150, 660], [0, 0, 0], [0, 0, 1300], [0, 0, ANC_CORE])
HP3SC = HELL("0000100", [57500, 143800, 575000], [15, 150, 810], [0, 0, 0], [0, 0, 1800], [0, ANC_CORE, ANC_CORE * 2])
HP4W = HELL("0000100", [75000, 187500, 750000], [15, 150, 990], [0, 0, 0], [0, 0, 2300])
HP5CD = HELL("0000100", [93000, 232500, 930000], [15, 150, 1530], [0, 0, 0], [0, 0, 2700])
HR1 = HELL("0000010", [26400, 66000, 330000], [60, 330, 1365], [0, 0, 4000], [0, 0, 900])
HR2 = HELL("0000010", [33000, 118800, 660000], [80, 500, 2420], [0, 1000, 10000], [0, 0, 1800], [0, HOLY_STARS * 200, HOLY_STARS * 1400 + TOKEN * 2])
HR3W = HELL("0000010", [48000, 172800, 960000], [180, 670, 3730], [0, 2000, 16000], [0, 0, 2600])
HR4CD = HELL("0000010", [62500, 225000, 1250000], [180, 630, 5310], [0, 2000, 14000], [0, 0, 2700])
HTR1 = HELL("0000001", [28000, 84000, 280000], [60, 300, 960], [0, 1000, 7000], [0, 0, 900])
# TODO HTR2 = HELL("0000001", [0, 0, 320000], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HTR3 = HELL("0000001", [21000, 75600, 420000], [60, 235, 1330], [0, 1000, 12000], [0, 0, 1300])
HTR4 = HELL("0000001", [37000, 133200, 740000], [60, 360, 2280], [1000, 4000, 22000], [0, 0, 2300])

# TWO SOURCE HELL EVENTS
HPTR1 = HELL("0000101", [31500, 113400, 630000], [120, 540, 1980], [0, 0, 0], [0, 0, 1900], [0, CH_CORE, CH_CORE])
# TODO HPTR2 = HELL("0000101", [31500, 113400, 630000], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
# TODO HPTR3 = HELL("0000101", [0, 0, 660000], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HPB1 = HELL("1000100", [15800, 56700, 315000], [120, 240, 1575], [0, 3000, 7000], [0, 0, 1100], [0, BRIGHT_ORB, BRIGHT_ORB * 4 + MONSTER_BOOST])
# TODO HPB2 = HELL("1000100", [44100, 132300, 441000], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HPB3 = HELL("1000100", [35300, 88200, 441000], [90, 330, 1890], [0, 1000, 7000], [0, 0, 1800], [0, 0, HOLY_STARS * 200])
HPR1 = HELL("0000110", [39000, 97600, 488000], [60, 150, 825], [0, 0, 0], [0, 0, 1500], [0, HOLY_STARS * 100, HOLY_STARS * 800])
HPR2 = HELL("0000110", [39000, 97600, 488000], [60, 300, 1680], [0, 0, 0], [0, 0, 1500], [0, BRIGHT_ORB + ANC_CORE, BRIGHT_ORB * 5 + ANC_CORE])
HPR3 = HELL("0000110", [44100, 158800, 882000], [150, 330, 3210], [0, 0, 0], [0, 0, 2400], [0, BRILLIANT_ORB + ANC_CORE, BRILLIANT_ORB * 3 + ANC_CORE * 2])
HTRB1 = HELL("1000001", [28000, 84000, 280000], [60, 285, 735], [0, 1000, 7000], [0, 0, 800])
HTRB2 = HELL("1000001", [37000, 133200, 740000], [60, 360, 2280], [1000, 4000, 22000], [0, 0, 2300])
HTRB3 = HELL("1000001", [66400, 166000, 830000], [120, 420, 2460], [2000, 5000, 22000], [0, 0, 2500])
HTRR1 = HELL("0000011", [32000, 96000, 320000], [60, 270, 990], [0, 1000, 7000], [0, 0, 900])
HTRR2 = HELL("0000011", [44800, 112000, 560000], [60, 270, 1410], [0, 2000, 19000], [0, 0, 1800])
HTRR3 = HELL("0000011", [66400, 166000, 830000], [120, 420, 2460], [1000, 4000, 26000], [0, 0, 2500])
HBR1 = HELL("1000010", [27000, 81000, 270000], [120, 525, 1905], [0, 1000, 5000], [0, 0, 800])
HBR2 = HELL("1000010", [40000, 100000, 500000], [60, 480, 2700], [0, 1000, 10000], [0, 0, 1900], [0, 0, HOLY_STARS * 500 + TOKEN * 2])
HBR3 = HELL("1000010", [45600, 114000, 570000], [120, 540, 3000], [0, 4000, 15000], [0, 0, 2100], [0, HOLY_STARS * 100, HOLY_STARS * 600 + TOKEN * 3])
# TODO HBR4 = HELL("1000010", [0, 0, 590000], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HLTR1 = HELL("0001001", [53700, 134200, 671000], [360, 1020, 4440], [0, 0, 0], [0, 0, 800], [0, 0, MONSTER_BOOST * 2])
HLB1 = HELL("1001000", [53700, 134200, 671000], [360, 1020, 4440], [0, 0, 0], [0, 0, 800])

# THREE SOURCE HELL EVENTS
# TODO HPTRB1 = HELL("1000101", [0, 0, 630000], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HPTRB2 = HELL("1000101", [34700, 124700, 693000], [60, 240, 2130], [1000, 4000, 22000], [0, 0, 2000])
HPTRB3 = HELL("1000101", [34700, 124700, 693000], [120, 600, 2310], [0, 0, 0], [0, 0, 2100], [0, BRIGHT_ORB + CH_CORE, BRIGHT_ORB * 5 + CH_CORE])
# TODO HPTRB4 = HELL("1000101", [34700, 124700, 693000], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HPTRB5 = HELL("1000101", [60500, 151200, 756000], [60, 240, 2460], [2000, 5000, 22000], [0, 0, 2300])
HPTRR1 = HELL("0000111", [60500, 151200, 756000], [120, 600, 2520], [0, 0, 0], [0, 0, 2200], [0, BRILLIANT_ORB + ANC_CORE, BRILLIANT_ORB * 3 + ANC_CORE * 2])
# TODO HPBR1 = HELL("1000110", [0, 0, 560000], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) NOT IN FANDOM
HPBR2 = HELL("1000110", [31500, 113400, 630000], [120, 540, 3480], [0, 0, 0], [0, 0, 2000], [0, BRIGHT_ORB + ANC_CORE, BRIGHT_ORB * 5 + ANC_CORE * 2 + TOKEN * 2])
HTRBR1 = HELL("1000011", [320000, 96000, 320000], [60, 240, 900], [0, 1000, 6000], [0, 0, 900])
HTRBR2 = HELL("1000011", [320000, 96000, 320000], [60, 270, 960], [0, 2000, 6000], [0, 0, 900], [0, BRIGHT_ORB, BRIGHT_ORB * 4])
HTRBR3 = HELL("1000011", [21000, 75600, 420000], [60, 235, 1330], [0, 1000, 12000], [0, 0, 1300])  # TODO FANDOM TYPO? STEP 2 15M*13
HTRBR4 = HELL("1000011", [44800, 112000, 560000], [60, 270, 1395], [1000, 3000, 20000], [0, 0, 1800])
HLTRB1 = HELL("1001001", [79000, 197500, 790000], [480, 1560, 5520], [0, 0, 0], [0, 0, 1000], [0, 0, MONSTER_BOOST])

# FOUR SOURCE HELL EVENTS
HPTRBR1 = HELL("1000111", [40300, 100800, 504000], [60, 270, 1260], [1000, 3000, 20000], [0, 0, 1600])
HPTRBR2 = HELL("1000111", [40300, 100800, 504000], [120, 435, 1650], [0, 0, 0], [0, 0, 1800], [0, ANC_CORE, ANC_CORE * 2])  # NOT IN FANDOM, CHECKED
HLTRBR1 = HELL("1001011", [79000, 197500, 790000], [480, 1560, 5520], [0, 0, 0], [0, 0, 1000])
# endregion

# TROOPS AND PACTS
P1 = OBJECT('pact', 1, 5400, 1200)
P2 = OBJECT('pact', 2, 10800, 2400)
P3 = OBJECT('pact', 3, 18000, 4800)
P4 = OBJECT('pact', 4, 28800, 9000)
T1 = OBJECT('troop', 1, 15, 1)
T2 = OBJECT('troop', 2, 30, 2)
T3 = OBJECT('troop', 3, 60, 5)
T4 = OBJECT('troop', 4, 120, 15)

def find_step(points_to_achieve: list, points_achieved):
    for step in range(len(points_to_achieve)):
        if points_to_achieve[step] > points_achieved:
            return step - 1
    return len(points_to_achieve) - 1


def extra_troops(points_to_achieve, points_achieved):
    return max(ceil((points_to_achieve - points_achieved) / troop_tier.points), 0)


def extra_pacts(points_to_achieve, points_achieved):
    return max(ceil((points_to_achieve - points_achieved) / pact_tier.points), 0)


def speed_up():
    global current_solo, current_hell, pact_solo, pact_hell, troop_solo, troop_hell, TOTAL_SPEEDUPS_USED, TOTAL_SPEEDUPS_EARNED, ttl, mtl, TOTAL_TIMES_SPED_UP, spaa

    solo = current_solo
    hell = current_hell
    ps = pact_solo
    ph = pact_hell
    ts = troop_solo
    th = troop_hell
    srac = solo.speedups[find_step(solo.points, spaa)]  # solo_rewards_already_claimed

    # GRID 1 (None|P or P|None)
    if (ps and not ph and not ts and not th) or (ph and not ps and not ts and not th):
        # OPTION 1 (P)
        o1_solo_step = find_step(solo.points, dpp * ps + spaa)
        o1_hell_step = find_step(hell.points, dpp * ph)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = mtl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (P+)
        if ps:
            o2_solo_step = min(o1_solo_step + 1, 3)
            o2_extra_pacts = extra_pacts(solo.points[o2_solo_step], dpp + spaa)
            o2_rewards = solo.speedups[o2_solo_step] - srac
            o2_speedups_used = mtl + o2_extra_pacts * pact_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        elif ph:
            o2_hell_step = min(o1_hell_step + 1, 3)
            o2_extra_pacts = extra_pacts(hell.points[o2_hell_step], dpp)
            o2_rewards = hell.speedups[o2_hell_step]
            o2_speedups_used = mtl + o2_extra_pacts * pact_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # CALCULATIONS
        solution = max(o1, o2)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                mtl = dmt
                spaa += dpp * ps

            else:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                mtl = dmt
                spaa += (dpp + o2_extra_pacts * pact_tier.points) * ps

    # GRID 2 (None|Tr or Tr|None)
    elif (ts and not ph and not ps and not th) or (th and not ps and not ts and not ph):
        # OPTION 1 (Tr)
        o1_solo_step = find_step(solo.points, dtp * ts + spaa)
        o1_hell_step = find_step(hell.points, dtp * th)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = ttl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (Tr+)
        if ts:
            o2_solo_step = min(o1_solo_step + 1, 3)
            o2_extra_troops = extra_troops(solo.points[o2_solo_step], dtp + spaa)
            o2_rewards = solo.speedups[o2_solo_step] - srac
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        elif th:
            o2_hell_step = min(o1_hell_step + 1, 3)
            o2_extra_troops = extra_troops(hell.points[o2_hell_step], dtp)
            o2_rewards = hell.speedups[o2_hell_step]
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # CALCULATIONS
        solution = max(o1, o2)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                ttl = dtt
                spaa += dtp * ts
            else:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                ttl = dtt
                spaa += (dtp + o2_extra_troops * troop_tier.points) * ts

    # GRID 3 (None|P+Tr or P+Tr|None)
    elif (ps and ts and not ph and not th) or (ph and th and not ps and not ts):
        # OPTION 1 (Tr)
        o1_solo_step = find_step(solo.points, dtp * ts + spaa)
        o1_hell_step = find_step(hell.points, dtp * th)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = ttl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (Tr+)
        if ts:
            o2_solo_step = min(o1_solo_step + 1, 3)
            o2_extra_troops = extra_troops(solo.points[o2_solo_step], dtp + spaa)
            o2_rewards = solo.speedups[o2_solo_step] - srac
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        elif th:
            o2_hell_step = min(o1_hell_step + 1, 3)
            o2_extra_troops = extra_troops(hell.points[o2_hell_step], dtp)
            o2_rewards = hell.speedups[o2_hell_step]
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # OPTION 3 (P)
        o3_solo_step = find_step(solo.points, dpp * ps + spaa)
        o3_hell_step = find_step(hell.points, dpp * ph)
        o3_solo_rewards = solo.speedups[o3_solo_step] - srac
        o3_hell_rewards = hell.speedups[o3_hell_step]
        o3_rewards = o3_solo_rewards + o3_hell_rewards
        o3_speedups_used = mtl
        o3 = o3_rewards - o3_speedups_used

        # OPTION 4 (PTr)
        o4_solo_step = find_step(solo.points, dpp * ps + dtp * ts + spaa)
        o4_hell_step = find_step(hell.points, dpp * ph + dtp * th)
        o4_solo_rewards = solo.speedups[o4_solo_step] - srac
        o4_hell_rewards = hell.speedups[o4_hell_step]
        o4_rewards = o4_solo_rewards + o4_hell_rewards
        o4_speedups_used = mtl + ttl
        o4 = o4_rewards - o4_speedups_used

        # OPTION 5 (PTr+)
        if ts:
            o5_solo_step = min(o4_solo_step + 1, 3)
            o5_extra_troops = extra_troops(solo.points[o5_solo_step], dtp + dpp + spaa)
            o5_rewards = solo.speedups[o5_solo_step] - srac
            o5_speedups_used = mtl + ttl + o5_extra_troops * troop_tier.real_time
            o5 = o5_rewards - o5_speedups_used
        elif th:
            o5_hell_step = min(o4_hell_step + 1, 3)
            o5_extra_troops = extra_troops(hell.points[o5_hell_step], dtp + dpp)
            o5_rewards = hell.speedups[o5_hell_step]
            o5_speedups_used = mtl + ttl + o5_extra_troops * troop_tier.real_time
            o5 = o5_rewards - o5_speedups_used

        # OPTION 6 (P+)
        if ps:
            o6_solo_step = min(o3_solo_step + 1, 3)
            o6_extra_pacts = extra_pacts(solo.points[o6_solo_step], dpp + spaa)
            o6_rewards = solo.speedups[o6_solo_step] - srac
            o6_speedups_used = mtl + o6_extra_pacts * pact_tier.real_time
            o6 = o6_rewards - o6_speedups_used
        elif ph:
            o6_hell_step = min(o3_hell_step + 1, 3)
            o6_extra_pacts = extra_pacts(hell.points[o6_hell_step], dpp)
            o6_rewards = hell.speedups[o6_hell_step]
            o6_speedups_used = mtl + o6_extra_pacts * pact_tier.real_time
            o6 = o6_rewards - o6_speedups_used

        # OPTION 7 (P+Tr)
        if ps:
            o7_solo_step = min(o4_solo_step + 1, 3)
            o7_extra_pacts = extra_pacts(solo.points[o7_solo_step], dtp + dpp + spaa)
            o7_rewards = solo.speedups[o7_solo_step] - srac
            o7_speedups_used = mtl + ttl + o7_extra_pacts * pact_tier.real_time
            o7 = o7_rewards - o7_speedups_used
        elif ph:
            o7_hell_step = min(o4_hell_step + 1, 3)
            o7_extra_pacts = extra_pacts(hell.points[o7_hell_step], dtp + dpp)
            o7_rewards = hell.speedups[o7_hell_step]
            o7_speedups_used = mtl + ttl + o7_extra_pacts * pact_tier.real_time
            o7 = o7_rewards - o7_speedups_used

        # CALCULATIONS
        solution = max(o1, o2, o3, o4, o5, o6, o7)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                ttl = dtt
                spaa += dtp * ts

            elif solution == o2:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                ttl = dtt
                spaa += (dtp + o2_extra_troops * troop_tier.points) * ts

            elif solution == o3:
                TOTAL_SPEEDUPS_USED += o3_speedups_used
                TOTAL_SPEEDUPS_EARNED += o3_rewards
                mtl = dmt
                spaa += dpp * ps

            elif solution == o4:
                TOTAL_SPEEDUPS_USED += o4_speedups_used
                TOTAL_SPEEDUPS_EARNED += o4_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + dtp * ts

            elif solution == o5:
                TOTAL_SPEEDUPS_USED += o5_speedups_used
                TOTAL_SPEEDUPS_EARNED += o5_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + (dtp + o5_extra_troops * troop_tier.points) * ts

            elif solution == o6:
                TOTAL_SPEEDUPS_USED += o6_speedups_used
                TOTAL_SPEEDUPS_EARNED += o6_rewards
                mtl = dmt
                spaa += (dpp + o6_extra_pacts * pact_tier.points) * ps

            elif solution == o7:
                TOTAL_SPEEDUPS_USED += o7_speedups_used
                TOTAL_SPEEDUPS_EARNED += o7_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o7_extra_pacts * pact_tier.points) * ps + dtp * ts

    # GRID 4 (P|P)
    elif ps and ph and not ts and not th:
        # OPTION 1 (P)
        o1_solo_step = find_step(solo.points, dpp * ps + spaa)
        o1_hell_step = find_step(hell.points, dpp * ph)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = mtl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (P+)
        if o1_solo_step == 3 and o1_hell_step == 3:
            o2 = -1000000
        elif o1_solo_step == 3 or solo.points[o1_solo_step + 1] - spaa >= hell.points[o1_hell_step + 1]:
            o2_hell_step = o1_hell_step + 1
            o2_extra_pacts = extra_pacts(hell.points[o2_hell_step], dpp)
            o2_solo_rewards = o1_solo_rewards
            o2_hell_rewards = hell.speedups[o2_hell_step]
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = mtl + o2_extra_pacts * pact_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        else:
            o2_solo_step = o1_solo_step + 1
            o2_extra_pacts = extra_pacts(solo.points[o2_solo_step], dpp + spaa)
            o2_solo_rewards = solo.speedups[o2_solo_step] - srac
            o2_hell_rewards = o1_hell_rewards
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = mtl + o2_extra_pacts * pact_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # OPTION 3 (P++)
        if o1_solo_step == 3 or o1_hell_step == 3:
            o3 = -1000000
        else:
            o3_solo_step = o1_solo_step + 1
            o3_hell_step = o1_hell_step + 1
            o3_extra_pacts = extra_pacts(max(solo.points[o3_solo_step] - spaa, hell.points[o3_hell_step]), dpp)
            o3_solo_rewards = solo.speedups[o3_solo_step] - srac
            o3_hell_rewards = hell.speedups[o3_hell_step]
            o3_rewards = o3_solo_rewards + o3_hell_rewards
            o3_speedups_used = mtl + o3_extra_pacts * pact_tier.real_time
            o3 = o3_rewards - o3_speedups_used

        # CALCULATIONS
        solution = max(o1, o2, o3)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                mtl = dmt
                spaa += dpp * ps

            elif solution == o2:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                mtl = dmt
                spaa += (dpp + o2_extra_pacts) * ps

            elif solution == o3:
                TOTAL_SPEEDUPS_USED += o3_speedups_used
                TOTAL_SPEEDUPS_EARNED += o3_rewards
                mtl = dmt
                spaa += (dpp + o3_extra_pacts) * ps

    # GRID 5 (P|Tr or Tr|P)
    elif (ps and th and not ph and not ts) or (ts and ph and not ps and not th):
        # OPTION 1 (Tr)
        o1_solo_step = find_step(solo.points, dtp * ts + spaa)
        o1_hell_step = find_step(hell.points, dtp * th)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = ttl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (Tr+)
        if ts:
            o2_solo_step = min(o1_solo_step + 1, 3)
            o2_extra_troops = extra_troops(solo.points[o2_solo_step], dtp + spaa)
            o2_rewards = solo.speedups[o2_solo_step] - srac
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        elif th:
            o2_hell_step = min(o1_hell_step + 1, 3)
            o2_extra_troops = extra_troops(hell.points[o2_hell_step], dtp)
            o2_rewards = hell.speedups[o2_hell_step]
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # OPTION 3 (P)
        o3_solo_step = find_step(solo.points, dpp * ps + spaa)
        o3_hell_step = find_step(hell.points, dpp * ph)
        o3_solo_rewards = solo.speedups[o3_solo_step] - srac
        o3_hell_rewards = hell.speedups[o3_hell_step]
        o3_rewards = o3_solo_rewards + o3_hell_rewards
        o3_speedups_used = mtl
        o3 = o3_rewards - o3_speedups_used

        # OPTION 4 (PTr)
        o4_solo_step = find_step(solo.points, dpp * ps + dtp * ts + spaa)
        o4_hell_step = find_step(hell.points, dpp * ph + dtp * th)
        o4_solo_rewards = solo.speedups[o4_solo_step] - srac
        o4_hell_rewards = hell.speedups[o4_hell_step]
        o4_rewards = o4_solo_rewards + o4_hell_rewards
        o4_speedups_used = mtl + ttl
        o4 = o4_rewards - o4_speedups_used

        # OPTION 5 (PTr+)
        if ts:
            o5_solo_step = min(o4_solo_step + 1, 3)
            o5_extra_troops = extra_troops(solo.points[o5_solo_step], dtp + spaa)
            o5_solo_rewards = solo.speedups[o5_solo_step] - srac
            o5_hell_rewards = o4_hell_rewards
            o5_rewards = o5_solo_rewards + o5_hell_rewards
            o5_speedups_used = ttl + o5_extra_troops * troop_tier.real_time
            o5 = o5_rewards - o5_speedups_used
        elif th:
            o5_hell_step = min(o4_hell_step + 1, 3)
            o5_extra_troops = extra_troops(hell.points[o5_hell_step], dtp)
            o5_solo_rewards = o4_solo_rewards
            o5_hell_rewards = hell.speedups[o5_hell_step]
            o5_rewards = o5_solo_rewards + o5_hell_rewards
            o5_speedups_used = ttl + o5_extra_troops * troop_tier.real_time
            o5 = o5_rewards - o5_speedups_used

        # OPTION 6 (P+)
        if ps:
            o6_solo_step = min(o3_solo_step + 1, 3)
            o6_extra_pacts = extra_pacts(solo.points[o6_solo_step], dpp + spaa)
            o6_rewards = solo.speedups[o6_solo_step] - srac
            o6_speedups_used = mtl + o6_extra_pacts * pact_tier.real_time
            o6 = o6_rewards - o6_speedups_used
        elif ph:
            o6_hell_step = min(o3_hell_step + 1, 3)
            o6_extra_pacts = extra_pacts(hell.points[o6_hell_step], dpp)
            o6_rewards = hell.speedups[o6_hell_step]
            o6_speedups_used = mtl + o6_extra_pacts * pact_tier.real_time
            o6 = o6_rewards - o6_speedups_used

        # OPTION 7 (P+Tr)
        if ps:
            o7_solo_step = min(o4_solo_step + 1, 3)
            o7_extra_pacts = extra_pacts(solo.points[o7_solo_step], dpp + spaa)
            o7_solo_rewards = solo.speedups[o7_solo_step] - srac
            o7_hell_rewards = o4_hell_rewards
            o7_rewards = o7_solo_rewards + o7_hell_rewards
            o7_speedups_used = mtl + o7_extra_pacts * pact_tier.real_time
            o7 = o7_rewards - o7_speedups_used
        elif ph:
            o7_hell_step = min(o4_hell_step + 1, 3)
            o7_extra_pacts = extra_pacts(hell.points[o7_hell_step], dpp)
            o7_solo_rewards = o4_solo_rewards
            o7_hell_rewards = hell.speedups[o7_hell_step]
            o7_rewards = o7_solo_rewards + o7_hell_rewards
            o7_speedups_used = mtl + o7_extra_pacts * pact_tier.real_time
            o7 = o7_rewards - o7_speedups_used

        # OPTION 8 (P+Tr+)
        o8_solo_step = min(o4_solo_step + 1, 3)
        o8_hell_step = min(o4_hell_step + 1, 3)
        o8_extra_pacts = o7_extra_pacts
        o8_extra_troops = o5_extra_troops
        o8_solo_rewards = solo.speedups[o8_solo_step] - srac
        o8_hell_rewards = hell.speedups[o8_hell_step]
        o8_rewards = o8_solo_rewards + o8_hell_rewards
        o8_speedups_used = mtl + ttl + o8_extra_troops * troop_tier.real_time + o8_extra_pacts * pact_tier.real_time
        o8 = o8_rewards - o8_speedups_used

        # CALCULATIONS
        solution = max(o1, o2, o3, o4, o5, o6, o7, o8)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                ttl = dtt
                spaa += dtp * ts

            elif solution == o2:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                ttl = dtt
                spaa += (dtp + o2_extra_troops) * ts

            elif solution == o3:
                TOTAL_SPEEDUPS_USED += o3_speedups_used
                TOTAL_SPEEDUPS_EARNED += o3_rewards
                mtl = dmt
                spaa += dpp * ps

            elif solution == o4:
                TOTAL_SPEEDUPS_USED += o4_speedups_used
                TOTAL_SPEEDUPS_EARNED += o4_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + dtp * ts

            elif solution == o5:
                TOTAL_SPEEDUPS_USED += o5_speedups_used
                TOTAL_SPEEDUPS_EARNED += o5_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + (dtp + o5_extra_troops) * ts

            elif solution == o6:
                TOTAL_SPEEDUPS_USED += o6_speedups_used
                TOTAL_SPEEDUPS_EARNED += o6_rewards
                mtl = dmt
                spaa += (dpp + o6_extra_pacts) * ps

            elif solution == o7:
                TOTAL_SPEEDUPS_USED += o7_speedups_used
                TOTAL_SPEEDUPS_EARNED += o7_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o7_extra_pacts) * ps + dtp * ts

            elif solution == o8:
                TOTAL_SPEEDUPS_USED += o8_speedups_used
                TOTAL_SPEEDUPS_EARNED += o8_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o8_extra_pacts) * ps + (dtp + o8_extra_troops) * ts

    # GRID 6 (P|P+Tr or P+Tr|P)
    elif (ps and ph and th and not ts) or (ps and ts and ph and not th):
        # OPTION 1 (Tr)
        o1_solo_step = find_step(solo.points, dtp * ts + spaa)
        o1_hell_step = find_step(hell.points, dtp * th)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = ttl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (Tr+)
        if ts:
            o2_solo_step = min(o1_solo_step + 1, 3)
            o2_extra_troops = extra_troops(solo.points[o2_solo_step], dtp + spaa)
            o2_rewards = solo.speedups[o2_solo_step] - srac
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        elif th:
            o2_hell_step = min(o1_hell_step + 1, 3)
            o2_extra_troops = extra_troops(hell.points[o2_hell_step], dtp)
            o2_rewards = hell.speedups[o2_hell_step]
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # OPTION 3 (P)
        o3_solo_step = find_step(solo.points, dpp + spaa)
        o3_hell_step = find_step(hell.points, dpp)
        o3_solo_rewards = solo.speedups[o3_solo_step] - srac
        o3_hell_rewards = hell.speedups[o3_hell_step]
        o3_rewards = o3_solo_rewards + o3_hell_rewards
        o3_speedups_used = mtl
        o3 = o3_rewards - o3_speedups_used

        # OPTION 4 (PTr)
        o4_solo_step = find_step(solo.points, dpp * ps + dtp * ts + spaa)
        o4_hell_step = find_step(hell.points, dpp * ph + dtp * th)
        o4_solo_rewards = solo.speedups[o4_solo_step] - srac
        o4_hell_rewards = hell.speedups[o4_hell_step]
        o4_rewards = o4_solo_rewards + o4_hell_rewards
        o4_speedups_used = ttl + mtl
        o4 = o4_rewards - o4_speedups_used

        # OPTION 5 (PTr+)
        if ts:
            o5_solo_step = min(o4_solo_step + 1, 3)
            o5_extra_troops = extra_troops(solo.points[o5_solo_step], dtp + dpp + spaa)
            o5_solo_rewards = solo.speedups[o5_solo_step] - srac
            o5_hell_rewards = o4_hell_rewards
            o5_rewards = o5_solo_rewards + o5_hell_rewards
            o5_speedups_used = mtl + ttl + o5_extra_troops * troop_tier.real_time
            o5 = o5_rewards - o5_speedups_used
        elif th:
            o5_hell_step = min(o4_hell_step + 1, 3)
            o5_extra_troops = extra_troops(hell.points[o5_hell_step], dtp + dpp)
            o5_solo_rewards = o4_solo_rewards
            o5_hell_rewards = hell.speedups[o5_hell_step]
            o5_rewards = o5_solo_rewards + o5_hell_rewards
            o5_speedups_used = mtl + ttl + o5_extra_troops * troop_tier.real_time
            o5 = o5_rewards - o5_speedups_used

        # OPTION 6 (P+)
        if o3_solo_step == 3 and o3_hell_step == 3:
            o6 = -1000000
        elif o3_solo_step == 3 or solo.points[o3_solo_step + 1] - spaa >= hell.points[o3_hell_step + 1]:
            o6_hell_step = o3_hell_step + 1
            o6_extra_pacts = extra_pacts(hell.points[o6_hell_step], dpp)
            o6_solo_rewards = o3_solo_rewards
            o6_hell_rewards = hell.speedups[o6_hell_step]
            o6_rewards = o6_solo_rewards + o6_hell_rewards
            o6_speedups_used = mtl + o6_extra_pacts * pact_tier.real_time
            o6 = o6_rewards - o6_speedups_used
        else:
            o6_solo_step = o3_solo_step + 1
            o6_extra_pacts = extra_pacts(solo.points[o6_solo_step], dpp + spaa)
            o6_solo_rewards = solo.speedups[o6_solo_step] - srac
            o6_hell_rewards = o3_hell_rewards
            o6_rewards = o6_solo_rewards + o6_hell_rewards
            o6_speedups_used = mtl + o6_extra_pacts * pact_tier.real_time
            o6 = o6_rewards - o6_speedups_used

        # OPTION 7 (P+Tr)
        if o4_solo_step == 3 and o4_hell_step == 3:
            o7 = -1000000
        elif o4_solo_step == 3 or solo.points[o4_solo_step + 1] - dtp * ts - spaa >= hell.points[o4_hell_step + 1] - dtp * th:
            o7_hell_step = o4_hell_step + 1
            o7_extra_pacts = extra_pacts(hell.points[o7_hell_step], dpp + dtp * th)
            o7_solo_rewards = o4_solo_rewards
            o7_hell_rewards = hell.speedups[o7_hell_step]
            o7_rewards = o7_solo_rewards + o7_hell_rewards
            o7_speedups_used = mtl + o7_extra_pacts * pact_tier.real_time
            o7 = o7_rewards - o7_speedups_used
        else:
            o7_solo_step = o4_solo_step + 1
            o7_extra_pacts = extra_pacts(solo.points[o7_solo_step], dpp + dtp * ts + spaa)
            o7_solo_rewards = solo.speedups[o7_solo_step] - srac
            o7_hell_rewards = o4_hell_rewards
            o7_rewards = o7_solo_rewards + o7_hell_rewards
            o7_speedups_used = mtl + o7_extra_pacts * pact_tier.real_time
            o7 = o7_rewards - o7_speedups_used

        # OPTION 8 (P+Tr+)
        if o4_solo_step == 3 or o4_hell_step == 3:
            o8 = -1000000
        elif ts:
            o8_hell_step = o4_hell_step + 1
            o8_extra_troops = o5_extra_troops
            o8_extra_pacts = extra_pacts(hell.points[o8_hell_step], dpp)
            o8_solo_rewards = o5_solo_rewards
            o8_hell_rewards = hell.speedups[o8_hell_step]
            o8_rewards = o8_solo_rewards + o8_hell_rewards
            o8_speedups_used = mtl + ttl + o8_extra_troops * troop_tier.real_time + o8_extra_pacts * pact_tier.real_time
            o8 = o8_rewards - o8_speedups_used
        elif th:
            o8_solo_step = o4_solo_step + 1
            o8_extra_troops = o5_extra_troops
            o8_extra_pacts = extra_pacts(solo.points[o8_solo_step], dpp + spaa)
            o8_solo_rewards = solo.speedups[o8_solo_step] - srac
            o8_hell_rewards = o5_hell_rewards
            o8_rewards = o8_solo_rewards + o8_hell_rewards
            o8_speedups_used = mtl + ttl + o8_extra_troops * troop_tier.real_time + o8_extra_pacts * pact_tier.real_time
            o8 = o8_rewards - o8_speedups_used

        # OPTION 9 (P++)
        if o3_solo_step == 3 or o3_hell_step == 3:
            o9 = -1000000
        else:
            o9_solo_step = o3_solo_step + 1
            o9_hell_step = o3_hell_step + 1
            o9_extra_pacts = extra_pacts(max(solo.points[o9_solo_step] - spaa, hell.points[o9_hell_step]), dpp)
            o9_solo_rewards = solo.speedups[o9_solo_step] - srac
            o9_hell_rewards = hell.speedups[o9_hell_step]
            o9_rewards = o9_solo_rewards + o9_hell_rewards
            o9_speedups_used = mtl + o9_extra_pacts * pact_tier.real_time
            o9 = o9_rewards - o9_speedups_used

        # OPTION 10 (P++Tr)
        if o4_solo_step == 3 or o4_hell_step == 3:
            o10 = -1000000
        else:
            o10_solo_step = o4_solo_step + 1
            o10_hell_step = o4_hell_step + 1
            o10_extra_pacts = extra_pacts(max(solo.points[o10_solo_step] - spaa - dtp * ts, hell.points[o10_hell_step] - dtp * th), dpp)
            o10_solo_rewards = solo.speedups[o10_solo_step] - srac
            o10_hell_rewards = hell.speedups[o10_hell_step]
            o10_rewards = o10_solo_rewards + o10_hell_rewards
            o10_speedups_used = mtl + o10_extra_pacts * pact_tier.real_time
            o10 = o10_rewards - o10_speedups_used

        # CALCULATIONS
        solution = max(o1, o2, o3, o4, o5, o6, o7, o8, o9, o10)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                ttl = dtt
                spaa += dtp * ts

            elif solution == o2:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                ttl = dtt
                spaa += (dtp + o2_extra_troops) * ts

            elif solution == o3:
                TOTAL_SPEEDUPS_USED += o3_speedups_used
                TOTAL_SPEEDUPS_EARNED += o3_rewards
                mtl = dmt
                spaa += dpp * ps

            elif solution == o4:
                TOTAL_SPEEDUPS_USED += o4_speedups_used
                TOTAL_SPEEDUPS_EARNED += o4_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + dtp * ts

            elif solution == o5:
                TOTAL_SPEEDUPS_USED += o5_speedups_used
                TOTAL_SPEEDUPS_EARNED += o5_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ts + (dtp + o5_extra_troops) * ts

            elif solution == o6:
                TOTAL_SPEEDUPS_USED += o6_speedups_used
                TOTAL_SPEEDUPS_EARNED += o6_rewards
                mtl = dmt
                spaa += (dpp + o6_extra_pacts) * ps

            elif solution == o7:
                TOTAL_SPEEDUPS_USED += o7_speedups_used
                TOTAL_SPEEDUPS_EARNED += o7_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o7_extra_pacts) * ps + dtp * ts

            elif solution == o8:
                TOTAL_SPEEDUPS_USED += o8_speedups_used
                TOTAL_SPEEDUPS_EARNED += o8_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o8_extra_pacts) * ps + (dtp + o8_extra_troops) * ts

            elif solution == o9:
                TOTAL_SPEEDUPS_USED += o9_speedups_used
                TOTAL_SPEEDUPS_EARNED += o9_rewards
                mtl = dmt
                spaa += (dpp + o9_extra_pacts) * ps

            elif solution == o10:
                TOTAL_SPEEDUPS_USED += o10_speedups_used
                TOTAL_SPEEDUPS_EARNED += o10_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o10_extra_pacts) * ps + dtp * ts

    # GRID 7 (Tr|Tr)
    elif ts and th and not ps and not ph:
        # OPTION 1 (Tr)
        o1_solo_step = find_step(solo.points, dtp + spaa)
        o1_hell_step = find_step(hell.points, dtp)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = ttl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (Tr+)
        if o1_solo_step == 3 and o1_hell_step == 3:
            o2 = -1000000
        elif o1_solo_step == 3 or solo.points[o1_solo_step + 1] - spaa >= hell.points[o1_hell_step + 1]:
            o2_hell_step = o1_hell_step + 1
            o2_extra_troops = extra_troops(hell.points[o2_hell_step], dtp)
            o2_solo_rewards = o1_solo_rewards
            o2_hell_rewards = hell.speedups[o2_hell_step]
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        else:
            o2_solo_step = o1_solo_step + 1
            o2_extra_troops = extra_troops(solo.points[o2_solo_step], dtp + spaa)
            o2_solo_rewards = solo.speedups[o2_solo_step] - srac
            o2_hell_rewards = o1_hell_rewards
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # OPTION 3 (Tr++)
        if o1_solo_step == 3 or o1_hell_step == 3:
            o3 = -1000000
        else:
            o3_solo_step = o1_solo_step + 1
            o3_hell_step = o1_hell_step + 1
            o3_extra_troops = extra_troops(max(solo.points[o3_solo_step] - spaa, hell.points[o3_hell_step]), dtp)
            o3_solo_rewards = solo.speedups[o3_solo_step] - srac
            o3_hell_rewards = hell.speedups[o3_hell_step]
            o3_rewards = o3_solo_rewards + o3_hell_rewards
            o3_speedups_used = ttl + o3_extra_troops * troop_tier.real_time
            o3 = o3_rewards - o3_speedups_used

        # CALCULATIONS
        solution = max(o1, o2, o3)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                ttl = dtt
                spaa += dtp * ts

            elif solution == o2:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                ttl = dtt
                spaa += (dtp + o2_extra_troops) * ts

            elif solution == o3:
                TOTAL_SPEEDUPS_USED += o3_speedups_used
                TOTAL_SPEEDUPS_EARNED += o3_rewards
                ttl = dtt
                spaa += (dtp + o3_extra_troops) * ts

    # GRID 8 (Tr|P+Tr or P+Tr|Tr)
    elif (ts and ph and th and not ps) or (ps and ts and th and not ph):
        # OPTION 1 (Tr)
        o1_solo_step = find_step(solo.points, dtp + spaa)
        o1_hell_step = find_step(hell.points, dtp)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = ttl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (Tr+)
        if o1_solo_step == 3 and o1_hell_step == 3:
            o2 = -1000000
        elif o1_solo_step == 3 or solo.points[o1_solo_step + 1] - spaa >= hell.points[o1_hell_step + 1]:
            o2_hell_step = o1_hell_step + 1
            o2_extra_troops = extra_troops(hell.points[o2_hell_step], dtp)
            o2_solo_rewards = o1_solo_rewards
            o2_hell_rewards = hell.speedups[o2_hell_step]
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        else:
            o2_solo_step = o1_solo_step + 1
            o2_extra_troops = extra_troops(solo.points[o2_solo_step], dtp + spaa)
            o2_solo_rewards = solo.speedups[o2_solo_step] - srac
            o2_hell_rewards = o1_hell_rewards
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # OPTION 3 (Tr++)
        if o1_solo_step == 3 or o1_hell_step == 3:
            o3 = -1000000
        else:
            o3_solo_step = o1_solo_step + 1
            o3_hell_step = o1_hell_step + 1
            o3_extra_troops = extra_troops(max(solo.points[o3_solo_step] - spaa, hell.points[o3_hell_step]), dtp)
            o3_solo_rewards = solo.speedups[o3_solo_step] - srac
            o3_hell_rewards = hell.speedups[o3_hell_step]
            o3_rewards = o3_solo_rewards + o3_hell_rewards
            o3_speedups_used = ttl + o3_extra_troops * troop_tier.real_time
            o3 = o3_rewards - o3_speedups_used

        # OPTION 4 (P)
        o4_solo_step = find_step(solo.points, dpp * ps + spaa)
        o4_hell_step = find_step(hell.points, dpp * ph)
        o4_solo_rewards = solo.speedups[o4_solo_step] - srac
        o4_hell_rewards = hell.speedups[o4_hell_step]
        o4_rewards = o4_solo_rewards + o4_hell_rewards
        o4_speedups_used = mtl
        o4 = o4_rewards - o4_speedups_used

        # OPTION 5 (PTr)
        o5_solo_step = find_step(solo.points, dtp + dpp * ps + spaa)
        o5_hell_step = find_step(hell.points, dtp + dpp * ph)
        o5_solo_rewards = solo.speedups[o5_solo_step] - srac
        o5_hell_rewards = hell.speedups[o5_hell_step]
        o5_rewards = o5_solo_rewards + o5_hell_rewards
        o5_speedups_used = mtl
        o5 = o5_rewards - o5_speedups_used

        # OPTION 6 (PTr+)
        if o5_solo_step == 3 and o5_hell_step == 3:
            o6 = -1000000
        elif o5_solo_step == 3 or solo.points[o5_solo_step + 1] - dpp * ps - spaa >= hell.points[o5_hell_step + 1] - dpp * ph:
            o6_hell_step = o5_hell_step + 1
            o6_extra_troops = extra_troops(hell.points[o6_hell_step], dtp + dpp * ph)
            o6_solo_rewards = o5_solo_rewards
            o6_hell_rewards = hell.speedups[o6_hell_step]
            o6_rewards = o6_solo_rewards + o6_hell_rewards
            o6_speedups_used = mtl + ttl + o6_extra_troops * troop_tier.real_time
            o6 = o6_rewards - o6_speedups_used
        else:
            o6_solo_step = o5_solo_step + 1
            o6_extra_troops = extra_troops(solo.points[o6_solo_step], dtp + dpp * ps + spaa)
            o6_solo_rewards = solo.speedups[o6_solo_step] - srac
            o6_hell_rewards = o5_hell_rewards
            o6_rewards = o6_solo_rewards + o6_hell_rewards
            o6_speedups_used = ttl + mtl + o6_extra_troops * troop_tier.real_time
            o6 = o6_rewards - o6_speedups_used

        # OPTION 7 (PTr++)
        if o5_solo_step == 3 or o5_hell_step == 3:
            o7 = -1000000
        else:
            o7_solo_step = o5_solo_step + 1
            o7_hell_step = o5_hell_step + 1
            o7_extra_troops = extra_troops(max(solo.points[o7_solo_step] - spaa - dpp * ps, hell.points[o7_hell_step] - dpp * ph), dtp)
            o7_solo_rewards = solo.speedups[o7_solo_step] - srac
            o7_hell_rewards = hell.speedups[o7_hell_step]
            o7_rewards = o7_solo_rewards + o7_hell_rewards
            o7_speedups_used = mtl + ttl + o7_extra_troops * troop_tier.real_time
            o7 = o7_rewards - o7_speedups_used

        # OPTION 8 (P+)
        if ps:
            o8_solo_step = min(o4_solo_step + 1, 3)
            o8_extra_pacts = extra_pacts(solo.points[o8_solo_step], dpp + spaa)
            o8_rewards = solo.speedups[o8_solo_step] - srac
            o8_speedups_used = mtl + o8_extra_pacts * pact_tier.real_time
            o8 = o8_rewards - o8_speedups_used
        elif ph:
            o8_hell_step = min(o4_hell_step + 1, 3)
            o8_extra_pacts = extra_pacts(hell.points[o8_hell_step], dpp)
            o8_rewards = hell.speedups[o8_hell_step]
            o8_speedups_used = mtl + o8_extra_pacts * pact_tier.real_time
            o8 = o8_rewards - o8_speedups_used

        # OPTION 9 (P+Tr)
        if ps:
            o9_solo_step = min(o5_solo_step + 1, 3)
            o9_extra_pacts = extra_pacts(solo.points[o9_solo_step], dpp + dtp + spaa)
            o9_solo_rewards = solo.speedups[o9_solo_step] - srac
            o9_hell_rewards = o5_hell_rewards
            o9_rewards = o9_solo_rewards + o9_hell_rewards
            o9_speedups_used = mtl + ttl + o9_extra_pacts * pact_tier.real_time
            o9 = o9_rewards - o9_speedups_used
        elif ph:
            o9_hell_step = min(o5_hell_step + 1, 3)
            o9_extra_pacts = extra_pacts(hell.points[o9_hell_step], dpp + dtp)
            o9_solo_rewards = o5_solo_rewards
            o9_hell_rewards = hell.speedups[o9_hell_step]
            o9_rewards = o9_solo_rewards + o9_hell_rewards
            o9_speedups_used = mtl + ttl + o9_extra_pacts * pact_tier.real_time
            o9 = o9_rewards - o9_speedups_used

        # OPTION 10 (P+Tr+)
        if o5_solo_step == 3 or o5_hell_step == 3:
            o10 = -1000000
        elif ps:
            o10_hell_step = o5_hell_step + 1
            o10_extra_troops = extra_troops(hell.points[o10_hell_step], dtp)
            o10_extra_pacts = o9_extra_pacts
            o10_solo_rewards = o9_solo_rewards
            o10_hell_rewards = hell.speedups[o10_hell_step]
            o10_rewards = o10_solo_rewards + o10_hell_rewards
            o10_speedups_used = ttl + mtl + o10_extra_troops * troop_tier.real_time + o10_extra_pacts * pact_tier.real_time
            o10 = o10_rewards - o10_speedups_used
        elif ph:
            o10_solo_step = o5_hell_step + 1
            o10_extra_troops = extra_troops(solo.points[o10_solo_step], dtp + spaa)
            o10_extra_pacts = o9_extra_pacts
            o10_solo_rewards = solo.speedups[o10_solo_step] - srac
            o10_hell_rewards = o9_hell_rewards
            o10_rewards = o10_solo_rewards + o10_hell_rewards
            o10_speedups_used = ttl + mtl + o10_extra_troops * troop_tier.real_time + o10_extra_pacts * pact_tier.real_time
            o10 = o10_rewards - o10_speedups_used

        # CALCULATIONS
        solution = max(o1, o2, o3, o4, o5, o6, o7, o8, o9, o10)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                ttl = dtt
                spaa += dtp * ts

            elif solution == o2:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                ttl = dtt
                spaa += (dtp + o2_extra_troops) * ts

            elif solution == o3:
                TOTAL_SPEEDUPS_USED += o3_speedups_used
                TOTAL_SPEEDUPS_EARNED += o3_rewards
                ttl = dtt
                spaa += (dtp + o3_extra_troops) * ts

            elif solution == o4:
                TOTAL_SPEEDUPS_USED += o4_speedups_used
                TOTAL_SPEEDUPS_EARNED += o4_rewards
                mtl = dmt
                spaa += dpp * ps

            elif solution == o5:
                TOTAL_SPEEDUPS_USED += o5_speedups_used
                TOTAL_SPEEDUPS_EARNED += o5_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + dtp * ts

            elif solution == o6:
                TOTAL_SPEEDUPS_USED += o6_speedups_used
                TOTAL_SPEEDUPS_EARNED += o6_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + (dtp + o6_extra_troops) * ts

            elif solution == o7:
                TOTAL_SPEEDUPS_USED += o7_speedups_used
                TOTAL_SPEEDUPS_EARNED += o7_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + (dtp + o7_extra_troops) * ts

            elif solution == o8:
                TOTAL_SPEEDUPS_USED += o8_speedups_used
                TOTAL_SPEEDUPS_EARNED += o8_rewards
                mtl = dmt
                spaa += (dpp + o8_extra_pacts) * ps

            elif solution == o9:
                TOTAL_SPEEDUPS_USED += o9_speedups_used
                TOTAL_SPEEDUPS_EARNED += o9_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o9_extra_pacts) * ps + dtp * ts

            elif solution == o10:
                TOTAL_SPEEDUPS_USED += o10_speedups_used
                TOTAL_SPEEDUPS_EARNED += o10_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o10_extra_pacts) * ps + (dtp + o10_extra_troops) * ts

    # GRID 9 (P+Tr|P+Tr)
    elif ps and ts and ph and th:
        # OPTION 1 (Tr)
        o1_solo_step = find_step(solo.points, dtp + spaa)
        o1_hell_step = find_step(hell.points, dtp)
        o1_solo_rewards = solo.speedups[o1_solo_step] - srac
        o1_hell_rewards = hell.speedups[o1_hell_step]
        o1_rewards = o1_solo_rewards + o1_hell_rewards
        o1_speedups_used = ttl
        o1 = o1_rewards - o1_speedups_used

        # OPTION 2 (Tr+)
        if o1_solo_step == 3 and o1_hell_step == 3:
            o2 = -1000000
        elif o1_solo_step == 3 or solo.points[o1_solo_step + 1] - spaa >= hell.points[o1_hell_step + 1]:
            o2_hell_step = o1_hell_step + 1
            o2_extra_troops = extra_troops(hell.points[o2_hell_step], dtp)
            o2_solo_rewards = o1_solo_rewards
            o2_hell_rewards = hell.speedups[o2_hell_step]
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used
        else:
            o2_solo_step = o1_solo_step + 1
            o2_extra_troops = extra_troops(solo.points[o2_solo_step], dtp + spaa)
            o2_solo_rewards = solo.speedups[o2_solo_step] - srac
            o2_hell_rewards = o1_hell_rewards
            o2_rewards = o2_solo_rewards + o2_hell_rewards
            o2_speedups_used = ttl + o2_extra_troops * troop_tier.real_time
            o2 = o2_rewards - o2_speedups_used

        # OPTION 3 (Tr++)
        if o1_solo_step == 3 or o1_hell_step == 3:
            o3 = -1000000
        else:
            o3_solo_step = o1_solo_step + 1
            o3_hell_step = o1_hell_step + 1
            o3_extra_troops = extra_troops(max(solo.points[o3_solo_step] - spaa, hell.points[o3_hell_step]), dtp)
            o3_solo_rewards = solo.speedups[o3_solo_step] - srac
            o3_hell_rewards = hell.speedups[o3_hell_step]
            o3_rewards = o3_solo_rewards + o3_hell_rewards
            o3_speedups_used = ttl + o3_extra_troops * troop_tier.real_time
            o3 = o3_rewards - o3_speedups_used

        # OPTION 4 (P)
        o4_solo_step = find_step(solo.points, dpp + spaa)
        o4_hell_step = find_step(hell.points, dpp)
        o4_solo_rewards = solo.speedups[o4_solo_step] - srac
        o4_hell_rewards = hell.speedups[o4_hell_step]
        o4_rewards = o4_solo_rewards + o4_hell_rewards
        o4_speedups_used = mtl
        o4 = o4_rewards - o4_speedups_used

        # OPTION 5 (PTr)
        o5_solo_step = find_step(solo.points, dtp + dpp + spaa)
        o5_hell_step = find_step(hell.points, dtp + dpp)
        o5_solo_rewards = solo.speedups[o5_solo_step] - srac
        o5_hell_rewards = hell.speedups[o5_hell_step]
        o5_rewards = o5_solo_rewards + o5_hell_rewards
        o5_speedups_used = mtl + ttl
        o5 = o5_rewards - o5_speedups_used

        # OPTION 6 (PTr+)
        if o5_solo_step == 3 and o5_hell_step == 3:
            o6 = -1000000
        elif o5_solo_step == 3 or solo.points[o5_solo_step + 1] - dpp * ps - spaa >= hell.points[o5_hell_step + 1] - dpp * ph:
            o6_hell_step = o5_hell_step + 1
            o6_extra_troops = extra_troops(hell.points[o6_hell_step], dtp + dpp)
            o6_solo_rewards = o5_solo_rewards
            o6_hell_rewards = hell.speedups[o6_hell_step]
            o6_rewards = o6_solo_rewards + o6_hell_rewards
            o6_speedups_used = ttl + mtl + o6_extra_troops * troop_tier.real_time
            o6 = o6_rewards - o6_speedups_used
        else:
            o6_solo_step = o5_solo_step + 1
            o6_extra_troops = extra_troops(solo.points[o6_solo_step], dtp + dpp + spaa)
            o6_solo_rewards = solo.speedups[o6_solo_step] - srac
            o6_hell_rewards = o5_hell_rewards
            o6_rewards = o6_solo_rewards + o6_hell_rewards
            o6_speedups_used = ttl + mtl + o6_extra_troops * troop_tier.real_time
            o6 = o6_rewards - o6_speedups_used

        # OPTION 7 (PTr++)
        if o5_solo_step == 3 or o5_hell_step == 3:
            o7 = -1000000
        else:
            o7_solo_step = o5_solo_step + 1
            o7_hell_step = o5_hell_step + 1
            o7_extra_troops = extra_troops(max(solo.points[o7_solo_step], hell.points[o7_hell_step]), dtp + dpp)
            o7_solo_rewards = solo.speedups[o7_solo_step] - srac
            o7_hell_rewards = hell.speedups[o7_hell_step]
            o7_rewards = o7_solo_rewards + o7_hell_rewards
            o7_speedups_used = mtl + ttl + o7_extra_troops * troop_tier.real_time
            o7 = o7_rewards - o7_speedups_used

        # OPTION 8 (P+)
        if o4_solo_step == 3 and o4_hell_step == 3:
            o8 = -1000000
        elif o4_solo_step == 3 or solo.points[o4_solo_step + 1] - spaa >= hell.points[o4_hell_step + 1]:
            o8_hell_step = o4_hell_step + 1
            o8_extra_pacts = extra_pacts(hell.points[o8_hell_step], dpp)
            o8_solo_rewards = o4_solo_rewards
            o8_hell_rewards = hell.points[o8_hell_step]
            o8_rewards = o8_solo_rewards + o8_hell_rewards
            o8_speedups_used = mtl + o8_extra_pacts * pact_tier.real_time
            o8 = o8_rewards - o8_speedups_used
        else:
            o8_solo_step = o4_solo_step + 1
            o8_extra_pacts = extra_pacts(solo.points[o8_solo_step], dpp + spaa)
            o8_solo_rewards = solo.speedups[o8_solo_step] - srac
            o8_hell_rewards = o4_hell_rewards
            o8_rewards = o8_solo_rewards + o8_hell_rewards
            o8_speedups_used = mtl + o8_extra_pacts * pact_tier.real_time
            o8 = o8_rewards - o8_speedups_used

        # OPTION 9 (P+Tr)
        if o5_solo_step == 3 and o5_hell_step == 3:
            o9 = -1000000
        elif o5_solo_step == 3 or solo.points[o5_solo_step + 1] - spaa >= hell.points[o5_hell_step + 1]:
            o9_hell_step = o5_hell_step + 1
            o9_extra_pacts = extra_pacts(hell.points[o9_hell_step], dpp)
            o9_solo_rewards = o5_solo_rewards
            o9_hell_rewards = hell.speedups[o9_hell_step]
            o9_rewards = o9_solo_rewards + o9_hell_rewards
            o9_speedups_used = mtl + o9_extra_pacts * pact_tier.real_time
            o9 = o9_rewards - o9_speedups_used
        else:
            o9_solo_step = o5_solo_step + 1
            o9_extra_pacts = extra_pacts(solo.points[o9_solo_step], dpp + spaa)
            o9_solo_rewards = solo.speedups[o9_solo_step] - srac
            o9_hell_rewards = o5_hell_rewards
            o9_rewards = o9_solo_rewards + o9_hell_rewards
            o9_speedups_used = mtl + o9_extra_pacts * pact_tier.real_time
            o9 = o9_rewards - o9_speedups_used

        # OPTION 10 (P++)
        if o4_solo_step == 3 or o4_hell_step == 3:
            o10 = -1000000
        else:
            o10_solo_step = o4_solo_step + 1
            o10_hell_step = o4_hell_step + 1
            o10_extra_pacts = extra_pacts(max(solo.points[o10_solo_step] - spaa, hell.points[o10_hell_step]), dpp)
            o10_solo_rewards = solo.speedups[o10_solo_step] - srac
            o10_hell_rewards = hell.speedups[o10_hell_step]
            o10_rewards = o10_solo_rewards + o10_hell_rewards
            o10_speedups_used = mtl + o10_extra_pacts * pact_tier.real_time
            o10 = o10_rewards - o10_speedups_used

        # OPTION 11 (P++Tr)
        if o5_solo_step == 3 or o5_hell_step == 3:
            o11 = -1000000
        else:
            o11_solo_step = o5_solo_step + 1
            o11_hell_step = o5_hell_step + 1
            o11_extra_pacts = extra_pacts(max(solo.points[o11_solo_step] - spaa, hell.points[o11_hell_step]), dpp + dtp)
            o11_solo_rewards = solo.speedups[o11_solo_step] - srac
            o11_hell_rewards = hell.speedups[o11_hell_step]
            o11_rewards = o11_solo_rewards + o11_hell_rewards
            o11_speedups_used = mtl + ttl + o11_extra_pacts * pact_tier.real_time
            o11 = o11_rewards - o11_speedups_used

        # CALCULATIONS
        solution = max(o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11)
        if solution >= 0:
            TOTAL_TIMES_SPED_UP += 1
            if solution == o1:
                TOTAL_SPEEDUPS_USED += o1_speedups_used
                TOTAL_SPEEDUPS_EARNED += o1_rewards
                ttl = dtt
                spaa += dtp * ts

            elif solution == o2:
                TOTAL_SPEEDUPS_USED += o2_speedups_used
                TOTAL_SPEEDUPS_EARNED += o2_rewards
                ttl = dtt
                spaa += (dtp + o2_extra_troops) * ts

            elif solution == o3:
                TOTAL_SPEEDUPS_USED += o3_speedups_used
                TOTAL_SPEEDUPS_EARNED += o3_rewards
                ttl = dtt
                spaa += (dtp + o3_extra_troops) * ts

            elif solution == o4:
                TOTAL_SPEEDUPS_USED += o4_speedups_used
                TOTAL_SPEEDUPS_EARNED += o4_rewards
                mtl = dmt
                spaa += dpp * ps

            elif solution == o5:
                TOTAL_SPEEDUPS_USED += o5_speedups_used
                TOTAL_SPEEDUPS_EARNED += o5_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + dtp * ts

            elif solution == o6:
                TOTAL_SPEEDUPS_USED += o6_speedups_used
                TOTAL_SPEEDUPS_EARNED += o6_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + (dtp + o6_extra_troops) * ts

            elif solution == o7:
                TOTAL_SPEEDUPS_USED += o7_speedups_used
                TOTAL_SPEEDUPS_EARNED += o7_rewards
                ttl = dtt
                mtl = dmt
                spaa += dpp * ps + (dtp + o7_extra_troops) * ts

            elif solution == o8:
                TOTAL_SPEEDUPS_USED += o8_speedups_used
                TOTAL_SPEEDUPS_EARNED += o8_rewards
                mtl = dmt
                spaa += (dpp + o8_extra_pacts) * ps

            elif solution == o9:
                TOTAL_SPEEDUPS_USED += o9_speedups_used
                TOTAL_SPEEDUPS_EARNED += o9_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o9_extra_pacts) * ps + dtp * ts

            elif solution == o10:
                TOTAL_SPEEDUPS_USED += o10_speedups_used
                TOTAL_SPEEDUPS_EARNED += o10_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o10_extra_pacts) * ps

            elif solution == o11:
                TOTAL_SPEEDUPS_USED += o11_speedups_used
                TOTAL_SPEEDUPS_EARNED += o11_rewards
                ttl = dtt
                mtl = dmt
                spaa += (dpp + o11_extra_pacts) * ps + dtp * ts
