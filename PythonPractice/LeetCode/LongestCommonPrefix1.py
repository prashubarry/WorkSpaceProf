def longest_common_prefix_v(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]


if __name__ == '__main__':
    n = int(input())
    input_string = list(input().rstrip().split())[:n]
    print(longest_common_prefix_v(input_string))
