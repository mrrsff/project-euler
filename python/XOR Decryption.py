def is_valid(c):
    return ord("0") <= c <= ord("9") or ord("a") <= c <= ord("z") or ord("A") <= c <= ord("Z") or chr(c) in [" ",",",".",":",";","+","[","],"""]
with open("p059_cipher.txt") as f:
    encrypted = list(map(int,f.readline().strip().split(",")))

decrypt = []
for i in range(ord("a"),ord("z")+1):
    for j in range(ord("a"),ord("z")+1):
        for k in range(ord("a"),ord("z")+1):
            decrypted = []
            for a in range(0,len(encrypted),3): 
                key = i,j,k
                if not is_valid(encrypted[a]^i) or not is_valid(encrypted[a+1]^j) or not is_valid(encrypted[a+2]^k):
                    decrypted = []
                    break
                decrypted.append(chr(encrypted[a]^i))
                decrypted.append(chr(encrypted[a+1]^j))
                decrypted.append(chr(encrypted[a+2]^k))
            if decrypted:
                decrypt.append("".join(decrypted))
print(decrypt)