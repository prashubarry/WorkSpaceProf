#Sherlock and Anagrams
import os
from collections import defaultdict

def sherlockAndAnagrams(s):
    substrings = defaultdict(int)
    #Finds all the anagrams of the given inupt string
    for i in range(1,len(s)):
        for j in range(len(s) - i + 1):
            substrings[''.join(sorted(s[j:j+i]))] += 1
    ans = 0
    for key,value in substrings.items():
        ans += value * (value-1) // 2

    return (ans)

if __name__=='__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)