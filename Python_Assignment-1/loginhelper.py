import json,string
class LoginHelp:
    def __init__(self, choice, mailid):

        self.choice = choice
        self.mailid = mailid
        self.user_data = self.read_user_data()

    def read_user_data(self): # getting user data from database

        with open("database.txt","r") as fin:
            return json.loads(fin.read() or "{}")

    def control(self): # function for selecting register or login

        self.register() if self.choice.lower() == "register" else self.login()

    def register(self): # register logic code

        while not (self.mail_valid()): # checking mail is in format or not
            print("Mail ID is not in correct format, Enter a new mail ID")
            self.mailid = input("Enter the new mail-ID: ")

        while not (self.mail_not_exist()): # checking if mail already available in database or not
            print("Mail ID already exists, Enter a new mail ID")
            self.mailid = input("Enter the new mail-ID: ")

        self.password=input("Enter a password: ")

        while not (self.pass_auth()): # chekcing password is in format or not
            print("Password is not in correct format, Create a password again")
            self.password=input("Enter a new password: ")

        self.user_data[self.mailid] = self.password
        self.wite_to_database() # updating database with user input
        print("ACCOUNT CREATED SUCCESSFULLY")

    def wite_to_database(self): # updating database with user input

        with open("database.txt", "w") as fin:
            json.dump(self.user_data, fin)
    def login(self): # login code logic

        for_login=1
        login_count = 3
        while self.mail_not_exist():
            print("MAIL-ID DOES NOT EXIST",end="\n")
            print("If you want to create a new one go for registering or enter the mail ID Again",end="\n")
            print("'Register' for Registering or 'Try' for login again")
            ch=input()
            self.mailid = input("Enter the mail-ID: ")
            if ch.lower()=="register":
                self.register()
                for_login=0
                break
            else:
                pass

        if for_login==1:
            self.password=input("Enter the password: ")
            if self.check_login():
                print("LOGIN SUCCESSFUL")
            else:
                print("PASSWORD IS INCORRECT")
                x=input("Do you want to reset the password(Y/N): ") # resetting password
                if x.lower()=="y":
                    self.password=input("Enter a new password: ")
                    if self.pass_auth():
                        self.user_data[self.mailid] = self.password
                        self.wite_to_database()
                        print("PASSWORD RESET IS SUCCESSFUL, TRY LOGIN AGAIN")
                    else:print("INVALID PASSWORD FORMAT")
                else:
                    while login_count >0 :
                        if not self.check_login():
                            print(f"You can have {login_count} more attempts to check password")
                            self.password=input("Enter a new password: ")
                            login_count-=1
                        else:
                            print("Login Successful")
                            break
                    else:
                        if not self.check_login():
                            print("Try to reset password")
                        else:
                            print("LOGIN SUCCESSFUL")
        else:
            pass

    def check_login(self):

        if self.password == self.user_data[self.mailid]:
            return True
        else: return False

    def mail_valid(self): # checking mail is in format or not

        if "@" in self.mailid and self.mailid[0].isalpha():  # checking mail valid or not
            if self.mailid[self.mailid.index("@") + 1] != '.':  # checking mail valid or not
                return True
            else:return False
        else:return False

    def mail_not_exist(self): # checking if mail already available in database or not

        if self.mailid not in self.user_data:
            return True
        else:return False

    def pass_auth(self): # checking password is in format or not

        pass_set=set(self.password)
        if len(self.password)>=8 and len(self.password)<=16:
            if pass_set.intersection(set(string.ascii_uppercase)) and \
                    pass_set.intersection(set(string.ascii_lowercase)) and \
                    pass_set.intersection(set(string.digits)) and \
                    pass_set.intersection(set(string.punctuation)) :
                return True
            else:return False
        else:return False
