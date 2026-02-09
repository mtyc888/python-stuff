from pathlib import Path
import json

def get_fav_num():
    fav_num = input("What is your favourite number?\n")
    check = check_num(fav_num)
    if check == False:
        path = Path('fav_num.txt')
        content = json.dumps(fav_num)
        path.write_text(content)
    else:
        print("number already exist")

def check_num(fav_num):
    path = Path('fav_num.txt')
    lines = path.read_text()
    check = False
    for line in lines:
        if line == fav_num:
            check = True
            break
    return check

def read_fav_num():
    path = Path('fav_num.txt')
    lines = path.read_text()
    print(f"I know your fav number! It's {lines}")

get_fav_num()
read_fav_num()