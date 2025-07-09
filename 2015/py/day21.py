import sys
from collections import namedtuple
from itertools import combinations


WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
ARMORS = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
RINGS = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


def simulate(player_attack, player_armor, boss_health, boss_attack, boss_armor):
    player_health = 100
    player_damage = max(1, player_attack - boss_armor)
    boss_damage = max(1, boss_attack - player_armor)

    while True:
        if (boss_health := boss_health - player_damage) <= 0:
            return True

        if (player_health := player_health - boss_damage) <= 0:
            return False


def main():
    part1 = 500
    part2 = 0

    boss_health, boss_attack, boss_armor = (int(line.split()[-1]) for line in sys.stdin)

    for weapon in WEAPONS:
        for armor in ARMORS:
            for (ring1, ring2) in combinations(RINGS, 2):
                cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
                player_attack = weapon[1] + ring1[1] + ring2[1]
                player_armor = armor[1] + ring1[2] + ring2[2]

                if simulate(
                    player_attack, player_armor, boss_health, boss_attack, boss_armor
                ):
                    part1 = min(part1, cost)
                else:
                    part2 = max(part2, cost)

    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
