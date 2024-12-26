from contact import Contact
from AddressBook import Addressbook

# UC-11 sort the entries in the address book alphabetically by Person’s name
class AddressBookMain:
    def __init__(self):
        self.address_book_sytem={}
        self.state_dict={}  # UC-9 Ability to view Persons by State
        self.city_dict={}   # UC-9 Ability to view Persons by City

    def display_addressbook_menu(self):
        print("Welcome to Address Book Program")
        while True:
            choice=int(input("1. Create New AddressBook\n2. Manage Existing AddressBook\n3. Delete Existing AddressBook\n4. View all the AddressBook\n5. Search by city or state\n6. Count no of persons\nEnter your choice:"))
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
            elif choice==5:
                self.search_city_state()
            elif choice==6:
                self.count_city_state()
            else:
                print("Invalid Choice")
                break

    def check_add_addbook(self,name):
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
            self.remove_city_dict(name)
            self.remove_state_dict(name)
            print(f"AddressBook {name} Deleted Successfully")
            return
        else:
            print(f"AddressBook {name} not found")

        
    def display_menu(self,name):
        if name in self.address_book_sytem:

            while True:  # add multiple person
                choice=int(input("1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. View Contacts\n5. Sorted order of Contacts\n6. Return to Main Menu\nEnter your choice:"))
                if choice==1:
                    self.add_contact_console(name,self.address_book_sytem[name])
                elif choice==2:
                    self.edit_contact_console(name,self.address_book_sytem[name])
                elif choice==3:
                    self.delete_contact_console(name,self.address_book_sytem[name])
                elif choice==4:
                    self.view_all_contact_console(self.address_book_sytem[name])
                elif choice==5:
                    self.name_sorted(self.address_book_sytem[name])
                elif choice==6:
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
        if isinstance(addbook, Addressbook):
            addbook.add_contact(new_contact,firstname)
            self.update_city_dict(new_contact.firstname,new_contact.city,addbook_name)
            self.update_state_dict(new_contact.firstname,new_contact.state,addbook_name)

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
        if isinstance(addbook,Addressbook):
            addbook.edit_contact(firstname,updated_contact) 
            self.update_city_dict(updated_contact.firstname,updated_contact.city,addbook_name)
            self.update_state_dict(updated_contact.firstname,updated_contact.state,addbook_name)

    def delete_contact_console(self,addbook_name,addbook):  # delete existing contact
        firstname = input("Enter the First name of Contact to be Deleted:")
        if isinstance(addbook,Addressbook):
            addbook.delete_contact(firstname)
            self.remove_city_dict(firstname,addbook_name)
            self.remove_state_dict(firstname,addbook_name)

    def view_all_contact_console(self,add_obj):
        if isinstance(add_obj,Addressbook):
            add_obj.view_all_contact()

    def update_city_dict(self,contact_name,city_name,addbook_name):
        for city,contact_names in self.city_dict.items():
            for contact_list in contact_names:
                if contact_list[0]==contact_name and contact_list[1]==addbook_name:
                    contact_names.remove(contact_list)

        cities_to_remove=[city for city in self.city_dict if self.city_dict[city]==[]]
        for city in cities_to_remove:  
                del self.city_dict[city]
            
        if city_name not in self.city_dict:
                self.city_dict[city_name] = []
        self.city_dict[city_name].append([contact_name,addbook_name])
        print(self.city_dict)

    def update_state_dict(self,contact_name,state_name,addbook_name):
        for state,contact_names in self.state_dict.items():
            for contact_list in contact_names:
                if contact_list[0]==contact_name and contact_list[1]==addbook_name:
                    contact_names.remove(contact_list)

        states_to_remove=[state for state in self.state_dict if self.state_dict[state]==[]]
        for state in states_to_remove:  
                del self.state_dict[state]
            
        if state_name not in self.state_dict:
                self.state_dict[state_name] = []
        self.state_dict[state_name].append([contact_name,addbook_name])
        print(self.state_dict)

    def remove_city_dict(self,firstname,addbook_name):
        for city,contact_names in self.city_dict.items():
            for contact_list in contact_names:
                if contact_list[0]==firstname and contact_list[1]==addbook_name:
                    contact_names.remove(contact_list)
            
        cities_to_remove=[city for city in self.city_dict if self.city_dict[city]==[]]
        for city in cities_to_remove:  
                del self.city_dict[city]
        print(self.city_dict)

    def remove_city_dict(self,addbook_name):
        for city,contact_names in self.city_dict.items():
            for contact_list in contact_names:
                if contact_list[1]==addbook_name:
                    contact_names.remove(contact_list)

    def remove_state_dict(self,firstname,addbook_name):
        for city,contact_names in self.state_dict.items():
            for contact_list in contact_names:
                if contact_list[0]==firstname and contact_list[1]==addbook_name:
                    contact_names.remove(contact_list)
            
        states_to_remove=[state for state in self.state_dict if self.state_dict[state]==[]]
        for state in states_to_remove:  
                del self.state_dict[state]
        print(self.state_dict)

    def remove_state_dict(self,addbook_name):
        for city,contact_names in self.state_dict.items():
            for contact_list in contact_names:
                if contact_list[1]==addbook_name:
                    contact_names.remove(contact_list)

    def search_city_state(self): # UC-8 Ability to search Person in a City or State
        choice=int(input("1. Search by city\n2. Search by State\nEnter your choice:"))
        if choice==1:
            city_name=input("Enter the name of city:")
            if city_name in self.city_dict:
                print(self.city_dict[city_name])
            else:
                print(f"no contacts in {city_name}")
        elif choice==2:
            state_name=input("Enter the name of state:")
            if state_name in self.state_dict:
                print(self.state_dict[state_name])
            else:
                print(f"no contacts in {state_name}")
        else:
            return
    
    def count_city_state(self): # UC-10 Ability to get number of contact by City or State
        choice=int(input("1. Count persons in city\n2. Count persons in State\nEnter your choice:"))
        if choice==1:
            city_name=input("Enter the name of city:")
            if city_name in self.city_dict:
                count=0
                for city,contacts in self.city_dict.items():
                    if city==city_name:
                        for contact in contacts:
                            count+=1
                print(f"No of contacts in {city_name} is {count}")
            else:
                print(f"no contacts in {city_name}")
        
        elif choice==2:
            state_name=input("Enter the name of State:")
            if state_name in self.state_dict:
                count=0
                for state,contacts in self.state_dict.items():
                    if state==state_name:
                        for contact in contacts:
                            count+=1
                print(f"No of contacts in {state_name} is {count}")
            else:
                print(f"no contacts in {state_name}")

    def name_sorted(self,addbook): # UC-11 sort the entries in the address book alphabetically by Person’s name
        if isinstance(addbook,Addressbook):
            addbook.name_sorted()
add1=AddressBookMain()
add1.display_addressbook_menu()
