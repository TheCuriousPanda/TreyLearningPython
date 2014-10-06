from User import User

def read_users():
    userslistfile = open('userslist.txt', 'r')
    userlist = []
    for userindex in range(1,3):
        temp_user_info = userslistfile.readline()
        temp_user_infolist = temp_user_info.split(' ')
        userlist.append(User(temp_user_infolist[0],temp_user_infolist[1],int(temp_user_infolist[2])))
    return userlist
   
def add_user(user):
    pass

    
def add_win(user):
    pass

    
def get_wins(user):
    pass
