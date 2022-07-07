def findTriangles():
    for i in range(1,55):
        triangles.append(i*(i+1)/2)

with open("p042_words.txt") as f:
    input = f.readlines()
    input = list(eval(*input))

triangles = []
findTriangles()
minus = ord("A")-1
maxvalue = 0
triwords = []
for word in input:
    nums = []
    for letter in word:
        nums.append(ord(letter)-minus)
    maxvalue = max(sum(nums), maxvalue)
    if sum(nums) in triangles:
        triwords.append(word)
print(triwords, len(triwords))