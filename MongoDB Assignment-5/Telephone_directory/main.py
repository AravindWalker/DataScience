from TD import TelDirectory

serv_id = input("Please enter telephone server that you need to connect: ")
print("These are the things you can do with telephone directory: ")

opts = ["Create", "Read", "Update", "Delete"]

for i, j in enumerate(opts):
    print(i + 1, ". ", j)

check = 0

while check == 0:
    ch = input("Enter what you need in telephone directory: ")
    if ch in opts:
        check = 1
    else:
        print("Please select the above mentioned options")

action = TelDirectory(serv_id, ch)
