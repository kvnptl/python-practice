def count_substring(string, sub_string):
    cnt = 0

    # My code
    # if sub_string[0] in string:
    #     j = 0
    #     idx = 0
    #     for i in range(len(string)):
    #         for k in range(idx, len(string)):
    #             if string[k] == sub_string[j]:
    #                 j += 1
    #                 if j == len(sub_string):
    #                     cnt += 1
    #                     j = 0
    #                     idx = k-len(sub_string)+1+1
    #                     break
    #             else:
    #                 j = 0
    #         if idx+len(sub_string) > len(string):
    #             break

    # Optimized code
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            cnt += 1

    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
