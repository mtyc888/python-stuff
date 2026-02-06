usernames = ['p1','p2','p3','p4','p5', 'admin']

for name in usernames:
    if name == 'admin':
        print('would you like to see the status report?')
    else:
        print(f'hello {name}')