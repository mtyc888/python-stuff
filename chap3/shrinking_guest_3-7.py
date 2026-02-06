people = ['pp1', 'pp2', 'pp3']

for person in people:
    print(f'{person} are invited to dinner')
    
print(f"{people[0]} can't make it")

print(f"inviting 'bill'")

people.insert(0,'bill')

for person in people:
    print(f'{person} are invited to dinner')
    
print("more guest")

people.insert(0, '1st guest')

people.insert(int(len(people)/2), 'middle guest')

people.insert(len(people), 'last guest')

for person in people:
    print(f'{person} are invited to dinner')
    
print("I can only invite 2 guests")

while len(people) > 2:
    name = people.pop()
    print(f"{name} kicked out")
        
for person in people:
    print(f'{person} are still invited to dinner')
    
del people[0]

del people[0]

print(people)