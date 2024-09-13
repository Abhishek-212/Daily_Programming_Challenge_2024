def merge_arr(arr1, arr2, m, n):
    arr1 = arr1 + arr2
    arr1.sort()
    list1, list2 = [], []
    for i in range(m):
        list1.append(arr1[i])
    print(list1)
    for j in range(m, m+n):
        list2.append(arr1[j])
    print(list2)

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
m = len(arr1) ; n = len(arr2)
merge_arr(arr1, arr2, m, n)