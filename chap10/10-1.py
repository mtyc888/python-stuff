from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(line)

strings = []

for line in lines:
    strings.append(line)

print(strings)