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