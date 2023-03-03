strs = ["dog","racecar","car"]
def match(lenn, word, m_list):
    for i in range(lenn, 0, -1):
        if word[0:i] == m_list[0:i]:
            return word[0:i]
    return ""


m_list = []
m_list.append(strs[0])
strs.pop(0)
for word in strs:
    m = len(word)
    n = len(m_list[-1])
    if m <= n:
        m_list.append(match(m, word, m_list[-1]))
        m_list.pop(0)

    else:
        m_list.append(match(n, word, m_list[-1]))
print( m_list[-1])


#prefix which is also a suffix
'''s='blablabla'
n = len(s)

for res in range(n // 2, 0, -1):

    # Check for shorter lengths
    # of first half.
    prefix = s[0: res]
    suffix = s[n - res: n]
    print(prefix,suffix)
    if (prefix == suffix):
            print(res)'''




