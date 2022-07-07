count = 0

for i in range(1,10):
    if i%4==2 or not i%4:
        count += 20* pow(30,(i//2-1))
    if i%4==3:
        count += 100 * pow(500,i//4)
print(count)