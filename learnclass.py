class Student:
    # property 1 : function
    def __init__(self, name, score): 
        """
            initialize, when class object student is born, function would do initialize
            only __init__ would automatically execute        
        """
        # property 2 : non function
        self.name = name
        self.score = score
        print("I'm born! I'm " + name)

    def do_hw(self):
        print("I'm doing my hw!")
        """
            Self = self reference
            that's why we need self, but why we don't have to send argument value for "self"?
            Because python would automatically pass self inside the function.
        """
        self.study()

    def study(self):
        print("I'm study")
        self.score += 5

    def sleep(self):
        print("I am sleeping!")

s1 = Student("Allen",100)
s2 = Student("Ben",95)
students = [s1, s2]
for s in students:
    print(s.name, "'s score is ", s.score)

"""
class 3 特點:
收納func
透過self 共用身上的屬性
包奘程式碼
"""