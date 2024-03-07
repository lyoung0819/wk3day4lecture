from app.models import User

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None # If user is not logged in, then it will equal None. Once logged in, it will equal that instance 


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


    # Method to log a user in
    def log_user_in(self):
        # Ask the user for their creds 
        username_input = input('What is your username? ')
        password_input = input('What is your password? ')
        # Loop through the users in the blog user list 
        for user in self.users:
            # Check if the user's username matches the user input - same with password
            if user.username == username_input and user.check_password(password_input):
                # If both are True, set the blog's current user to that user
                self.current_user = user
                print(f"{user} has logged in.")
                # Once we find the right user, we don't need to to check other users so break
                break
        # if we go through the entire loop without breaking # AN ELSE AFTER A FOR WILL RUN IF THE FOR DOES NOT BREAK
        else: 
            # Then the user has bad creds
            print('Username and/or password is incorrect.')

    # Method to log a user out
    def log_user_out(self):
        username = self.current_user.username
        self.current_user = None
        print(f"{username} has been logged out.")

    