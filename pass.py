class Person:
    def greet(self):
        return f"Hi"
    def walk(self):
        pass
    
class Worker:
    def work(self):
        print("Is working")
   
        
        

class Student(Person, Worker):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def __str__(self):
        return f"I'm {self.name} {self.surname} and I'm attending 3rd grade school"
    
    def greet(self):
        return super().greet() + " I'm a student"
    
    def walk(self):
        print(" I'm walking")
    
    
s1 = Student("Paul", "Rigs")
print (s1)
s1.work()

print(s1.greet())
s1.walk()


