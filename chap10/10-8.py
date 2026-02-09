from pathlib import Path

try:
    pathCats = Path('cats.txt')
    pathDogs = Path('dogs.txt')
    catnames = pathCats.read_text()
    dognames = pathDogs.read_text()
    for name in catnames.splitlines():
        print(name)
    for name in dognames.splitlines():
        print(name)
except FileNotFoundError:
    print("File is missing.")


