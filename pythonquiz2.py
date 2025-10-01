#variables
age = 18
name = "Zaire"
print("Hi, my name is", name, "and I am", age, "years old.")

#integer
print('12')

#strings
print("Hello, World!")

#list
print([1, 2, 3, 4, 5])

#function
def square(number):
    return number * number
result = square(5)
print(result)

#class
class Greeter:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}!"
person = Greeter("Alice")
print(person.greet())