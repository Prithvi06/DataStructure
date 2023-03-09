'''string='ABC'
m_list=[]
m_list.append(string)
t_list=[]
for i in range(len(string)-1):
    for word in m_list:
        for j in range(i,len(word)):
            word=list(word)
            word[i],word[j]=word[j],word[i]
            nword=''.join(word)
            t_list.append(nword)
    m_list=t_list
    t_list=[]
    
print(m_list)

'''
input=[1,2,3]
m_list=[]
m_list.append(input)
t_list=[]
for i in range(len(input)-1):
    for words in m_list:
        for j in range(i,len(words)):
            word = words.copy()
            #print(word)
            word[i],word[j]=word[j],word[i]
            t_list.append(word)
            #print('tlist',t_list)
    m_list=t_list
    t_list=[]
    
print('mlist',m_list)
sort_list=sorted(m_list)
print(sort_list)
import math
element=[3,2,1]
index=max(index for index,item in enumerate(sort_list) if item==element)
if index==math.factorial(len(input))-1:
    index=0
    print(index,sort_list[index])
else:
    print(index,sort_list[index+1])
result=repr(sort_list[index]).replace(' ','')
print(type(eval(result)))