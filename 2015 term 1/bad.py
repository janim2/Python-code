__author__ = 'Administrator'
# BANKY CLASS
class Banky():
    def __init__(self,name,init_amt):
        self .AccountName =name
        self.Balance =init_amt


    def __str__(self):
        return self.AccountName + ":"+ str(self.Balance)



    def deposit(self,depo):
         self.Balance =int(depo)+int(self.Balance)

    def withdraw(self,amt):
         self.Balance -=int(amt)- int(self.withdraw)




