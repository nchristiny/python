## Animal is-a object.
class Animal(object):
    pass

## Dog is-a Animal.
class Dog(Animal):
    ## Dog has-a name.
    def __init__(self, name):
      self.name = name

## Cat is-a Animal.
class Cat(Animal):
    ## Cat has-a name.
    def __init__(self, name):
        self.name = name

## Person is-a object.
class Person(object):
    def __init__(self, name):
        ## Person has-a name.
        self.name = name

        ## Person has-a pet of some kind.
        self.pet = None

## Employee is-a Person.
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee inherits from superclass Person, therefore has-a name.
        super(Employee, self).__init__(name)
        ## Employee has-a salary.
        self.salary = salary

## Fish is-a object.
class Fish(object):
    pass

## Salmon is-a Fish.
class Salmon(Fish):
    pass

## Halibut is-a Fish.
class Halibut(Fish):
    pass

## rover is-a Dog.
rover = Dog("Rover")

## satan is-a Cat. So clever!
satan = Cat("Satan")

## mary is-a Person.
mary = Person("Mary")

## From mary get pet attribute and set it to satan.
mary.pet = satan

## frank is-a Employee.
frank = Employee("Frank", 120000)

## From frank get pet attribute and set it to rover.
frank.pet = rover

## flipper is-a Fish.
flipper = Fish()

## crouse is-a Salmon.
crouse = Salmon()

## harry is-a Halibut.
harry = Halibut()
