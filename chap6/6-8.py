p_dict1 = {
    "animal type":"cat",
    "owner":"tiffany"
}
p_dict2 = {
    "animal type":"dog",
    "owner":"bill"
}
p_dict3 = {
    "animal type":"mouse",
    "owner":"koko"
}
p_dict4 = {
    "animal type":"dragon",
    "owner":"emperor"
}
p_dict5 = {
    "animal type":"lion",
    "owner":"richard"
}

pets = []

pets.append(p_dict1)
pets.append(p_dict2)
pets.append(p_dict3)
pets.append(p_dict4)
pets.append(p_dict5)

for ppl in pets:
    print(f"{ppl.get("animal type")} owned by {ppl.get("owner")}")