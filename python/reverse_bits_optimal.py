
def reverse_bits(n):
    result = 0
    for i in range(32):  # Iterate over all 32 bits
        result = (result << 1) | (n & 1)  # Shift left and add the last bit of n
        n >>= 1  # Shift n to the right (remove processed bit)
    return result

integer=0b00000010100101000001111010011100

print(reverse_bits(integer))
