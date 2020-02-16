# Python memos
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

### Identity Operators
- `is`
- `is not`

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

### Sets
- A set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list.
- Sets support the in operator the same as lists do. You can add elements to sets using the `.add()` method, and remove elements using the `.pop()` method, similar to lists. Although, when you pop an element from a set, a random element is removed. Remember that sets, unlike lists, are unordered so there is no "last element".

### Dictionary
- A dictionary is a mutable data type that stores mappings of unique keys to values.
- Dictionaries can have keys of any immutable type, like integers or tuples, not just strings.
- We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the `in` keyword.
- `.get()` looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.

### For Loops
- A for loop is used to "iterate", or do something repeatedly, over an iterable.
- An **iterable** is an object that can return one of its elements at a time. This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.
- `range()` is a built-in function used to create an iterable sequence of numbers. eg: `range(start=0, stop, step=1)`

### While Loops vs For Loops
- For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a while loop.
- For loops are ideal when the number of iterations is known or finite. While loops are ideal when the iterations need to continue until a condition is met.

### Zip and Enumerate
- `zip` returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables.
- `enumerate` is a built in function that returns an iterator of tuples containing indices and values of a list. 

### Lambda Expressions
- You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.
- With a lambda expression, this function:  
`def multiply(x, y):
    return x * y`  
can be reduced to:  
`multiply = lambda x, y: x * y`

### High-order built-in functions
- map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
- filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True. 

### Errors
- There are two types of errors: Syntax errors and Exceptions
- Syntax errors occur when Python can't interpret our code since we didn't follow the correct syntax for Python.
- Exceptions occur when unexpected things hanppen during the execution of the code.

### Examples of exceptions:
`try:
    code
except Exception as e:
    code
    print("Exception occurred: {}".format(e))`
