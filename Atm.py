class Atm():
    def __init__(self,card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def cashWithDrawl(self):
        card = input("Enter your Card Number here.")
        pin = input("Enter your Pin Number here.")
        cash = input("Enter The Amount of Cash you Want to Withdrawl.")
        print("Cash Withdarwled Successfully.")
    
    def cashDeposit(self):
        card = input("Enter your Card Number here.")
        pin = input("Enter your Pin Number here.")
        cash = input("Enter The Amount of Cash you Want to Deposit.")
        print("Cash Deposited Successfully.")
    
    def balanceEnquiry(self):
        print("Balance Enquired Successfully.")

Aviraj = Atm(123,456)
Aviraj.cashWithDrawl()