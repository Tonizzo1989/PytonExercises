class Animal:
    def __init__(self, name, age, breed):
        self.__name = name
        self.__age = age
        self.__breed = breed
    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
        
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
        
    def get_breed(self):
        return self.__breed
    def set_breed(self, breed):
        self.__breed = breed
        
    attributeName = property(get_name, set_name)
        
    def __str__(self):
        return f"The animal {self.__name} he's {self.__age} years old and he's a {self.__breed}"

class Cat (Animal):
    def __init__(self, name, age, breed, family):
        super().__init__(name, age, breed)
        self.family = family
    
    def __str__(self):
        return super().__str__() +(f". The family is {self.family}")
    
A = Animal("Rex", 4, "German Shepherd")
print(A.get_age())
A.set_name = "Lollo"
print(A)
print(A.attributeName)
A.attributeName = "Rocky"
print(A)

c = Cat ("Giulietta", 15, "Mixed", "feline")
print (c)


