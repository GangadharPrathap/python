print('*'*50)
print('\tprint color name')
print('*'*50)
print('\tV ---> violet')
print('\tY ---> indigo')
print('\tB ---> blue')
print('\tY ---> Yellow')
print('\tO ---> Orange')
print('\tR ---> Red')
print('*'*50)
ch=input('enter a choice')
match(ch):
    case 'V':
        print('\tV ---> violet')
    case 'I':
        print('\tY ---> indigo')
    case 'B':
        print('\tB ---> blue')
    case 'G':
        print('\tB ---> blue')
    case 'Y':
        print('\tY ---> Yellow')
    case 'O':
        print('\tO ---> Orange')
    case 'R':
        print('\tR ---> Red')
    case _:
        print('enter in small letters or invalid color input')
print('*'*50)
