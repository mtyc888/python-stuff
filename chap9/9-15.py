import random
list_of_stuff = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

runs = 0
my_ticket = ['a1b2', 'c3d4'] 

while True:
    string = ""
    for i in range(4):
        string += random.choice(list_of_stuff)
    
    runs += 1
    
    if string in my_ticket:
        break

print(f"Found it! Runs: {runs}")
print(f"Winning ticket: {string}")