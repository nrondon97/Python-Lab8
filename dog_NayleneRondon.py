#Name: Naylene Rondon
#Date: 3/29/17
#Purpose: Classes - Object Orientation

class Dog():
    """A Simple attempt to model a dog."""

#__init__  method is needed
    def __init__(self, name, age):       #self always requires as a parameter
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


#Create an object
my_dog_1 = Dog("Willie", 6)  #Self doesn't appear as it is a calling of the class

#Called Instances
print("My dog's name is " + my_dog_1.name.title() + ".")
print("My dog is " + str(my_dog_1.age) + " years old.")

#Called Functions from within Class
my_dog_1.sit()
my_dog_1.roll_over()
        
#Create an object
my_dog_2 = Dog("Lucy", 3)  #Self doesn't appear as it is a calling of the class

#Called Instances
print("My dog's name is " + my_dog_2.name.title() + ".")
print("My dog is " + str(my_dog_2.age) + " years old.")

#Called Functions from within Class
my_dog_2.sit()
my_dog_2.roll_over()


print(my_dog_1.name.title() + " is the same breed as " + my_dog_2.name.title() + ".")
