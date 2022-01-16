from faker import Faker
fake = Faker(['pl_PL'])
for i in range(10):
    
    
    class card():
        def __init__(self, name, company, job, email):
            self.name = fake.name
            self.company = fake.company
            self.job = fake.job
            self.email = fake.email
    #print(fake.name(), fake.company(),fake.job(),fake.email())
        class BaseContact(card):
            def __init__(self, phone_number, *args):
                self.phone_number = fake.phone_number
            def __contact__(self):
                print(f'Wybieram numer {fake.phone_number} i dzwonię do {fake.name}')
        class BusinessContact(card):
            def __init__(self, phone_number, *args):
                self.phone_number = fake.phone_number
            def __contact__(self):
                print(f'Wybieram numer {fake.phone_number} i dzwonię do {fake.name}')
#print(card) 



