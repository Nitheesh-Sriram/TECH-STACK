class parent:
    def show(self):
        print("I am show method from parent class")
    
class child(parent):
    def show(self):
        print("I am show method from child class")
        super().show()

obj = child()
obj.show()