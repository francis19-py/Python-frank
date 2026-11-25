#Polymorphism means many forms. In Python, it allows different objects to respond to the same method call in different ways.
'''
Imagine a payment system with different payment methods:
- M-Pesa
- Bank transfer
- Card payment
Each payment method could have a process_payment() method, but each implements the operation differently.

Your backend can call the same method wit
'''

class Animal:
    def make_sound(self):
        print("Some animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.make_sound()   