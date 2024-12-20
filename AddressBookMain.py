#UC1 create a Contacts in Address Book

from contact import Contact
from AddressBook import Addressbook

class AddressBookMain:
    def __init__(self):
        self.address_book=Addressbook()
        
    def display_menu(self):
        print("Welcome to Address Book Program")
        while True:
            choice=int(input("1. Add Contact:"))
            if choice==1:
                contact1 = Contact("Punith", "M", "HSR", "Bangalore", "KA", "560100", "9830903020", "punith@gmail.com")
                self.address_book.add_contact(contact1)
    
        
add1=AddressBookMain()
add1.display_menu()

