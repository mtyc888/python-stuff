ans = ''

while ans != 'quit':
    ans = input('what is your age?')
    age = int(ans)
    if age < 3:
        print('free')
    elif age >= 3 and age <= 12:
        print('$10')
    else:
        print('$15')
