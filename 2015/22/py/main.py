import sys
from collections import namedtuple
from heapq import heappop, heappush


PLAYER_HEALTH = 50
PLAYER_MANA = 500
SPELLS = [
    (53, 4, 0, 0),
    (73, 2, 2, 0),
    (113, 0, 0, 1),
    (173, 0, 0, 2),
    (229, 0, 0, 3),
]
SHIELD_ARMOR = 7
SHIELD_TIME = 6
POISON_DAMAGE = 3
POISON_TIME = 6
RECHARGE_AMOUNT = 101
RECHARGE_TIME = 5


def solve(boss_health, boss_dmg, turn_damage):
    player_health = PLAYER_HEALTH
    player_mana = PLAYER_MANA
    game_states = [(0, 0, player_health, player_mana, boss_health, 0, 0, 0)]

    while game_states:
        (
            mana_used,
            turn,
            player_health,
            player_mana,
            boss_health,
            shield,
            poison,
            recharge,
        ) = heappop(game_states)

        if turn == 0 and (player_health := player_health - turn_damage) <= 0:
            continue

        shield -= shield and 1
        boss_health -= poison and POISON_DAMAGE
        poison -= poison and 1
        player_mana += recharge and RECHARGE_AMOUNT
        recharge -= recharge and 1

        if boss_health <= 0:
            return mana_used

        if turn == 0:
            statuses = (shield, poison, recharge)

            for spell in SPELLS:
                if player_mana < spell[0] or spell[3] and statuses[spell[3] - 1]:
                    continue

                heappush(
                    game_states,
                    (
                        mana_used + spell[0],
                        1,
                        player_health + spell[2],
                        player_mana - spell[0],
                        boss_health - spell[1],
                        spell[3] == 1 and SHIELD_TIME or shield,
                        spell[3] == 2 and POISON_TIME or poison,
                        spell[3] == 3 and RECHARGE_TIME or recharge,
                    ),
                )
        else:
            player_health = player_health - max(1, boss_dmg - (shield and SHIELD_ARMOR))

            heappush(
                game_states,
                (
                    mana_used,
                    0,
                    player_health,
                    player_mana,
                    boss_health,
                    shield,
                    poison,
                    recharge,
                ),
            )


def main():
    boss_health, boss_attack = (int(line.split()[-1]) for line in sys.stdin)

    print(solve(boss_health, boss_attack, 0))
    print(solve(boss_health, boss_attack, 1))


if __name__ == "__main__":
    main()
