class parent:
    def parent_method(self):
        print("I am parent method")

class child(parent):
    def child_method(self):
        print("I am child method")

c = child()
c.parent_method()
c.child_method()