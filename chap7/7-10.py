ans = ''
poll = []
china = 0
usa = 0
russia = 0
while ans != 'quit':
    ans = input('where would you want to go\n 1) China \n 2) USA \n 3) Russia \n 4) quit')
    pick = int(ans)
    if pick == 4:
        for pick in poll:
            if pick == 'China':
                china+=1
            elif pick == 'USA':
                usa+=1
            elif pick == 'Russia':
                russia +=1
            else:
                ans = "quit"
        print(f" China: {china} \n USA: {usa} \n Russia: {russia}\n")
        ans = 'quit'
    else:
        if pick == 1:
            poll.append('China')
        elif pick == 2:
            poll.append("USA")
        elif pick == 3:
            poll.append("Russia")

    