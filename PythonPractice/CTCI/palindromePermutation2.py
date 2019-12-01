def isPermuationPalindrome(phrase):
    bitvector = createBitVector(phrase)
    return bitvector == 0 or checkExactlyOneBitSet(bitvector)
#Create a bit vector for the string, for each letter with value i, toggle ith bit
def createBitVector(phrase):
    bitvector = 0
    for c in phrase:
        x = getCharNumber(c)
        bitvector = toggle(bitvector,x)
    return bitvector

#Toggle the ith bit in the integer
def toggle(bitvector, index):
    if (index < 0):
        return bitvector

    mask = 1<<index
    if ((bitvector and mask) == 0):
        bitvector!=mask
    else:
        bitvector&=~mask
    return bitvector

def getCharNumber(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')

    val = ord(c)
    if (a <= val and val <= z):
        return val - a
    elif (A <= val and val <= Z):
        return val - A
    return -1

#check that exactly one bit is set by subtracting one from the integer and anding with the original integer
def checkExactlyOneBitSet(bitvector):
    return (bitvector & (bitvector-1))==0
if __name__=='__main__':
    input_string = input()
    print(isPermuationPalindrome(input_string))