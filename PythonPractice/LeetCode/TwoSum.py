def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[j]==target - nums[i]):
                return (i,j)
if __name__=='__main__':
    n = int(input())
    num = list(map(int,input().rstrip().split()))[:n]
    target = int(input())
    print(twoSum(num,target))

