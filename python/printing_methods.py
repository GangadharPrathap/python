print('sum of two numbers using python')
#coma seperator method
a=int(input('enter the value of A:'))
b=int(input('enter the value of B:'))
c=a+b
print('Addition of ',a,'and',b,'is',c)
#string modulo method
print('addition of %d and %d is %d'%(a,b,c))
#formated method
print('addition of {} and {} is {}'.format(a,b,c))
#concatenation method
print('addition of '+str(a)+' and '+str(b)+' is '+str(c))