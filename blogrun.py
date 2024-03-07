from app import Blog

# Run the blog!
def run_blog():
    print('Welcome to the Kekambas Blog!')
    # Create instance of Blog class
    blog = Blog()
    #start running our blog until user quits
    while True:
        if blog.current_user is None:
            # Print logged out menu options
            print(f"1. Sign Up\n2. Login\n3. View All Posts\n4. View Single Posts\n5. Quit")
            # Ask the user what they want to do
            to_do = input('Which option would you like to do?')
            # Make sure they give a valid option 
            while to_do not in {'1','2','3','4','5'}:
                to_do = input('Inavlid option. Please enter 1, 2, 3, 4, or 5: ') # Re-define the to_do variable 
            # Different routes/options
            if  to_do == '5':
                break
            elif to_do == '1':
                # Call create new user method on the blog
                blog.create_new_user()
            elif to_do == '2':
                # Call log in method on the blog
                blog.log_user_in() 
            else:
                print(f'Option {to_do} is coming soon.')
        else:
            # Print the menu for logged in users
            print('1. Sign Out')
            to_do = input('Which option would you like to do? ')
            if to_do == '1':
                blog.log_user_out()
    # Once the user quits and while loop breaks
    print('Thank you for checking out the blog!')
    print(blog.users)
    print(blog.posts)

run_blog()