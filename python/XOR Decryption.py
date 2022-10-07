from time import process_time


with open("p059_cipher.txt") as f:
    encrypted = list(map(int,f.readline().strip().split(",")))

def solve(key, encrypted):
    ans = []
    for a in range(0,len(encrypted),3):
        ans.append(chr(encrypted[a]^key[0]))
        ans.append(chr(encrypted[a+1]^key[1]))
        ans.append(chr(encrypted[a+2]^key[2]))
    return "".join(ans)

def score(decrypted):
    ans = 0
    for i in decrypted:
        if 65 <= i <= 90:
            ans += 1
        elif 97 <= i <= 122:
            ans += 1
        elif i <= 31:
            ans -= 20
    return ans

best_key = None
best_sc = 0
for i in range(ord("a"),ord("z")+1):
    for j in range(ord("a"),ord("z")+1):
        for k in range(ord("a"),ord("z")+1):
            decrypted = []
            for a in range(0,len(encrypted),3): 
                key = i,j,k
                decrypted.append(encrypted[a]^i)
                decrypted.append(encrypted[a+1]^j)
                decrypted.append(encrypted[a+2]^k)
            sc = score(decrypted)
            if sc >= best_sc:
                best_sc = sc
                best_key = key

ans = solve(best_key, encrypted)
print(ans)
value = sum(ord(i) for i in ans)
print(f"Answer is {value}, elapsed time: {round(process_time(),3)}")