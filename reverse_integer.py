n=int(input())
s=0
x=0
if(n>0):
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    print(s)
else:
    f=n*(-1)
    while(f!=0):
        z=f%10
        x=x*10+z
        f=f//10
    x=(-1)*x
    print(x)
        