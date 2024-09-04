n=int(input())
r=0
z=1
while n!=0:
    d=n%10
    r=r+d
    z=z*d
    n=n//10
if(r==z):
    print('Spy Number')
else:
    print('Not Spy Number')