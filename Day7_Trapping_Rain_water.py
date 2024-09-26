
def trapped_water(arr):
    #print("Original Arr:",f"{arr}")
    left_arr =[]
    right_arr = []
    left_max = arr[0]
    left_arr.append(left_max)
    right_max = arr[-1]
    # right_arr.insert(0,right_max)
    
    # From left to Right store max
    for num in arr[1:]: #start from index 1
        if num > left_max:
            left_max = num
            left_arr.append(left_max)
        else:
            left_arr.append(left_max)
    #print("Left         ",left_arr)
    
    # From Right to left
    for num in reversed(arr):
        if num > right_max:
            right_max = num
            right_arr.insert(0,right_max)
        else:
            right_arr.insert(0,right_max)
    #print("Right        ",right_arr)
    
# Formula trapped_amount= min(left_arr[i],right_arr[i])- arr(i)
    trapped_sum = 0
    for j in range(len(arr)):
        trapped_amount = min(left_arr[j], right_arr[j])- arr[j]
        trapped_sum += trapped_amount
    print("Trapped Output",trapped_sum)
    
# Driver Code
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
trapped_water(arr)
