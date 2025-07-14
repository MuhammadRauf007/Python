class animal:
    def __init__(self,name):
        self.name = name 

class Pet(animal):
    def __init__(self, name):
        super().__init__(name)
        print(f"{name} is my pet")

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
        print(f"{name} is a Dog")


d = Dog("Puppy")
