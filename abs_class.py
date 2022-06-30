from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def tyre(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def mirror(self):
        pass
    def price(self,model):
        if model=='endeavour':
            return '4000000'
        elif model=='ecosport':
            return '170000'
        elif model=='aspire':
            return '1000000'
        else:
            return 'Please check at showroom'

class CarProduction(Car):
    def __init__(self,model,make="FORD"):
        self.model=model
        self.make=make

    def breaks(self):
        self.break_status='Applied'
    def mirror(self):
        self.mirror='Fitted'
    def seats(self):
        self.capacity='5 seater'
    def tyre(self):
        self.tyre_count=6
    def order_car(self,amount):
        self.amount=amount
        print("You order has been accepted. Received advance amount Rs.",self.amount)
c1=CarProduction(2022)
c1.order_car(11000)
print(c1.price('ecosport'))
