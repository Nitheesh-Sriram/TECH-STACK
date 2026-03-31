class parent:
    def __init__(self):
        print("I am from parent class constructor")

class child(parent):
    def __init__(self):
        print("I am from child class constructor")
        super().__init__()


obj = child()
