#linear search
lst=[1,2,3,4,5]
se=2
flag=0
for i in range (0,len(lst),1):
    if lst[i]==se:
     flag=1
    break
if flag==1:
    print('found')
else:
    print('not found')    
