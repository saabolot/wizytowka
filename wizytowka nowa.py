from faker import Faker

fake = Faker(['pl_PL'])


class Card:
    def __init__(self, first_name, last_name, phone_number, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
    
        #Variables
        self._label_length = 0


class BaseCard(Card):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  

    def contact():
        print(f"Kontaktuję się z {fake.first_name()} {fake.last_name()} e-mail: {fake.email()}")

    @property
    def label_length(self):
        self._label_length = len({self.first_name}+" "+{self.last_name})
        return self._label_length


class BussinessCard(Card):
    def __init__(self, job, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jon = job
        self.company = company

    def contact():
        print(f"Kontaktuję się z {fake.first_name()} {fake.last_name()} e-mail: {fake.email()}")


    @property
    def label_length(self):
        self._label_length = len({self.first_name}+" "+{self.last_name})
        return self._label_length

"""
    def fejk(self):
        print(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address(), fake.email())
"""    



def create_contacts(rodzaj, ilosc):
    for i in range(ilosc):
        if rodzaj == BaseCard:
            print()
        elif rodzaj == BussinessCard:
            print()
        else:
            print("zły rodzaj wizytówki")

create_contacts(BussinessCard, 5)