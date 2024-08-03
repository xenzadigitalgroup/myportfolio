# Kelas dan Objek
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Human(Person):
    def speak(self):
        return f"{self.name} CALL."

dog = Human("ZAKI")
print(dog.speak())
