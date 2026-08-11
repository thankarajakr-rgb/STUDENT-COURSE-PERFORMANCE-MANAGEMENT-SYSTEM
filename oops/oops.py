#Polymorphism ->Only over ridding no overloading

# Polymorphism in python means one interface or method can be have differentely depending on the object using it

class Animal:
  def eat(self):
    print("Animals can eat")
  def sound(self):
    print("Animals can create different Sounds")

class Dog(Animal):
  def sound(self):
    print("Dog Barks")
    super().sound()


class Streetdogs(Dog):
  def sound(self):
    print("bow bow bowww")
    super().sound()


class Puppy(Dog):
  def sound(self):
    print("wow wow")
    super().sound()

jacky=Puppy()
jacky.sound()
jacky.eat()


jac=Streetdogs()
jac.sound()



