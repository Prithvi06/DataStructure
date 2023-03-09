a=[-1,-2,-3,-2,5]
max_val=min(a)
print(min(a))
max_end=0
start=end=s=0
for  i in range(len(a)):
        max_end=max_end+a[i]
        if max_end>max_val:
            max_val=max_end
            start=s
            end=i
        if max_end<=0:
            max_end=0
            s=i+1
print(max_val,start,end)
