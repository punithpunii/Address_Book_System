class Contact:
    def __init__(self, firstname, lastname, address, city, state, zip, phonenumber, email):
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phonenumber=phonenumber
        self.email=email

    def __str__(self):  #UC1 create a Contacts in Address Book

        return f"{self.firstname},{self.lastname}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.phonenumber}, {self.email}"
    
