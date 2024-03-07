

class User:
    id_counter = 1

    def __init__(self, username, password):
        self.id = User.id_counter
        User.id_counter += 1
        self.username = username
        self.__password = password #this will be a private variable, password attribute can only be accessed within the class. We want to hide this 

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}"
    
    def check_password(self, password_guess):
        return self.__password == password_guess
    
u = User('brians', '123abc')

print(u.check_password('123abc'))
print(u.check_password('abc123'))

print(u.__password)