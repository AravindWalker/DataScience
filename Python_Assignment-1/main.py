from loginhelper import LoginHelp
print("Enter 'Login' or 'Register'")
choice = input("Enter your choice: ")
mail_id = input("Enter the mail-ID: ")
user = LoginHelp(choice, mail_id)
user.control()