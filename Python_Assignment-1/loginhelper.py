import json,string
class LoginHelp:
    def __init__(self, choice, mailid):
        self.choice = choice
        self.mailid = mailid
        self.user_data = self.read_user_data()
    def read_user_data(self):
        with open("database.txt","r") as fin:
            return json.loads(fin.read() or "{}")
    def control(self):
        self.register() if self.choice.lower() == "register" else self.login()
    def register(self):
        if self.mail_valid():
            if self.mail_exist():
                self.password=input("Enter a password: ")
                if self.pass_auth():
                    self.user_data[self.mailid] = self.password
                    self.wite_to_database()
                    print("ACCOUNT CREATED SUCCESSFULLY")
                else:print("INVALID PASSWORD FORMAT")
            else:print("MAIL-ID ALREADY EXIST'S")
        else:print("INVALID MAIL FORMAT")
    def wite_to_database(self):
        with open("database.txt", "w") as fin:
            json.dump(self.user_data, fin)
    def login(self):
        if not self.mail_exist():
            self.password=input("Enter the password: ")
            if self.password == self.user_data[self.mailid]:
                print("LOGIN SUCCESSFUL")
            else:
                print("PASSWORD IS INCORRECT")
                x=input("Do you want to reset the password(Y/N): ")
                if x=="Y":
                    self.password=input("Enter a new password: ")
                    if self.pass_auth():
                        self.user_data[self.mailid] = self.password
                        self.wite_to_database()
                        print("PASSWORD RESET IS SUCCESSFUL, TRY LOGIN AGAIN")
                    else:print("INVALID PASSWORD FORMAT")
                else:
                    print("TRY TO LOGIN AGAIN")
        else:
            print("MAIL-ID DOES NOT EXIST")
    def mail_valid(self):
        if "@" in self.mailid and self.mailid[0].isalpha():  # checking mail valid or not
            if self.mailid[self.mailid.index("@") + 1] != '.':  # checking mail valid or not
                return True
            else:return False
        else:return False
    def mail_exist(self):
        if self.mailid not in self.user_data:
            return True
        else:return False
    def pass_auth(self):
        pass_set=set(self.password)
        if len(self.password)>=8:
            if pass_set.intersection(set(string.ascii_uppercase)) and \
                pass_set.intersection(set(string.ascii_lowercase)) and \
                 pass_set.intersection(set(string.digits)) and \
                  pass_set.intersection(set(string.punctuation)) :
                return True
            else:return False
        else:return False