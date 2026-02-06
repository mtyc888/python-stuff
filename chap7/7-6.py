ans = ''
check = True
while ans != 'quit' and check:
    ans = input("add pizza toppings\n")
    
    if ans == 'quit':
        print('goodbye')
        check = False
    if ans == 'flag':
        check = False
        ans = 'quit'
    if ans == 'break':
        break
    else:
        print(f"{ans} added to the pizza")