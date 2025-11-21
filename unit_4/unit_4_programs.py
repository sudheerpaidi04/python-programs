# UNIT-4: Pandas DataFrame Operations

## Program 16: Create and Display Pandas Series

**Program Name:** Pandas Series Creation

**Program Code:**
```python
import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)

print("Pandas Series:")
print(series)
```

**Program Output:**
```
Pandas Series:
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

---

## Program 17: Convert Pandas Series to Python List

**Program Name:** Series to List Conversion

**Program Code:**
```python
import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:")
print(data)

py_list = data.tolist()
print("\nConverted to Python list:")
print(py_list)
print("\nType of the converted object:", type(py_list))
```

**Program Output:**
```
Pandas Series:
0    10
1    20
2    30
3    40
4    50
dtype: int64

Converted to Python list:
[10, 20, 30, 40, 50]

Type of the converted object: <class 'list'>
```

---

## Program 18: Create DataFrame from Dictionary

**Program Name:** DataFrame Creation with Index Labels

**Program Code:**
```python
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

print("Pandas DataFrame with index labels:")
print(df)
```

**Program Output:**
```
Pandas DataFrame with index labels:
        name    score  attempts qualify
a   Anastasia   12.5         1     yes
b       Dima      9.0         3      no
c   Katherine   16.5         2     yes
d      James     NaN         3      no
e      Emily     9.0         2      no
f    Michael    20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes
```

---

## Program 19: Replace Value in DataFrame Column

**Program Name:** DataFrame Value Replacement

**Program Code:**
```python
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

print("Original DataFrame:")
print(df)

df.loc[df['name'] == 'James', 'name'] = 'Suresh'

print("\nDataFrame after changing 'James' to 'Suresh':")
print(df)
```

**Program Output:**
```
Original DataFrame:
        name   score   attempts qualify
a   Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c   Katherine   16.5         2     yes
d      James    NaN         3      no
e      Emily    9.0         2      no
f    Michael   20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes

DataFrame after changing 'James' to 'Suresh':
        name   score   attempts qualify
a   Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c   Katherine   16.5         2     yes
d     Suresh    NaN         3      no
e      Emily    9.0         2      no
f    Michael   20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes
```

---

## Program 20: Insert New Column in DataFrame

**Program Name:** Add Column to DataFrame

**Program Code:**
```python
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df['age'] = [21, 23, 22, 20, 21, 24, 23, 22, 25, 20]

print(df)
```

**Program Output:**
```
      name  score  attempts qualify  age
a  Anastasia   12.5         1     yes   21
b       Dima    9.0         3      no   23
c  Katherine   16.5         2     yes   22
d      James    NaN         3      no   20
e      Emily    9.0         2      no   21
f    Michael   20.0         3     yes   24
g    Matthew   14.5         1     yes   23
h      Laura    NaN         1      no   22
i      Kevin    8.0         2      no   25
j      Jonas   19.0         1     yes   20
```

---

## Program 21: Extract Column Headers from DataFrame

**Program Name:** Get Column Headers as List

**Program Code:**
```python
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

col_list = df.columns.tolist()
print("List of column headers:")
print(col_list)
```

**Program Output:**
```
List of column headers:
['name', 'score', 'attempts', 'qualify']
```

---

---
