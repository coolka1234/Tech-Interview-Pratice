# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def max_profi(array):
    highest=0
    i=1
    for index, num in enumerate(array, i):
        for sec_num in array[index:]:
            print(f"{sec_num}, {num}")
            if sec_num - num > highest:
                highest=sec_num - num
                print(highest)
    return highest  
                

if __name__=='__main__':
    array=[7,1,5,3,6,4]
    print(max_profi(array))

