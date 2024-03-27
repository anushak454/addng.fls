class Animal:
    def make_sound(self):
        print("Animals can make sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog will bark")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

class Cow(Animal):
    pass

animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()

print(animal.make_sound())
print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())

"""
output::
Animals can make sound
None
Dog will bark
None
Cat meows
None
Animals can make sound
None

Process finished with exit code 0
"""
