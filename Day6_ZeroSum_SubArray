def zero_sum_subarr(arr):
    sum_map = {}
    result = []
    curr_sum = 0
    
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum == 0:
            result.append((0,i))
        if curr_sum in sum_map:
            for start in sum_map[curr_sum]:
                result.append((start + 1,i))
        if curr_sum in sum_map:
            sum_map[curr_sum].append(i)
        else:
            sum_map[curr_sum] = [i]
    return result


arr = [1,-1,2,-2,3,-3]
n = len(arr)
print(zero_sum_subarr(arr))
