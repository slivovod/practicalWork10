import random as rnd

arr = []
len = 20
for i in range(len):
    element = rnd.randint(-2, 7)
    if(element != 0):
        arr.append(element)
arr.sort()
print(arr)