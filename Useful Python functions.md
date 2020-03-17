# Useful Python functions
- `abs(x)`: The abs() takes only one argument, a number whose absolute value is to be returned. The argument can be an integer, a floating point number or a complex number.  
- `math.ceil(x)`: Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
- `math.floor(x)`: Return the floor of x as a float, the largest integer value less than or equal to x.
- `math.sqrt(x)`: Returns the square root of x.
- `pow(x, y, z(opt))`: Returns the value of x to the power of y. If a third parameter is present, it returns x to the power of y, modulus z.  
- `random.randrange(start(opt),stop,step(opt))`: This function generated the numbers in the sequence start-stop skipping step.  
- `random.randint(start,end)`: Returns a random integer within the given range as parameters. Start and end must be interger.
- `random.random()`: Return the next random floating point number in the range [0.0, 1.0).

- `random.shuffle(x)`: Takes a sequence(list, string, or tuple) and reorganize the order of the items.
- `random.choice(x)`: Returns a randomly selected element from the specified sequence.

- `list.index(element, start(opt), end(opt))`: Inbuilt function in Python, which searches for given element from start of the list and returns the lowest index where the element appears.
- `list.insert(index, element)`: Inbuilt function in Python that inserts a given element at a given index in a list.
- `list.count(object)` is an inbuilt function in Python that returns count of how many times a given object occurs in list.
- `list.remove(obj)` is an inbuilt function in Python that removes a given object from the list.
- `bisect.bisect(list,num,begin(opt),end(opt))` returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the right most position where element has to be inserted is returned. This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.
- `dict.setdefault(key, default_value(opt))`: Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
- `string.join(iterable)` method takes all items in an iterable and joins them into one string.A string must be specified as the separator.
- `sum(iterable,start(opt))`: Inbuilt function sum() which sums up the numbers in the list. Returns the sum of the list + start. 
- `functools.reduce(function,seq)` is used to apply a particular function to all of the elements in the sequence passed along.
