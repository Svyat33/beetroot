"""
Task 2

Doggy age

Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age. Then create
a method `human_age` which returns the dog’s age in human equivalent.
"""


class Dog:
    age_factor = 7

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


if __name__ == "__main__":
    d = Dog("Barky", 7)
    print(f"{d.name} is {d.human_age()} years old in human equivalent")
