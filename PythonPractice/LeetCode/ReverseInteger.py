import sys
def reverseInteger(num):
    negativeFlag = False
    if (num < 0):
        negativeFlag = True
        num=-num
    rev_num = 0
    prev_rev_num = 0
    while(num!=0):
        curr_digit = num % 10
        rev_num = (rev_num * 10 ) + curr_digit
        #check if the reverse has got overflowed
        if(rev_num >= sys.maxsize or rev_num <= -sys.maxsize-1):
            rev_num = 0
        if((rev_num-curr_digit)//10!=prev_rev_num):
            print("WARNING OVERFLO qWED!")
            return 0
        prev_rev_num = rev_num
        num = num//10

    return -rev_num if (negativeFlag == True) else rev_num
if __name__ =='__main__':
    number = int(input())
    print(reverseInteger(number))