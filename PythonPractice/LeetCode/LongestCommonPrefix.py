def longest_common_prefix(string):
    if not string:
        return ""
    prefix = string[0]
    for i in range(1, len(string)):
        while string[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if len(prefix) == 0:
                return ""
    return prefix

if __name__ == '__main__':
    n = int(input())
    input_string = list(input().rstrip().split())[:n]
    print(longest_common_prefix(input_string))
