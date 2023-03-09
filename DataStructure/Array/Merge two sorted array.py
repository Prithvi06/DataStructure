arr1=[1,5,9,10,15,20]
arr2=[2,3,8,13]
for i in range(len(arr1)):
    if arr1[i]>arr2[0]:
        arr1[i],arr2[0]=arr2[0],arr1[i]
        arr2.sort()
print(arr2,arr1)