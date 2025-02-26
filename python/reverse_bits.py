# Reverse bits of a given 32 bits unsigned integer.
def reverse(integer):
    power=len(integer)
    number=0
    index=len(integer)-1
    for i in range(power-1, -1, -1):
        if(integer[index]=='1'):
            number+=pow(2, i)
        index-=1
    return number

integer="00000010100101000001111010011100"

print(reverse(integer=integer))


