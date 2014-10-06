import UserFileEditor
users = UserFileEditor.read_users()
usernames = []
for user in users:
    usernames.append(user.get_name())
username=input("Please enter your username")
wins=input("Please enter record")
record = users[usernames.index(usernames)].get_wins
if (wins=record):
    print(record)
