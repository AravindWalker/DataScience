import pymongo


class TelDirectory:
    def __init__(self, ch):
        self.client = pymongo.MongoClient(
            "mongodb+srv://Aravind:8919072201@guvi-ds.6tybdko.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client.Telephone_directory
        self.records = self.db.Contact_list
        self.ch = ch.lower()
        self.choice()

    def choice(self):
        if self.ch == "create":
            self.create()
        elif self.ch == "read":
            self.read()
        elif self.ch == "update":
            self.update()
        else:
            self.delete()

    def create(self):
        print("Please enter the mentioned details: ")
        self.fields = ["Name", "Phone_number", "Place"]
        self.name = input("Enter the name: ")
        self.phone = input("Enter the no: ")
        self.place = input("Enter the place: ")
        self.dict_list = dict(zip(self.fields, [self.name, self.phone, self.place]))
        self.records.insert_one(self.dict_list)
        print("New contact added to contact list")

    def contact_list(self):
        print('CONTACT LIST -->')
        self.j = 1
        for i in self.records.find({}, {"_id": 0, "Name": 1}):
            print(f"{self.j}", ".", f"{i['Name']}")
            self.j += 1

    def read(self):
        self.contact_list()
        self.nm = input("For which name of the contact, details need to be displayed: ")
        for i in self.records.find({"Name": self.nm}, {"_id": 0}):
            print(f"The contact name is {i['Name']}")
            print(f"The contact number is {i['Phone_number']}")
            print(f"The contact place is {i['Place']}")

    def update(self):
        self.contact_list()
        self.sv = input("For which name of the contact, data needs to be updated: ")
        print('FIELDS -->')
        print("1. Name", "2. Phone_number", "3. Place", sep="\n")
        self.count = int(input("Enter the no. of fields that needs to be updated: "))
        if self.count == 3:
            self.f = ["Name", "Phone_number", "Place"]
        else:
            self.f = []
            for i in range(self.count):
                self.f.append(input(f"Enter the {i + 1}st field that needs to be updated: "))
        for i in self.f:
            self.new = input(f"Enter the new {i} :")
            if i == "Name":
                self.records.update_one({"Name": self.sv}, {"$set": {i: self.new}})
                self.sv = self.new
            else:
                self.records.update_one({"Name": self.sv}, {"$set": {i: self.new}})
            print(f"{i} is updated")

    def delete(self):
        self.contact_list()
        self.d_nm = input("Which name contact needs to be deleted: ")
        self.records.delete_one({"Name": self.d_nm})
        print(f"{self.d_nm} contact is deleted")
