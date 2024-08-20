a,b=map(int,input().split())
for i in range(1,b+1,1):
    if b*i%a==0:
        lcm=b*i
        print(lcm)
    break    