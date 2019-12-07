def longest_common_prefix(strs):
    def is_common_prefix(strs, length):
        str1 = strs[0][:length]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True

    if not strs:
        return ""
    min_len = len(min(strs, key=len))
    low, high = 1, min_len
    # The binary search on the length of the prefix on the first word
    while low <= high:
        mid = (low + high) // 2
        if is_common_prefix(strs, mid):
            low = mid + 1
        else:
            high = mid - 1
    return strs[0][:high]


if __name__ == '__main__':
    n = int(input())
    input_string = list(input().strip().split())
    print(longest_common_prefix(input_string))
