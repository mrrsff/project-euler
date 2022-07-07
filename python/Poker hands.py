def computeMatch(input):
    input = input.split()
    p1 = input[:5]
    p2 = input[5:]
    s1 = score(p1)
    s2 = score(p2)
    return s1, s2


def score(hand):
    scr = 0
    suits = [i[1] for i in hand]
    nums = [i[0] for i in hand]
    for i in range(len(nums)):
        if nums[i] == "T":
            nums[i] = "10"
        elif nums[i] == "J":
            nums[i] = "11"
        elif nums[i] == "Q":
            nums[i] = "12"
        elif nums[i] == "K":
            nums[i] = "13"
        elif nums[i] == "A":
            nums[i] = "14"
    nums = list(map(int, nums))
    highest = max(nums)
    pair = pairType(suits, nums)
    straight = sorted(nums) == sorted(list(range(min(nums), max(nums) + 1)))
    flush = suits.count(suits[0]) == len(suits)
    straightFlush = flush and straight
    royal = list(range(10, 15)) == nums and flush
    if royal:
        return 9, 0
    if straightFlush:
        return 8, 0
    if pair[0] == 6:
        return 7, pair[1][0]
    if pair[0] == 5:
        return 6, pair[1]
    if flush:
        return 5, 0
    if straight:
        return 4, 0
    if pair[0] == 3:
        return 3, pair[1][0]
    if pair[0] == 2:
        return 2, pair[1][0], pair[1][2]
    if pair[0] == 1:
        return 1, pair[1][0]
    return 0, highest


def pairType(suits, nums):
    quality = 0
    pairs = [i for i in nums if nums.count(i) > 1]
    indexes = [i for i in range(len(nums)) if nums.count(nums[i]) > 1]
    values = [nums[i] for i in indexes]
    if len(set(pairs)) == 1 and len(pairs) == 3:  # threeofakind
        quality += 3
    if len(set(pairs)) == 1 and len(pairs) == 2:  # onepair
        quality += 1
    if len(set(pairs)) == 2 and len(pairs) == 4:  # twopair
        quality += 2
    if len(set(pairs)) == 1 and len(pairs) == 4:  # fourofakind
        quality += 6
    return quality, sorted(values)


with open("p054_poker.txt") as f:
    pokerHands = f.readlines()
    for i in range(len(pokerHands)):
        pokerHands[i] = pokerHands[i][:-1]
win1 = 0
win2 = 0
for i in pokerHands:
    p1, p2 = computeMatch(i)
    if p1[0] == p2[0]:
        if p1[1] > p2[1]:
            win1 += 1
            winner = "P1"
        elif p2[1] > p1[1]:
            win2 += 1
            winner = "P2"
    elif p1[0] > p2[0]:
        win1 += 1
        winner = "P1"
    elif p1[0] < p2[0]:
        win2 += 1
        winner = "P2"
    print(p1, "vs", p2,"\nwinner is:", winner)
print("Player 1 won",win1,"games.")
