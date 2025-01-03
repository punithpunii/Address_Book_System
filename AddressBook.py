import json
from contact import Contact
class Addressbook:

    def __init__(self):
        self.contacts={}

    def add_contact(self,contact,firstname):  # add a new Contact
        if firstname in self.contacts: # UC-7 there is no Duplicate Entry of the same Person in a particular Address Book
                print(f"Contact with {firstname} already exists!")
        else:
            self.contacts[firstname]=contact
            print("Contact Added SuccessFully!",contact)
            
    def edit_contact(self,firstname,updated_contact):  # edit existing contact
        if firstname in self.contacts:
            self.contacts[firstname]=updated_contact
            print("Contact Edited Successfully!",updated_contact)
        else:
            print(f"Contact with {firstname} Not found!")
 
    def delete_contact(self,firstname):  # delete existing contact
        if firstname in self.contacts:
            del self.contacts[firstname]
            print("Contact deleted Successfully!")
        else:
            print("Invalid Name!")

    def view_all_contact(self):  # view all the existing contact
        print("All Contacts:")
        for name,values in self.contacts.items():
            if isinstance(values,Contact):
                print(f"{name}: {values}")

    def name_sorted(self): # UC-11 sort the entries in the address book alphabetically by Person’s name
        sorted_dict=dict(sorted(self.contacts.items()))
        for name,values in sorted_dict.items():
            print(f"{name}: {values}")

    def sort_city(self,sort_value): # UC-12 Ability to sort the entries in the address book by City, State, or Zip 
        print(f"The contacts in {sort_value} are:")
        for name,contact in self.contacts.items():
            if contact.city==sort_value:
                print(contact)
            elif contact.state==sort_value:
                print(contact)
            elif contact.zip==sort_value:
                print(contact)

    def save_to_file(self,file_name): # UC-13 Ability to Read or Write the Address Book
        try:
            with open(file_name,"w") as file:
                json.dump({firstname:contact.__dict__ for firstname,contact in self.contacts.items()},file,indent=4)
                print(f"Address book saved to {file_name}")
        except Exception as e:
            print(f"Error saving address book: {e}")
        
    def load_from_file(self,file_name): # UC-13 Ability to Read or Write the Address Book
        try:
            with open(file_name,"r") as file:
                data=json.load(file)
                self.contacts={firstname:Contact(**details) for firstname, details in data.items()}
            print(f"Address book loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found!")
        except Exception as e:
            print(f"Error loading address book: {e}")