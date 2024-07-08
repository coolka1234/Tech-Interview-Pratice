# // I want to know the size of the longest consecutive elements of X in Y. You will receive two arguments: items and key. Return the length of the longest segment of consecutive keys in the given items.

# // Notes:

# //     The items and the key will be either an integer or a string (consisting of letters only)
# //     If the key does not appear in the items, return 0

# // Examples

# // 90000, 0           -->  4
# // "abcdaaadse", "a"  -->  3
# // "abcdaaadse", "z"  -->  0

def consecutive(item, key):
    if isinstance(item, int):
        item=str(item)
        key=str(key)
    num_of_occurences=0
    max=0
    for i in (item):
        if(i==key):
            num_of_occurences+=1
        else:
            if num_of_occurences>max:
                max=num_of_occurences
            num_of_occurences=0
    if num_of_occurences:
        if num_of_occurences>max:
            return num_of_occurences
    return max
if __name__=="__main__":
    print(consecutive("abcdaaadse", "a"))

