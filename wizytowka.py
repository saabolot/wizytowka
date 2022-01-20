from faker import Faker


class card:
    def __init__(self, name, phone_number, address):
        self.name = None
        self.email = None
        self.phone_number = None


class BaseContact(card):
    def __init__(self, *args, **kwargs):
        super().__init__(self)
        self.phone_number = None

    def __contact__(self, phone_number, name):
        self.phone_number = phone_number
        print(f'Wybieram numer {phone_number} i dzwonię do {name}')


class BusinessContact(card):
    def __init__(self, job, company, email,  *args, **kwargs):
        super().__init__(self, job, company)
        self.phone_number = None

    def __contact__(self, phone_number, name):
        print(f'Wybieram numer {phone_number} i dzwonię do {name}')


fake = Faker(['pl_PL'])


person1 = BaseContact(fake)
