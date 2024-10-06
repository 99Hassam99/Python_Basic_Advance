# ADVANCED TYPE HINTS
# Python's typing module provides more advanced type hints, such as List, Tuple, Dict,
# and Union.
# You can import List, Tuple and Dict types from the typing module like this:


# The syntax of types looks something like this:
from typing import List,Tuple,Dict,Union

# List of integers
numbers: List[int] = [1,2,3,4,5]

# Tuple of a string and an integer
person: Tuple[str,int] = ("alice",21)

# Dictionary with string keys and integer values
scores: Dict[str,int] = {"Alice":90,"Shaq":80}

# UNION type for variable that can hold multiple types
identifier: Union[int,str] = "ID123"
# identifier =12345 # it's also valid

# These annotations help in making the code self-documenting and allow developers to
# understand the data structures used at a glance