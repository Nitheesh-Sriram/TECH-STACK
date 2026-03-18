class student:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print("Hello my name is :",self.name)


s1 = student("Nitheesh")
s1.greet()