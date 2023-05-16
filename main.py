passwordTrue = 'okey231'

for i in range(3):
    password = input("password -> ")
    if password == 'okey231':
        print('password is correct')
        break
    elif i < 2:
        print('password is dont correct')
    else:
        print('user is blocked')
