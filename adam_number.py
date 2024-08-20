# square of 12=144
# rev of 12=21
# square of 21=441
# reverse of 144=441      hence it is an adam number
n=int(input())
s=n**2
rev=0
while n!=0:
    c=n%10
    rev=rev*10+c
    n=n//10
d=rev**2
res=0
while d!=0:
    x=d%10
    res=res*10+x
    d=d//10
print('true'if s==res else 'false')