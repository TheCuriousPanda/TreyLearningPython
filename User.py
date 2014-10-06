class User:
    def __init__(self, name, password, wins):
        self.__name=name
        self.__password=password
        self.__wins=wins

    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password

    def get_wins(self):
        return self.__wins
