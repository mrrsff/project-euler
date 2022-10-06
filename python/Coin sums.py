coins = [1,2,5,10,20,50,100,200]
coins = coins[::-1]

balance = 200
ans = 0
def find(remaining, coins=):
    global ans
    if coins:
        remaining -= coins[0]
        if not remaining:
            print(coins.pop(0))
            find(balance)
            ans += 1
        else:
            find(remaining)

find(balance)
print(ans)
