def isPalindrome(x):
    """Special Cases:
        1. When x<0 then the integer number is not a palindrome
        2. If the last digit of the number is 0, then the the first digit also needs to be 0 to be a palindrome.
    """
    if (x<0 or (x%10 ==0 and x!=0)):
        return False
    rev_num = 0
    while(x > rev_num):
        rev_num = (rev_num * 10) +(x % 10)
        x = x // 10
    return x == rev_num or x == rev_num//10
if __name__ == '__main__':
    number = int(input())
    print(isPalindrome(number))