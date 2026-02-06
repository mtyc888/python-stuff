fav_numbers = {
    'p1':[1,2,44],
    'p2':[34,22,11],
    'p3':[56]
}

for key, value in fav_numbers.items():
    print(f"{key} likes:")
    for number in value:
        print(f'{number}')