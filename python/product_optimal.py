# Optimal version of product_except_self problem

def product(array):
    n=len(array)
    result=[1]*n
    #prefix
    prefix=1
    for i in range(n):
        result[i]=prefix*result[i]
        prefix*=array[i]
    # suffix
    suffix=1
    for i in range(n-1,-1,-1):
        result[i]=suffix*result[i]
        suffix*=array[i]

    return result







array=[1,2,3,4]
print(product(array))
