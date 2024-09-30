from itertools import permutations

def find_permutation(string):
    permut_list = [''.join(perm) for perm in permutations(string)]
    print(permut_list)

if __name__ == "__main__":
    
    strings = ['abcd']
    
    for string in strings:
        find_permutation(string)
