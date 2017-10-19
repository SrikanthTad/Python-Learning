class Parent:

        counter =10
        def __init__(self):

            print("class initialized")

        def parentFunc(self):
            print("parentFunc being called")

        def setCounter(self, count):
            Parent.counter = count

        def showCounter(self):
            print(str(Parent.counter))


class Child(Parent):
    def __init__(self):
        print("child class being initialized")

    def childFunc(self):
        print("childfunc being called")



c = Child()
c.childFunc()
print("hi")
