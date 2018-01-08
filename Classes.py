# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:27:11 2018

@author: Markos
"""


#Class definition in Python

class Car(object):
    def __init__(self, w, d):
        self.name = None #self.name is always pre-defined 
        self.wheels = w
        self.doors = d
        self.color = ""
    def paint(self, c): #this is a "setter"
        self.color = c
    def get_color(self):
        return self.color
    

    def __str__(self): #used when we call print() on our Class object
        return "This car has "+str(self.wheels)+"wheels and "+str(self.doors)+"doors"\
                "and the color is "+str(self.color)

    def __eq__(self, other):
        if self.wheels == other.wheels and \
            self.color == other.color and \
            self.doors == other.doors:
            return True
        else:
            return False

#Testing the new class
#create 2 new cars
mycar = Car(4, 2)
yourcar = Car(4,2)

yourcar.paint("black")
mycar.paint("red") #setter

print(mycar)
print(yourcar)
#check the color:
print("my car has color ",mycar.get_color())    #use the get instead of the dot
print("your car has color ",yourcar.get_color())

if mycar == yourcar:
    print ("Cool we have the same car!")
else:
    print("Sorry but we have different car!")
    
    
    

   
#################################
## Inheritance example
#################################
#class Person(Animal):
#    def __init__(self, name, age):
#        Animal.__init__(self, age)
#        self.set_name(name)
#        self.friends = []
#    def get_friends(self):
#        return self.friends
#    def speak(self):
#        print("hello")
#    def add_friend(self, fname):
#        if fname not in self.friends:
#            self.friends.append(fname)
#    def age_diff(self, other):
#        diff = self.age - other.age
#        print(abs(diff), "year difference")
#    def __str__(self):
#        return "person:"+str(self.name)+":"+str(self.age)
#
#print("\n---- person tests ----")
#p1 = Person("jack", 30)
#p2 = Person("jill", 25)
#print(p1.get_name())
#print(p1.get_age())
#print(p2.get_name())
#print(p2.get_age())
#print(p1)
#p1.speak()
#p1.age_diff(p2)



