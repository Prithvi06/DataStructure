#ATOI
s='-12434asdf'
s = s.strip()
result = 0
sign = 1
j = 0
if s == '' or s[0] >= 'a' and s[0] <= 'z' or s[0] >= 'A' and s[0] <= 'Z':
    print(0)

if s[0] == '-':
    sign = -1
    j += 1
elif s[0] == '+':
    sign = 1
    j = j + 1
if len(s) >= 2:
    if s[1] == '-' or s[1] == '+':
        print(0)
for i in range(j, len(s)):

    if s[i] >= '0' and s[i] <= '9':
        result = result * 10 + ord(s[i]) - 48
    else:
        break
result = result * sign
if result >= -2 ** 31 and result <= 2 ** 31 - 1:
    print(result)
else:
    if result <= -2 ** 31:
        print( -2147483648)
    else:
        print(2147483647)

#STRSTR
'''s='abcabcabcd'
x='abcd'
n = len(s)
m = len(x)
for i in range(n-m+1):
        print(s[i:m+i])
        if s[i:m+i]==x:
            print(i)'''