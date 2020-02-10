# Learning
**Data Types**: Integers, Floats, Booleans, Strings  
**Operators**: Arithmetic, Assignment, Comparison, Logical, Membership, Identity   
**Data Structures**: Lists, Tuples, Sets, Dictionaries, Compound Data Structure

### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Mod (the remainder after dividing)
- `**` Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
- `//` Divides and rounds down to the nearest integer

More information of **Bitwise operator** can be find [here](https://wiki.python.org/moin/BitwiseOperators).

### Assignment Operators
- `=` 
- `+=`
- `-=`

### Comparision Operators
- `>`	Greater than 
- `<`	Less than
- `==` Equal to 
- `!=` Not equal to 
- `>=` Greater than or equal to 
- `<=` Less than or equal to 

### Logical Operators
- `and` 
- `or`
- `not`

### Membership Operators
- `in`
- `not in`

### Methods
- A method in Python behaves similarly to a function. Methods actually are functions that are called using **dot notation**. 
- Methods are **specific to the data type** for a particular variable. So there are some built-in methods that are available for all strings, different methods that are available for all integers, etc.
- Important string methods: `.format()`, `.split()`

### Lists
- A list is a data structure in Python that is **mutable ordered** sequence of elements.
- We can pull more than one value from a list at a time by using slicing. When using slicing, it is important to remember that the lower index is **inclusive** and the upper index is **exclusive**.
- Lists are similar to strings. Since both types support the len function, indexing, slicing, and membership operator. 
- Difference between lists and strings is that strings are sequences of letters, while list elements can be any type of object. One more subtle difference is that lists can be modified but strings can't.

### Lists functions
- `len()` returns how many elements are in a list.
- `max()` returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
- `min()` returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
- `sorted()` returns a copy of a list in order from smallest to largest, leaving the list unchanged.

### Lists methods
- `.join()` is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
- `.append()` adds an element to the end of a list.

### Mutability and Order
- Mutability is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called mutable. However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered immutable.
- Order is about whether the position of an element in the object can be used to access the element. We can use the order to access parts of a list and string.

### Tuples
- A tuple is a data type for immutable ordered sequences of elements.
- The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code.
- **Tuple unpacking**: You can use tuple unpacking to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.
