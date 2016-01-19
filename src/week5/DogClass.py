# -*- coding: utf-8 -*-

class Animal(object):
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print "This animal's name: %s" % self.name

    def sound(self):
        print "The sound of this animal goes?"


class Cat(Animal):
    def sound(self):
        print "The sound of cat goes meow ~"


class Dog(Animal):
    "define Dog class"
    counter = 0

    def __init__(self, name, size):
        self.name = name
        self.__size = size
        Dog.counter += 1
        # print 'class' % self.name

    def getInfo(self):
        print "This dog's name: %s" % self.name
        print "This dog’s size: %s" % self.__size

    def greet(self):
        print "Hi, I am %s, my number is %d, my size is %d" % (self.name, Dog.counter, self.__size)


class BarkingDog(Dog):
    "define subclass BarkingDog"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1
        # print 'subclass:%s' % self.age

    def greet(self):
        "initial subclass"
        print "Woof! I am %s, my number is % d , my age is % d" % (self.name, Dog.counter, self.age)


if __name__ == '__main__':
    # dog = BarkingDog("Zoe", 3)
    # dog.greet()
    dog = Dog('coco', 'small')
    dog.sound()

    cat = Cat('kawaii')
    cat.getInfo()
    cat.sound()
    print isinstance(dog, Animal)
    print isinstance(cat, Animal)
    print isinstance(dog, Dog)
    print isinstance(dog, Cat)
