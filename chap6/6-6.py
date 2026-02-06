favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

list_of_ppl = ['jen', 'marvin', 'edward']

for ppl in list_of_ppl:
    if ppl in favorite_languages:
        print(f"Thank you {ppl} for taking the poll")
    else:
        print(f"{ppl} please take the poll")
