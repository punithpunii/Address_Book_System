from contact import Contact
from AddressBook import Addressbook

class AddressBookMain:
    def __init__(self):
        self.Ab=Addressbook()
        
    def display_menu(self):
        print("Welcome to Address Book Program")
        
add1=AddressBookMain()
add1.display_menu()

