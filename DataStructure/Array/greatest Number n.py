nums=list(map(int,input('enter list').split()))
k=int(input('enter k value'))
n=len(nums)/k
dict1={}
for i in nums:
            if  i in dict1:
                print(i)
                dict1[i]=dict1[i]+1
            else:
                dict1[i]=1
print(dict1)
list1=[]
for key,val in dict1.items():
            if val>n:
                list1.append(key)
    
print(list1)
        
