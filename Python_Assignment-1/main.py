from loginhelper import LoginHelp # import modules that has login/register supporting code
print("Enter 'Login' or 'Register'")
choice = input("Enter your choice: ")
mail_id = input("Enter the mail-ID: ")
user = LoginHelp(choice, mail_id) # initializing the LoginHelp class
user.control()
