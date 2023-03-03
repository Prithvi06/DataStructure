s="aba"
Dict = {}
for c in s:
    if c in Dict.keys():
        Dict[c] = Dict[c] + 1
    else:
        Dict[c] = 1
List = []
for key, value in Dict.items():
    List.append(value)
Min = min(List)
Max = max(List)
print(List,Max,Min)
if Min == Max:
    n = len(s)//Max
    print(n)
    subs = s[0:n]
    for i in range(n, len(s), n):
        if s[i:n + i] == subs:
            pass
        else:
            print("false")
    print( "true")
else:
    print("ofalse")
'''
for k in range(1, len(s) // 2 + 1):
    if s == s[k:] + s[:k]:
        print(k,s[k:] , s[:k])
        print( 'True')
print('False')'''