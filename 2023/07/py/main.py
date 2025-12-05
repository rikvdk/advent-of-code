import sys
from itertools import islice


cards = [str(i) for i in range(2, 10)] + ["T", "J", "Q", "K", "A"]
cards = ["J"] + [str(i) for i in range(2, 10)] + ["T", "Q", "K", "A"]


def counts(hand):
    return (hand.count(c) for c in set(hand))


def n_of_a_kind(hand, n):
    return any(count >= n for count in counts(hand))


def full_house(hand):
    return 3 in counts(hand) and 2 in counts(hand)


def two_pair(hand):
    temp = counts(hand)
    return 2 in temp and 2 in temp


def score(hand):
    return sum(cards.index(c) * (14 ** (5 - i)) for i, c in enumerate(hand[0]))


def main():
    part1 = 0
    part2 = 0

    hands = []
    buckets = [[] for i in range(7)]

    # for line in islice(sys.stdin, 50):
    for line in sys.stdin:
        hand = line.split()

        # if "J" not in hand[0]: continue

        foo = sorted([(hand[0].count(c), cards.index(c), c) for c in hand[0] if c != "J"], reverse=True)
        if foo and "J" in hand[0]:
            hand.append(hand[0].replace("J", foo[0][2]))
        else:
            hand.append(hand[0])

        print(hand[0])
        print(hand[2])
        # print()
        # print(foo)

        if    n_of_a_kind(hand[2], 5): buckets[6].append(hand)
        elif  n_of_a_kind(hand[2], 4): buckets[5].append(hand)
        elif  full_house( hand[2]   ): buckets[4].append(hand)
        elif  n_of_a_kind(hand[2], 3): buckets[3].append(hand)
        elif  two_pair(   hand[2]   ): buckets[2].append(hand)
        elif  n_of_a_kind(hand[2], 2): buckets[1].append(hand)
        else:                          buckets[0].append(hand)

    i = 1

    for bucket in buckets:
        bucket.sort(key=score)

        for hand, bid, _ in bucket:
            print(hand)
            part1 += int(bid) * i
            i += 1

    print(buckets)
    print(part1)
    # print(part2)


if __name__ == "__main__":
    main()
