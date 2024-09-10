
def missing_num(arr, length):
    full_set = set(range(1, length+1))   # Creating arr of all elements
    arr_set = set(arr)                   # Passing original arr in set
    missing_numbers = full_set - arr_set
    if missing_numbers:                  # if missing_numbers have value
        print(" ".join(map(str, missing_numbers)))
    else:                                # if missing_numbers NOT have value 
        print(length+1)

arr = [2,3,4]
length = arr[-1]                  # Getting last element as length
missing_num(arr, length) 
