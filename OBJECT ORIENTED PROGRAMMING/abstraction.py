'''
Abstraction means hiding unnecessary implementation details and exposing only the essential operations.

For example, when using an ATM, you interact with operations such as withdrawing money without needing to understand all the internal processing.

In Python, we can implement abstraction using the abc module and abstract classes.

'''

from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass

class bus(Transport):
    def calculate_fare(self, distance):
        return distance * 50

class taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 100
#cus3 =Transport() # This will raise an error because we cannot instantiate an abstract class
cus1 = bus()
cus2 = taxi()
print("Bus fare:",cus1.calculate_fare(5))
print("Taxi fare:",cus2.calculate_fare(5))