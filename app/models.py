

class User:
    id_counter = 1

    def __init__(self, username, password):
        self.id = User.id_counter
        User.id_counter += 1
        self.username = username
        self.__password = password #this will be a private variable, password attribute can only be accessed within the class.  

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}"
    
    def check_password(self, password_guess):
        return self.__password == password_guess
    

class Post:
    id_counter = 1

    def __init__(self, title, body, author):
        self.id = Post.id_counter
        Post.id_counter += 1
        self.title = title
        self.body = body
        self.author = author 

    def __str__(self):
        # Set up str to print the full post, opposed to the individual pieces(body, title, etc)
        return f"""
        {self.id} - {self.title} 
        By: {self.author}
        {self.body}
        """
    
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
