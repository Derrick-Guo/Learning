# Useful Python functions
- `abs(x)`: The abs() takes only one argument, a number whose absolute value is to be returned. The argument can be an integer, a floating point number or a complex number.  
- `ord(char)` returns an integer representing the Unicode character.
- `chr(i)` returns a character (a string) from an integer which represents the unicode code point of the character.
- `math.ceil(x)`: Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
- `math.floor(x)`: Return the floor of x as a float, the largest integer value less than or equal to x.
- `math.sqrt(x)`: Returns the square root of x.
- `pow(x, y, z(opt))`: Returns the value of x to the power of y. If a third parameter is present, it returns x to the power of y, modulus z.  
- `random.randrange(start(opt),stop,step(opt))`: This function generated the numbers in the sequence start-stop skipping step.  
- `random.randint(start,end)`: Returns a random integer within the given range as parameters. Start and end must be interger.
- `random.random()`: Return the next random floating point number in the range [0.0, 1.0).

- `random.shuffle(x)`: Takes a sequence(list, string, or tuple) and reorganize the order of the items.
- `random.choice(x)`: Takes a sequence(list, string, or tuple), and returns a randomly selected element from the specified sequence.

- `list.index(element, start(opt), end(opt))`: Inbuilt function in Python, which searches for given element from start of the list and returns the lowest index where the element appears.
- `list.insert(index, element)`: Inbuilt function in Python that inserts a given element at a given index in a list.
- `list.count(object)` is an inbuilt function in Python that returns count of how many times a given object occurs in list.
- `list.remove(obj)` is an inbuilt function in Python that removes a given object from the list.
- `bisect.bisect(list,num,begin(opt),end(opt))` returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the right most position where element has to be inserted is returned. This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.
- `dict.setdefault(key, default_value(opt))`: Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
- `string.join(iterable)` method takes all items in an iterable and joins them into one string. A string must be specified as the separator. If the iterable contains any non-string values, it raises a TypeError exception.
- `string.replace(old, new, count)` is an inbuilt function in Python programming language that returns a copy of the string where all occurrences of a substring is replaced with another substring.
- `string.startswith(prefix,start(opt),end(opt))` returns True if a string starts with the specified prefix(string). If not, it returns False.
- `string.endswith(suffix,start(opt),end(opt))` returns True if a string ends with the specified suffix. If not, it returns False.
- `string.isalnum()` checks whether all the characters in the given string is alphanumeric or not.
- `string.find(substring,start(opt),end(opt))` returns the index of first occurrence of the substring (if found). If not found, it returns -1.
- `string.index(substring,start(opt),end(opt))` returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
- `string(import).digits` is the string '0123456789'. 
- `string(import).hexdigits` is the string '0123456789abcdefABCDEF'.
- `sum(iterable,start(opt))`: Inbuilt function sum() which sums up the numbers in the list. Returns the sum of the list + start. 
- `functools.reduce(function,seq,initializer(opt))` is used to apply a particular function to all of the elements in the sequence passed along. The initializer will be set as the first argument to the function.
  - At first step, first two elements of sequence are picked and the result is obtained. 
  - Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored. 
  - This process continues till no more elements are left in the container. 
  - The final returned result is returned and printed on console.
- `collections.Counter()` is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
- `collections.namedtuples(typename, field_names)` Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
- 'collections.defaultdict(default_factory)' is a sub-class of the dict class that returns a dictionary-like object. The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists. The `default_factory` parameter is a function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError. When the `list` class is passed as the `default_factory` argument, then a defaultdict is created with the values that are list.
- `all(iterable)` returns True when all elements in the given iterable are true. If not, it returns False.
- `any(iterable)` returns True if any element of an iterable is True. If not, returns False.
- `itertools.combinations(iterable, r)` returns the r length subsequences of elements from the input iterable. 
eg: `li=[0,1,2] 
print([num for num in itertools.combinations(li,2)])` will be [(0, 1), (0, 2), (1, 2)].
- `itertools.groupby(iterable,keyfunc(opt))` returns grouped key and iterator pairs for the given iterable. Refer to https://www.geeksforgeeks.org/itertools-groupby-in-python/
- `itertools.islice(iterable,start(opt),stop,step(opt))` returns sliced iterator which passed as argument.  
eg:`li=[0,1,2,3,4,5] 
print([num for num in itertools.islice(li,3)])` will be [0, 1, 2].
