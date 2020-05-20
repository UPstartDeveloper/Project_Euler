"""
Hacker Rank Problem found here:
https://www.hackerrank.com/challenges/electronics-shop/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

1. Clarifying Questions
    - are the prices on positive integers?
    - will the prices alwas be unique within one array?
    - is the array sorted?
    - size limits on any kind on the lists?

2. Assumptions:
    - a keyboard and a USB always have a price > 0
    - prices are always positive integers
    - no duplicates within the same list of a product's prices
    - not sorted (although it make sense for a store)
    - from the problem description, we know the lists may or may not be equal
       in length, and that there'll always be between 1 and 1000 items for
       both a USB or keyboard (referred tp here as 'products')


Idea 1: using for loops
- esstenially re-implement naive two sum
- use for loops to record all combinations
- take the max of these combinations that is <= budget, and return it
- if all combos are > budget, then return -1
"""


def find_combos(keyboards, drives, b):
    """Traverse both arrays of prices such that there are always two products
       being combined.

    """
    # make the shorter list the one iterated over in the outer loop
    if len(keyboards) <= len(drives):
        outer, inner = keyboards, drives
    else:  # len(keyboards) > len(drives)
        outer, inner = drives, keyboards
    # build the combinations
    combos = list()
    for price1 in outer:
        for price2 in inner:
            combo = price1 + price2
            # only add combos within budget, and that have both products
            if combo <= b and price1 > 0 and price2 > 0:
                combos.append(combo)
    return combos


def get_money_spent(keyboards, drives, b):
    # calculate all ways the customer can purchase the product
    combos = find_combos(keyboards, drives, b)
    # in case there were no combinations that fit the requirements
    if len(combos) == 0:
        return -1
    # choose the combination that spends the most money in combos list
    max_combo = 0
    for combo in combos:
        if combo > max_combo:
            max_combo = combo
    return max_combo
