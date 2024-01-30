class Dog:
    """A simple attempt to model a dog!"""

    def __init__(self,name,age):
        """Makes the name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting text based"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """The dog rolls over"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie',6)
your_dog = Dog('Lucy',3)

my_dog.sit()
my_dog.roll_over()

print(f"My dogs name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog's age is {your_dog.age}")