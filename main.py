class ContactList:
    def __init__(self):


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        for i in Contact.all_contacts:
            Contact.all_contacts.remove(i)


class Supplier(Contact):
    all_orders = {}

    # def __init__(self):
    #     super().__init__(args, kwargs)
    #     pass

    def order(self, _string):
        Supplier.all_orders[self.email] = [_string]



