import random
list_of_stuff = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
string = ""
for i in range(len(list_of_stuff)):
    random_num = random.randrange(0,len(list_of_stuff) - 1)
    string += str(list_of_stuff[random_num])
    
print(f"Lucky draw: {string}")