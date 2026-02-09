from pathlib import Path

path = Path('guests_list.txt')
contents = input("What is your name?\n")
path.write_text(contents)
