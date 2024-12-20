from contact import Contact
from AddressBook import Addressbook

#UC5 - add multiple person to Address Book
class AddressBookMain:
    def __init__(self):
        self.address_book=Addressbook()
        
    def display_menu(self):
        print("Welcome to Address Book Program")
        while True:  # add multiple person
            choice=int(input("1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. View Contacts\nEnter your choice:"))
            if choice==1:
                self.add_contact_console()
            elif choice==2:
                self.edit_contact_console()
            elif choice==3:
                self.delete_contact_console()
            elif choice==4:
                self.address_book.view_all_contact()
            else:
                print("Invalid choice:")
                break

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

    def edit_contact_console(self):  # edit Contact
        firstname = input("Enter the First name of Contact to be edited:")
        lastname=input("LastName:")
        address=input("Address:")
        city=input("City:")
        state=input("State:")
        zip=input("Zip:")
        phonenumber=input("Phone_Num:")
        email=input("E-mail:")

        updated_contact=Contact(firstname,lastname,address,city,state,zip,phonenumber,email)
        self.Ab.edit_contact(firstname,updated_contact)        

    def delete_contact_console(self):  # delete existing contact
        firstname = input("Enter the First name of Contact to be Deleted:")
        self.Ab.delete_contact(firstname)

add1=AddressBookMain()
add1.display_menu()

