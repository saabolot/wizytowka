


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

    def contact(self):
        print(f"Kontaktuję się z {self.first_name()} {self.last_name()} e-mail: {self.email()}")

    @property
    def label_length(self):
        self._label_length = len({self.first_name}+" "+{self.last_name})
        return self._label_length

    


class BussinessCard(Card):
    def __init__(self, job, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jon = job
        self.company = company

    def contact(self):
        print(f"Kontaktuję się z {self.first_name()} {self.last_name()} e-mail: {self.email()}")


    @property
    def label_length(self):
        self._label_length = len({self.first_name}+" "+{self.last_name})
        return self._label_length


def fejk_base():
    from faker import Faker
    fake = Faker(['pl_PL'])
    print(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address(), fake.email())

def fejk_bussiness():        
    from faker import Faker
    fake = Faker(['pl_PL'])
    print(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address(), fake.email(), fake.job(), fake.company())

def create_contacts(rodzaj, ilosc):
    if rodzaj == BaseCard:
        for i in range(ilosc):
            wizyt = fejk_base()
            print(wizyt)
    elif rodzaj == BussinessCard:
        for i in range(ilosc):  
            wizyt=fejk_bussiness()    
            print(wizyt)  
    else:
        print("zły rodzaj wizytówki")

create_contacts(BussinessCard, 3)


        