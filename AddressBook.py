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
