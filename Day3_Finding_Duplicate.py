
def find_duplicate(arr):
    elements = set()
    for num in arr:
        if num in elements:
            return num
        elements.add(num)
arr = [2, 3, 1, 3, 4]
print(find_duplicate(arr))
