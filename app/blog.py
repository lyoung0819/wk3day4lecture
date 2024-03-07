from app.models import User

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []


    # Method to create a new user instance and add to the Blog's user list 
    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check to see if this username exists already
        if username in {u.username for u in self.users}: # set comprehension 
            print(f'User with username {username} already exists.')
        else:
            password = input('Please enter a password: ')
            # Create an instance of User class (now that we have a username and password) ^ import app.models import User
            new_user = User(username, password)
            # Add the new instance of the user to the blog's user list
            self.users.append(new_user)
            print(f"{new_user} has been created.")