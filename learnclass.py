class Student:
    def __init__(self): # initialize, when class object student is born, function would do initialize
    # only __init__ would automatically execute
        print("I'm born!")

    def do_hw(self):
        print("I'm doing my hw!")

    def study(self):
        print("I'm study")

    def sleep(self):
        print("I am sleeping!")

s = Student()
s.do_hw()
s.study()
s.sleep()