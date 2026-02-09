from pathlib import Path
import json

def get_fav_num():
    fav_num = input("What is your favourite number?\n")
    path = Path('fav_num.txt')
    content = json.dumps(fav_num)
    path.write_text(content)

def read_fav_num():
    path = Path('fav_num.txt')
    lines = path.read_text()
    print(f"I know your fav number! It's {lines}")

get_fav_num()
read_fav_num()