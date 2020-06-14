from itertools import combinations


def solution(num_buns, num_required):
    keyrings = [[] for i in range(num_buns)]
    copies_per_key = num_buns - num_required + 1

    for key, bunnies in enumerate(combinations(range(num_buns), copies_per_key)):
        for bunny in bunnies:
            print(keyrings, bunny, key, bunnies)
            keyrings[bunny].append(key)
    return keyrings
