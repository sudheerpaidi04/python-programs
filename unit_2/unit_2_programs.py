# UNIT-2: Object-Oriented Programming (OOP)

## Program 6: Car Class with Methods

**Program Name:** Car Class Definition

**Program Code:**
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.year} {self.make} {self.model} is starting...")
    
    def stop(self):
        print(f"{self.year} {self.make} {self.model} is stopping...")

my_car = Car("Toyota", "Camry", 2022)
my_car.start()
my_car.stop()
```

**Program Output:**
```
2022 Toyota Camry is starting...
2022 Toyota Camry is stopping...
```

---

## Program 7: Inheritance - Base and Derived Classes

**Program Name:** Animal Inheritance Demo

**Program Code:**
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()
```

**Program Output:**
```
Dog barks
Cat meows
```

---

## Program 8: Polymorphism Demonstration

**Program Name:** Animal Polymorphism

**Program Code:**
```python
class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def make_sound(self):
        print("Tweet!")

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.make_sound()
```

**Program Output:**
```
Woof!
Meow!
Tweet!
```

---

## Program 9: Exception Handling - Division by Zero

**Program Name:** Exception Handling Demo

**Program Code:**
```python
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    divide_numbers(21, 2)
    divide_numbers(8, 0)
```

**Program Output:**
```
The result of 21 / 2 is: 10.5
Error: Division by zero is not allowed.
```

---

---
