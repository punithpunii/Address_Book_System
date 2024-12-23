from contact import Contact
from AddressBook import Addressbook

#UC2 - add a new Contact to Address Book

class AddressBookMain:
    def __init__(self):
        self.address_book=Addressbook()
        
    def display_menu(self):
        print("Welcome to Address Book Program")
        while True:
            choice=int(input("1. Add Contact:"))
            if choice==1:
                self.add_contact_console()

    def add_contact_console(self):  # add a new Contact
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
        self.Ab.add_contact(new_contact)         
    
        
add1=AddressBookMain()
add1.display_menu()

