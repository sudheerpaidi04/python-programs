## Program 2: Print Sequence Using For Loop

**Program Name:** Print Sequence with Step

**Program Code:**
```python
for i in range(8, 90, 3):
    print(i, end='  ')
```

**Program Output:**
```
8 11 14 17 20 23 26 29 32 35 38 41 44 47 50 53 56 59 62 65 68 71 74 77 80 83 86 89
```

---

## Program 3: Split String into Characters

**Program Name:** String to Character Array

**Program Code:**
```python
text = "hello"
characters = list(text)
print(characters)
```

**Program Output:**
```
['h', 'e', 'l', 'l', 'o']
```

---

## Program 4: Find Largest Number in List

**Program Name:** Maximum Number Finder

**Program Code:**
```python
numbers = [45, 12, 78, 34, 89, 23, 90, 67]
largest = max(numbers)
print(f"The largest number in the list is: {largest}")
```

**Program Output:**
```
The largest number in the list is: 90
```

---

## Program 5: Calculate nth Fibonacci Number

**Program Name:** Fibonacci Number Calculator

**Program Code:**
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
    return b

n = int(input("Enter the position (n) of the Fibonacci number: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
```

**Program Output:**
```
Enter the position (n) of the Fibonacci number: 3
The 3th Fibonacci number is: 2
```

---

---
