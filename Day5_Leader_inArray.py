def find_leader(arr, n):
    leader = []
    
    max_from_right = arr[-1]       # seting last element as leader
    leader.append(max_from_right)  # for(start, stop, steps)

    for i in range(n-1, -1, -1):
        if arr[i] > max_from_right:
            leader.append(arr[i])
            max_from_right = arr[i]
    leader.reverse()
    print(leader)


arr = [1,2,3,1000000]
n = len(arr)
find_leader(arr, n)
