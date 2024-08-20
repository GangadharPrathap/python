a,b=map(int,input().split())
n=int(input())
for i in range(a,b+1,1):
    print('{} X {} ={}'.format(i,n,i*n))