#Composition means building a class using objects of other classes.

'''class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is ready to move")


car1 = Car()
car1.start_car()'''

class Processor:
    def process(self):
        print("processor is processing instructions")


class Memory:
    def load_data(self):
        print("Memory is loading data")

class Computer:
    def __init__(self):
        self.Processor = Processor()
        self.Memory = Memory()

    def start_computer(self):
        self.Processor.process()
        self.Memory.load_data()
        print("Computer has started successfully")