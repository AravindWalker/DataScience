from TD import TelDirectory

print("These are the things you can do with telephone directory: ")
print("1. CREATE", "2. READ", "3. UPDATE", "4. DELETE", sep="\n")
ch = input("Enter what you need in telephone directory: ")
action = TelDirectory(ch)
