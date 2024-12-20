class Addressbook:

    def __init__(self):
        self.contacts=[]

    def add_contact(self,contact):  # add a new Contact
        self.contacts.append(contact)
        print("Contact Added SuccessFully!",contact)

    def edit_contact(self,firstname,updated_contact):  # edit existing contact
        for index,contact in enumerate(self.contacts):
            if contact.firstname == firstname:
                self.contacts[index]=updated_contact
                print("Contact Edited Successfully!",updated_contact)
 
    def delete_contact(self,firstname):  # delete existing contact
        for contact in self.contacts:
            if contact.firstname==firstname:
                self.contacts.remove(contact)
                print("Contact deleted Successfully!")
            else:
                print("Invalid Name!")

    def view_all_contact(self):
        print("All Contacts:")
        for contact in self.contacts:
            print(contact)