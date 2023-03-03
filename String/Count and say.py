def countandsay(num):
    print('c',num)
    str1 = num + ' '
    newstr = ''
    #arr = [0] * (int(max(str1)) + 1)
    j = 1
    k = 0
    for i in (str1):
        if i != ' ':
            k += 1
            if i == str1[k]:
                j += 1
            else:
                #arr[int(i)] = j
                newstr += str(j)#str(arr[int(i)])
                newstr += i
                j=1
                #arr[int(i)] = 0
    return newstr

n=10
if n == 1:
    print("1")
num = "1"
for i in range(1, n):
    num = countandsay(num)
print( num)