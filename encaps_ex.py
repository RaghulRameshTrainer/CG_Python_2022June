class Account():
    def __init__(self,fname,lname,deposit):
        self.fname=fname
        self.lname=lname
        self.__balance=deposit   # public, (_) protected (__) private
        self.username=fname+'123'
        self.password=lname.title()+'@100'

    def getBalance(self):
        return self.__balance
    def setBalance(self,amount):
        self.__balance=self.__balance+amount