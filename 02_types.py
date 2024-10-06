# Type hints are added using the colon (:) syntax for variables and the -> syntax for
# function return types.

"""
# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str) -> str:
return f"Hello, {name}!"
# Usage
print(greeting("Alice")) # Output: Hello, Alice!
"""

n : int = 5
name : str = "shaq"

def sum(a: int, b: int)-> int:
    return a+b
print(sum(1,2))


# example 2
# variable type hint
age : int=25

# function type hint
def greeting(name: str)->str:
    return f"Hello,{name}"
print(greeting("Shaq"))