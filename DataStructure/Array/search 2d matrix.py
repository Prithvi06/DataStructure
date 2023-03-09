'''matrix=[[1]]
target=3
l = 0
h = len(matrix)
for i in range(len(matrix)):
    while (l <h):
        mid = (l + h) // 2
        print(mid)
        if target == matrix[i][mid]:
            print('true')
            break
        if target < matrix[i][mid]:
            h = mid - 1
        else:
            l = mid + 1
print('false')

def twoSum( num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i + 1
        else:
            return map[num[i]], i + 1

    return -1, -1

res=twoSum([2,6,5,8,12], 14)
print(res)'''



s="abcabcbb"
max_len = 0
l = 0
sset = []
for r in range(len(s)):
    if s[r] not in sset:
        sset.append(s[r])
        max_len = max(max_len, r - l + 1)
        print(max_len,sset)
    else:
        while (s[r] in sset):
            sset.remove(s[l])
            print('after remove',s[l],sset)
            l += 1
        sset.append(s[r])
        print('then append',sset)
        max_len = max(max_len, r - l + 1)
print(max_len)

