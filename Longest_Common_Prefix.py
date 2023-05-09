def longestCommonPrefix(arr):
    res = ""
    for i in range(len(arr[0])):
        for s in arr:
            if i == len(s) or s[i] != arr[0][i]:
                return res
        res += arr[0][i]
    return res


poop = [""]
print(longestCommonPrefix(poop))