print('Choose "Register" or "Login"')
choice=input("Enter your choice: ")
opt1="Register"
opt2="Login" # need to write case for 1st input as login bcz data will be empty
if choice==opt1:
  mail_id=input("Enter the mailid: ")
  if "@" in mail_id and mail_id[0].isalpha(): #checking mail valid or not
    if mail_id[mail_id.index("@")+1]!='.':  #checking mail valid or not
      password=input("Enter the password: ")
      if 5<len(password)<16: # checking only one condition for password need to update others
        with open("database.txt","a") as x:   #Writing data to file
          x.write(mail_id+":")
          x.write(password+"\n")
      else:
        print("Wrong password format")
    else:
      print("Wrong mail format")
  else:
    print("Wrong mail format")
else:
  with open("database.txt", "r") as x:
    a = x.readlines()  # changing file data to list
    b=a.copy()
    a = [i.strip("\n") for i in a] # removing newline character
  print("PROVIDE THE LOGIN CREDENTIALS ")
  login=input("Enter the mailid: ")
  count=0
  for j,i in enumerate(a):
    key = i.index(":")
    if login==i[:key]:
      pswrd=input("Enter the password: ")
      if pswrd==i[key+1 :]:
        print("LOGIN SUCCESSFUL")
        count=1
        break
      else:
        count=1
        print("password is wrong")
        deci=input("Want to reset password (Y/N): ")
        if deci=="Y":
          reset_pswrd=input("enter new password: ")
          b[j]=i[:key]+":"+reset_pswrd+"\n"
          with open("database.txt","w") as x:
            x.writelines(b)
          print("PASSWORD UPDATED SUCCESFULLY")
          print("LOGIN AGAIN!!")
        else:
          print("Kindly login again or register")
  if count==0:
    print("user id not available go for registering")