def isPermutationOfPalindrome(phrase):
    table = buildCharFrequency(phrase)
    return checkMaxOneOdd(table)

def checkMaxOneOdd(table):
    foundOdd = False
    for count in table:
        if count%2==1:
            if foundOdd:
                return False
            foundOdd = True
    return True
def getCharNumber(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if (a <= val and val <= z):
        return val - a
    elif(A <= val and val <= Z):
        return val - A

    return -1
def buildCharFrequency(phrase):
    table = [0 for _ in range(ord('z')-ord('a')+1)]
    for char in phrase:
        x = getCharNumber(char)
        if (x!=-1):
            table[x]+=1
    return table
if __name__=='__main__':
    input_string = input()
    #length = len(input_string)
    print(isPermutationOfPalindrome(input_string))
