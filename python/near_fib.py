n=int(input())
a=0
b=1
c=a+b
pr=0
while c<=n:
    pr=c
    c=a+b
    a=b
    b=c
if n-pr==c-n:
    print(pr,c)
elif n-pr<c-n:
    print(pr)
else:
    print(c)            