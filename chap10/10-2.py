from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(line)

strings = []

for line in lines:
    sen = line.replace('python', 'C++')
    strings.append(sen)

print(strings)