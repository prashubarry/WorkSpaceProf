def twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num]=i
        else:
            return  [h[n],i]
if __name__=='__main__':
    n = int(input())
    num = list(map(int,input().rstrip().split()))[:n]
    target = int(input())
    print(twoSum(num,target))
