def sorting_arr(arr, n):
    zeros, once, twos = [], [], []
    
    for i in range(n):
        if arr[i] == 0:
            zeros.append(arr[i])
        if arr[i] == 1:
            once.append(arr[i])
        if arr[i] == 2:
            twos.append(arr[i])
    print(zeros + once + twos)
    

arr = [0, 1, 2, 1, 0, 2, 1, 0]
n = len(arr)
sorting_arr(arr, n)

# OR 
"""
def sorting_arr(arr):
    print([x for x in arr if x == 0] + [x for x in arr if x == 1] + [x for x in arr if x == 2])

arr = [0, 1, 2, 1, 0, 2, 1, 0]
sorting_arr(arr)
"""