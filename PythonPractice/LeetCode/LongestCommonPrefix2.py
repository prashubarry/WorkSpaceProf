def longestCommonPrefix(strs):
    def commonPrefix(left, right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]

    def find_longestCommonPrefix(strs, left_index, right_index):
        if left_index == right_index:
            return strs[left_index]
        # recursive call
        else:
            mid_index = (left_index + right_index) // 2
            lcpLeft = find_longestCommonPrefix(strs, left_index, mid_index)
            lcpRight = find_longestCommonPrefix(strs, mid_index + 1, right_index)
            return commonPrefix(lcpLeft, lcpRight)

    if not strs:
        return ""
    return find_longestCommonPrefix(strs, 0, len(strs) - 1)


if __name__ == '__main__':
    n = int(input())
    input_string = list(input().rstrip().split())[:n]
    print(longestCommonPrefix(input_string))
