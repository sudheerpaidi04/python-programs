# UNIT-3: NumPy and Array Operations

## Program 10: Add Two Numbers Function

**Program Name:** Simple Addition Function

**Program Code:**
```python
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
print("The sum is:", result)
```

**Program Output:**
```
Enter first number: 12
Enter second number: 8
The sum is: 20
```

---

## Program 11: Check if All Array Elements are Non-Zero

**Program Name:** Non-Zero Elements Checker

**Program Code:**
```python
def no_zero_elements(arr):
    for element in arr:
        if element == 0:
            return False
    return True

array = list(map(int, input("Enter array elements separated by space: ").split()))
if no_zero_elements(array):
    print("✅ All elements are non-zero.")
else:
    print("❌ At least one element is zero.")
```

**Program Output (Case 1):**
```
Enter array elements separated by space: 4 0 6 9
❌ At least one element is zero.
```

**Program Output (Case 2):**
```
Enter array elements separated by space: 3 5 7 2
✅ All elements are non-zero.
```

---

## Program 12: Element-Wise Array Comparison

**Program Name:** NumPy Array Comparison

**Program Code:**
```python
import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([15, 20, 25, 40, 60])

print("Array 1:", array1)
print("Array 2:", array2)
print("\nElement-wise Comparisons:")
print("Greater:         ", np.greater(array1, array2))
print("Greater Equal:   ", np.greater_equal(array1, array2))
print("Less:            ", np.less(array1, array2))
print("Less Equal:      ", np.less_equal(array1, array2))
print("Equal:           ", np.equal(array1, array2))

tolerance = 5
print("\nEqual within tolerance (±{}):".format(tolerance), np.allclose(array1, array2, atol=tolerance))
```

**Program Output:**
```
Array 1: [10 20 30 40 50]
Array 2: [15 20 25 40 60]

Element-wise Comparisons:
Greater:          [False False  True False False]
Greater Equal:    [False  True  True  True False]
Less:             [ True False False False  True]
Less Equal:       [ True  True False  True  True]
Equal:            [False  True False  True False]

Equal within tolerance (±5): False
```

---

## Program 13: NumPy Methods - max, min, argmax, argmin, unique

**Program Name:** NumPy Array Methods

**Program Code:**
```python
import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])
print("Original array:", arr)

print("\nUsing repr():")
print(repr(arr))

print("\nUsing count():")
arr_list = arr.tolist()
print("Count of 4 in array:", arr_list.count(4))

print("\nUsing np.bincount():")
print("Element counts (by index):", np.bincount(arr))

print("\nUsing np.unique():")
unique_elements, counts = np.unique(arr, return_counts=True)
print("Unique elements:", unique_elements)
print("Counts:", counts)
```

**Program Output:**
```
Original array: [1 2 2 3 4 4 4 5]

Using repr():
array([1, 2, 2, 3, 4, 4, 4, 5])

Using count():
Count of 4 in array: 3

Using np.bincount():
Element counts (by index): [0 1 2 1 3 1]

Using np.unique():
Unique elements: [1 2 3 4 5]
Counts: [1 2 1 3 1]
```

---

## Program 14: Extract Elements Less and Greater than Threshold

**Program Name:** Array Threshold Filtering

**Program Code:**
```python
import numpy as np

arr = np.array([5, 12, 7, 20, 3, 15, 8])
threshold = 10

less_than = arr[arr < threshold]
greater_than = arr[arr > threshold]

print("Original Array:", arr)
print("Values less than", threshold, ":", less_than)
print("Values greater than", threshold, ":", greater_than)
```

**Program Output:**
```
Original Array: [ 5 12  7 20  3 15  8]
Values less than 10 : [5 7 3 8]
Values greater than 10 : [12 20 15]
```

---

## Program 15: Find Indices of Max and Min Values

**Program Name:** Max and Min Indices Finder

**Program Code:**
```python
import numpy as np

arr = np.array([[10, 20, 5],
                [15, 3, 25],
                [30, 8, 12]])

print("Original array:")
print(arr)

max_indices = np.argmax(arr, axis=1)
min_indices = np.argmin(arr, axis=1)

print("\nIndices of the maximum values along each row:", max_indices)
print("Indices of the minimum values along each row:", min_indices)

max_values = arr[np.arange(len(arr)), max_indices]
min_values = arr[np.arange(len(arr)), min_indices]

print("\nMaximum values:", max_values)
print("Minimum values:", min_values)
```

**Program Output:**
```
Original array:
[[10 20  5]
 [15  3 25]
 [30  8 12]]

Indices of the maximum values along each row: [1 2 0]
Indices of the minimum values along each row: [2 1 1]

Maximum values: [20 25 30]
Minimum values: [5 3 8]
```

---

---
