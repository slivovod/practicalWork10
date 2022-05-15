import random as rnd

arr = []
for i in range(10):
    arr.append(rnd.randint(0, 20))
print("before sorting array: \n", arr)
arr_start = sorted(arr[:4])
arr_mid = arr[4:-4]
arr_end = sorted(arr[-4:], reverse=True)

arr_sort = arr_start + arr_mid + arr_end

print("after sorting array: \n", arr_sort)