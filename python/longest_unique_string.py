# Given a string s, find the length of the longest without duplicate characters.

#brute force

def find_longest_unique(string):
    def is_unique(string):
        set_of_letters=set()
        for letter in string:
            if letter in set_of_letters:
                return False
            else:
                set_of_letters.add(letter)
        return True
    best=""
    best_len=0
    for i in range(len(string)):
        for j in range(len(string)):
            sub_string=string[i:j]
            if is_unique(sub_string) and len(sub_string)>best_len:   
                best=sub_string
                best_len=len(sub_string)
    return best

def find_longest_unique_optimal(s):
    seen = set()  
    left = 0
    max_length = 0

    for right in range(len(s)):  
        while s[right] in seen:  
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])  
        max_length = max(max_length, right - left + 1)

    return max_length


s = "abcabcbb"
print(find_longest_unique_optimal(s))  
string="asldkfeohalskd,hfahtwoalhdc"
print(find_longest_unique(string))
