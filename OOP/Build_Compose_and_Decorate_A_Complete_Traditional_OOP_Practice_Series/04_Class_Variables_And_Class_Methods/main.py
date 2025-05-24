class Bank:

    bank_name = "Bank Al-Habib Linmited"

    def __init__(self, account_holder):
        self.account_holder = account_holder


    @classmethod 
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

customer1 = Bank("Nazeen") 

customer1.show_details()

Bank.change_bank_name("Meezan Bank Limited")

customer1.show_details()

