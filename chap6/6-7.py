person = {
    "fname":"marvin",
    "lname":"tan",
    "age":"26",
    "city":"penang"
}

person2 = {
    "fname":"syasya",
    "lname":"tan",
    "age":"25",
    "city":"brunei"
}

person3 = {
    "fname":"mimi",
    "lname":"tan",
    "age":"2",
    "city":"brunei"
}

list_ppl = []

list_ppl.append(person)
list_ppl.append(person2)
list_ppl.append(person3)

for ppl in list_ppl:
    print(f" firstname: {ppl.get('fname')} \n lastname: {ppl.get('lname')} \n age: {ppl.get('age')} \n city:{ppl.get('city')} \n\n")