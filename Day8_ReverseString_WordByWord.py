def reverse_string(input):
    input_list = input.split()
    reversed_list = input_list[::-1]
    # joining each word in reversed_list
    print('"'+' '.join(reversed_list)+'"')

# Driver 
input = "A good       example"
reverse_string(input)
