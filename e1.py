import random as rnd

arr = []
try:
    n = int(input())
except:
    n = 1
for i in range(n):
    arr.append(rnd.randint(0, 100))

min_element_value = arr[0]
max_element_value = arr[0]
max_element_index = 0
for i in range(n):
    if(min_element_value > arr[i]):
        min_element_value = arr[i]
    if(max_element_value < arr[i]):
        max_element_value = arr[i]
        max_element_index = i
print(arr)
print("min element value: ", min_element_value)
print("max element value: ", max_element_value, " ||  max element index: ", max_element_index)