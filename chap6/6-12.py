cities = {
    'manhattan': {'country':'USA', 'fact':'good hotdog'},
    'new york': {'country':'USA', 'fact':'stinks of weed'},
    'boston':{'country':'USA', 'fact':'lobster'}
}

for key, value in cities.items():
    print(f"{key}, country: {value.get('country')} fact: {value.get('fact')}")

cities['shenzhen'] = {
    'country':'china',
    'fact':'hotpot'
}

for key, value in cities.items():
    print(f"{key}, country: {value.get('country')} fact: {value.get('fact')}")