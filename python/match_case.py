print('*'*50)
print("\tArthematic operators")
print('*'*50)
print('\t1.Addition')
print('\t2.subtraction')
print('\t3.multiplication')
print('\t4.division')
print('\t5.modular division')
print('\t6.Power')
print('\t7.Floor division')
print("*"*50)
choice=int(input('enter a choice'))
match(choice):
    case 1:
        print('enter values of a,b for addition')
        a,b=map(int,input().split())
        c=a+b
        print(c)
    case 2:
        print('enter values of a,b for subtraction')
        a,b=map(int,input().split())
        c=a-b
        print(c)
    case 3:
        print('enter values of a,b for multiplication')
        a,b=map(int,input().split())
        c=a*b
        print(c)
    case 4:
        print('enter values of a,b for division:')
        a,b=map(int,input().split())
        c=a/b
        print(c)
    case 5:
        print('enter values of a,b for modular division:')
        a,b=map(int,input().split())
        c=a%b
        print(c)
    case 6:
        print('enter values of a,b for power division:')
        a,b=map(int,input().split())
        c=pow(a,b)
        print(c)
    case 7:
        print('enter values of a,b for floor division:')
        a,b=map(int,input().split())
        c=a//b
        print(c)
    case _:
        print('enter a valid input')
        
    
