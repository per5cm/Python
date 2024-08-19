# Loops

its an infinite loop.

```python
i = 3 
while i != 0:
    print("meow")
    i = i - 1
```
```mermaid
graph TD
    A[Start] --> B[i = 3]
    B --> C{i != 0?}
    C -- Yes --> D[Print "meow"]
    D --> E[i = i - 1]
    E --> C
    C -- No --> F[End]
```

# Data type list

is like intergers and loat or bool (boolean expression) Python also has list. a list of things in real world is a list of things in Python.