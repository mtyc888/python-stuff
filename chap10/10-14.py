from pathlib import Path
import json

def get_stored_username(path):
    contents = path.read_text()
    username = json.loads(contents)
    return username

def get_new_username(path):
    username = input('What is your name? \n')
    age = input('what is your age?\n')
    hobby = input('what is your hobby?\n')
    user_dict = {
        'user':{
            'username': username,
            'age': age,
            'hobby': hobby
        }
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    print(f"We'll remember your when you come back, {username}")

def greet_user():
    path = Path('username.json')
    if path.exists():
        username = get_stored_username(path)
        q1 = input(f'is {username} your username? \n (y/n)')
        if q1 == 'y':
            print(f'Welcome back {username}')
        else:
            get_new_username(path)
    else:
        get_new_username(path)

greet_user()
