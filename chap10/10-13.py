from pathlib import Path
import json

def greet_user():
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
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

greet_user()
