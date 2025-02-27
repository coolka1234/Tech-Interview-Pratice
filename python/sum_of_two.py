# Given two integers a and b, return the sum of the two integers without using the operators + and -.

def sum_without_op(a, b):
    def to_binary(num):
        return bin(num)
    a, b = to_binary(a), to_binary(b)
    if len(a)>len(b):
        a, b = b, a
    bigger_len=len(a)
    smaller_len=len(b)
    while smaller_len < bigger_len:
        ''.join(('0', b))
    carry=0
    sum=""
    for j in range(bigger_len, -1, -1):
        if carry==1:
            if a[j]=='0' and b[j]=='0':
                ''.join(('0', sum))
            elif (a[j]=='0' and b[j]=='1') or (a[j]=='0' and b[j] == '0'):
                ''.join(('1', sum))
            else:
                ''.join(('0', sum))
                carry=1
        else:
            if a[j]=='0' and b[j]=='0':
                ''.join(('1', sum))
            elif (a[j]=='0' and b[j]=='1') or (a[j]=='0' and b[j] == '0'):
                carry=1
                ''.join(('0', sum))
            else:
                carry=1
                ''.join(('1', sum))
    return sum

a, b = 102, 1029
print(sum_without_op(a,b))




