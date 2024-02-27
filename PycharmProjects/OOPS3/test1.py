#multilevel inheritance
class bank:

    def transaction(self):
        print("total transcation value")
    def account_opening(self):
        print("this will show you your accaount opening details")
    def deposite(self):
        print("this will show you your deposite details")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will shoe you all the transaction hapended to icici from hdfc")

class icici(HDFC_bank):
    pass


s = icici()
s.hdfc_to_icici()
s.deposite()
s.account_opening()
s.transaction()
