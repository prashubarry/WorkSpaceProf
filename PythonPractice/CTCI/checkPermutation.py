def checkPermutation(s1,s2):
    NUM_OF_CHARS = 256
    count1 = [0]*NUM_OF_CHARS
    count2 = [0]*NUM_OF_CHARS

    for i in s1:
        count1[ord(i)]+=1
    for i in s2:
        count2[ord(i)]+=1

    if (len(s1)!=len(s2)):
        return False
    for x in range(NUM_OF_CHARS):
        if count1[x]!=count2[x]:
            return False
    return True

if __name__=='__main__':
    s1 = input()
    s2 = input()

    print(checkPermutation(s1,s2))