from faker import Faker
fake = Faker(['pl_PL'])


class Card:
    def __init__(self, first_name, last_name, phone_number, address, email):
        self.first_name = None
        self.last_name = None
        self.phone_number = None
        self.address = None
        self.email = None

        #Variables
        self._label_length = len(first_name) + len(last_name)
    
class BaseContact(Card):
    def __init__(self, *args, **kwargs):
        super().__init__(self)
        
    def __contact__(self):
        print(f'Wybieram numer {phone_number} i dzwonię do {first_name} {last_name}')
    
    @property
    def label_length(self):
        return self.label_length

class BusinessContact(Card):
    def __init__(self, job, company, email,  *args, **kwargs):
        super().__init__(self, job, company)
        self.phone_number = None

    def __contact__(self, phone_number, first_name, last_name):
        print(f'Wybieram numer {phone_number} i dzwonię do {first_name} {last_name}')


person1 = BaseContact
