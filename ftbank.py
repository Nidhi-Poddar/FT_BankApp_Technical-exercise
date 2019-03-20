import sys
import datetime

def get_date():
    return datetime.date.today().strftime("%d/%m/%Y")

class Customer:
    '''Customer class with bank related operations'''
    
    def __init__(self,balance=0, transaction=0):
        self.balance = balance
        self.transaction = transaction
        self.dates = get_date()

    def deposit(self,amt):
        self.balance = self.balance + amt
        print('After deposit the balance: ', self.balance)
        self.credit = amt
        self.transaction = self.transaction + 1

    def withdraw(self, amt):
        if amt>self.balance:
            print('Insufficient Funds... cannot perform this operation')
            sys.exit()
            
        self.balance=self.balance-amt
        print('After withdraw The balance: ',self.balance)
        self.debit = amt
        self.transaction = self.transaction + 1

    def display_account(self):
        print('| Date || Credit || Debit|| Balance')

        if self.transaction > 0:
            print('|{date} ||{credit} ||{debit} ||{balance}|'.format(date=self.dates, credit=self.credit, debit=self.debit, balance=self.balance))
              
c=Customer(0)

print('Welcome to Poddar Bank')
while True:
    print("1. Deposit\n2. Withdraw\n3. Transaction History\n4. Exit")
    option = int(input('Choose your option'))
    if option == 1:
        amt = float(input('Enter the amount to deposit'))
        if amt > 0:
            c.deposit(amt)
        else:
            print('Please enter valid amount')
    elif option == 2:
        amt = float(input('Enter the amount to withdraw'))
        c.withdraw(amt)
    elif option == 3:
        c.display_account()
    
    elif option == 4:
        sys.exit()
    else :
        print('Please choose a valid option')
    
    
      
