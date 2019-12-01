def isPermutationOfPalindrome(phrase):
    countOdd = 0
    table = [0 for _ in range(ord('z')-ord('a')+1)]
    for char in phrase:
        x = getCharNumber(char)
        if x!=-1:
            table[x]+=1
            if table[x]%2==1:
                countOdd+=1
            else:
                countOdd-=1
    return countOdd<=1

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

if __name__=='__main__':
    input_string = input()
    print(isPermutationOfPalindrome(input_string))
