current_users = ['user1', 'user2', 'user3', 'useR4', 'usEr5']
new_users = ['user4', 'user5', 'user6', 'user7', 'user8']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'{user} is used, pick another username')
    else:
        print(f'{user} is available')
