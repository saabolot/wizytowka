
class card:  
    #pass
    class card():
        def __init__(self, name, company, job, address, phone_number, email):
            self.name = None
            self.company = None
            self.job = None
            self.email = None
            self.phone_number = None
        class BaseContact(card):
            def __init__(self, phone_number, address):
                super().__init__(self, phone_number, address)
                self.phone_number = phone_number            
            def __contact__(self, phone_number, name):
                self.phone_number = phone_number  
                print(f'Wybieram numer {phone_number} i dzwonię do {name}')
        class BusinessContact(card):
            def __init__(self, phone_number, job, company):
                super().__init__(self, phone_number, job, company)
                self.phone_number = phone_number
            def __contact__(self, phone_number, name):
                print(f'Wybieram numer {phone_number} i dzwonię do {name}')
from faker import Faker
fake = Faker(['pl_PL'])


    
person1 = BaseContact(fake.address, fake.phone_number)

