# Your task is to make a function that can take any non-negative integer as an argument and return it with its 
# digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    
    str_num = str(num)
    arr = []
    
    for i in str_num:
       arr.append(i)
    
    sorted_arr = sorted(arr)[::-1]
    result = ''.join(sorted_arr)
    
    return int(result)
