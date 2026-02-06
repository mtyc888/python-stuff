usernames = []
if len(usernames) == 0:
    print('we need to find users')
for name in usernames:
    if name == 'admin':
        print('would you like to see the status report?')
    else:
        print(f'hello {name}')