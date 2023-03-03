'''s='AACECAAAA'
str1=s
p=''
for i in range(len(s)-1,0,-1):
    if s==s[::-1] :
       print(len(p),p+str1)
       break
    else:
        p=p+s[-1]
        print('p',p)
        s=s[:i]
        print('e',s)
print(p+str1)'''


def ispalindrome(s):
    l = len(s)

    i = 0
    j = l - 1
    while i <= j:

        if (s[i] != s[j]):
            return False
        i += 1
        j -= 1

    return True


# Driver code
if __name__ == "__main__":

    s = "ABCDBA"
    cnt = 0
    flag = 0

    while (len(s) > 0):

        # if string becomes palindrome then break
        if (ispalindrome(s)):
            flag = 1
            break

        else:
            cnt += 1

            # erase the last element of the string
            s = s[:-1]

    # print the number of insertion at front
    if (flag):
        print(cnt)
