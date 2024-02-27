#multiple inheritance

class bank:

    def transaction(self):
        print("total transcation value")
    def account_opening(self):
        print("this will show you your accaount opening details")
    def deposite(self):
        print("this will show you your deposite details")
    def test(self):
        print("this is a test method for blank class")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will shoe you all the transaction hapended to icici from hdfc")

    def test(self):
        print("this is a test method for HDFC blank class")

class ineuron_bank:
    def accont_status_icici(self):
        print("print account status of icici")

#class icici(bank, HDFC_bank):
#    pass

class icici(HDFC_bank,bank, ineuron_bank):
    pass

s = icici()
s.hdfc_to_icici()
s.transaction()
s.deposite()
s.account_opening()
s.test()
s.accont_status_icici()