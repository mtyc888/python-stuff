ans = ''

while ans != 'quit':
    ans = input("add pizza toppings\n")
    
    if ans == 'quit':
        print('goodbye')
    else:
        print(f"{ans} added to the pizza")