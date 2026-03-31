class Parent:
    def __init__(self):
        self.value = 69

    def show(self):
        print("Parent class value =", self.value)

class Child(Parent):
    def display(self):
        value = 96
        print(f"Child class value = {value} and parent class value = {self.value}")

obj = Child()
obj.display()