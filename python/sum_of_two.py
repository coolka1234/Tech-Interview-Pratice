# Given two integers a and b, return the sum of the two integers without using the operators + and -.

def sum_without_op(a, b):
    def to_binary(num):
        return bin(num)
    a, b = to_binary(a), to_binary(b)
    b=b[2:]
    a=a[2:]
    if len(a)>len(b):
        a, b = b, a
    bigger_len=len(b)
    smaller_len=len(a)
    print(f'{smaller_len}, {bigger_len}, {a}, {b}')
    while smaller_len < bigger_len:
        a=''.join(('0', a))
        smaller_len+=1
    carry=0
    sum=""
    print(f'{smaller_len}, {bigger_len}, {a}, {b}')
    for j in range(bigger_len-1, -1, -1):
        if carry==0:
            if a[j]=='0' and b[j]=='0':
                sum=''.join(('0', sum))
            elif (a[j]=='0' and b[j]=='1') or (a[j]=='1' and b[j] == '0'):
                sum=''.join(('1', sum))
            else:
                sum=''.join(('0', sum))
                carry=1
        else:
            if a[j]=='0' and b[j]=='0':
                sum=''.join(('1', sum))
                carry=0
            elif (a[j]=='0' and b[j]=='1') or (a[j]=='1' and b[j] == '0'):
                carry=1
                sum=''.join(('0', sum))
            else:
                carry=1
                sum=''.join(('1', sum))
    return int(sum, 2)

def sum_without_op_optimally(a, b):
    MASK = 0xFFFFFFFF 
    while b != 0:
        carry = (a & b) << 1   
        a = (a ^ b) & MASK    
        b = carry & MASK     

    return a if a <= 0x7FFFFFFF else ~(a ^ MASK)

a, b = 102, 1207102983
print(sum_without_op(a,b))




