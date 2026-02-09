from pathlib import Path

path = Path('guest_book.txt')
guest_list = []
guest_string = ""
while True:
    user_input = input("What is your name (enter 1 to exit)\n")
    if user_input == "1":
        break
    guest_list.append(user_input)

for guest in guest_list:
    guest_string += guest + "\n"

path.write_text(guest_string)