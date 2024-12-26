from contact import Contact
from AddressBook import Addressbook

#UC6 - add multiple Address Book to the System. Each Address Book has a unique Name
class AddressBookMain:
    def __init__(self):
        self.address_book_sytem={}

    def display_addressbook_menu(self):
        print("Welcome to Address Book Program")
        while True:
            choice=int(input("1. Create New AddressBook\n2. Manage Existing AddressBook\n3. Delete Existing AddressBook\n4. View all the AddressBook\nEnter your choice:"))
            if choice==1:
                name=input("Enter the name of AddressBook to be created:")
                self.check_add_addbook(name)

            elif choice==2:
                name=input("Enter the name of AddressBook to be Managed:")
                if name in self.address_book_sytem:
                    self.display_menu(name)
                else:
                    print(f"AddressBook with {name} not found")

            elif choice==3:
                name=input("Enter the name of AddressBook to be Deleted:")
                self.del_addbook(name)

            elif choice==4:
                for addbook in self.address_book_sytem:
                    print(addbook)
            else:
                print("Invalid Choice")
                break

    def check_add_addbook(self,name): # add multiple Address Book to the System
        if name in self.address_book_sytem:
            print(f"AddressBook with {name} already Exists")
            return
        else:
            address_book=Addressbook()
            self.address_book_sytem[name]=address_book
            print("New AddressBook Created Successfully")

    def del_addbook(self,name):
        if name in self.address_book_sytem:
            del self.address_book_sytem[name]
            print(f"AddressBook {name} Deleted Successfully")
            return
        else:
            print(f"AddressBook {name} not found")

        
    def display_menu(self,name):
        if name in self.address_book_sytem:

            while True:  # add multiple person
                choice=int(input("1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. View Contacts\n5. Return to Main Menu\nEnter your choice:"))
                if choice==1:
                    self.add_contact_console(name,self.address_book_sytem[name])
                elif choice==2:
                    self.edit_contact_console(name,self.address_book_sytem[name])
                elif choice==3:
                    self.delete_contact_console(name,self.address_book_sytem[name])
                elif choice==4:
                    self.view_all_contact_console(self.address_book_sytem[name])
                elif choice==5:
                    break

    def add_contact_console(self,addbook_name,addbook):  # add a new Contact
        print("Enter the details:")
        firstname=input("FirstName:")
        lastname=input("LastName:")
        address=input("Address:")
        city=input("City:")
        state=input("State:")
        zip=input("Zip:")
        phonenumber=input("Phone_Num:")
        email=input("E-mail:")

        new_contact=Contact(firstname,lastname,address,city,state,zip,phonenumber,email)

    def edit_contact_console(self,addbook_name,addbook):  # edit Contact
        firstname = input("Enter the First name of Contact to be edited:")
        lastname=input("LastName:")
        address=input("Address:")
        city=input("City:")
        state=input("State:")
        zip=input("Zip:")
        phonenumber=input("Phone_Num:")
        email=input("E-mail:")

        updated_contact=Contact(firstname,lastname,address,city,state,zip,phonenumber,email)

    def delete_contact_console(self,addbook_name,addbook):  # delete existing contact
        firstname = input("Enter the First name of Contact to be Deleted:")
        if isinstance(addbook,Addressbook):
            addbook.delete_contact(firstname)
        
    def view_all_contact_console(self,add_obj):
        if isinstance(add_obj,Addressbook):
            add_obj.view_all_contact()

    

add1=AddressBookMain()
add1.display_addressbook_menu()

