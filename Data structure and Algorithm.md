# Basics of Data structure and Algorithm

### Tricks:
If you encounter an algorithm that you haven’t met before in an interview, making a results table will help. 


### Efficiency
- Efficiency, also called “Complexity”, is how well you’re using your computer’s resources to get a particular job done.
- Think of it in terms of space and time, which is how long does your code take to run, and how much storage space do you need.
- When we’re discussing efficiency we often talk about it in terms of the worst case scenario.


### Algorithm
Algorithm is just a series of steps for solving a problem. Or you can say it is a high level description of a trick for solving a problem.

### Big O Notation
- We can describe efficiency of code with Big O Notation, which is always going to be a mathematical function of the variable n.
- The variable n represents the length of an input to your function.

### Collection
A collection is just a group of things, without inherent order.

### List
- A list is a collection with order.
- Inserting into a list happens in constant time.

### Array
- An array is a list with index.
- Inserting into an array is O(n), 

### Linked list
- An extension of a list.
- Inserting an element happens in constant time.
- Doubly linked list: Each element has pointers to both the next element and the previous element. 

### Stacks
- Stack is a list-based data structure.
- Push: Add an element (O(1))
- Pop: Take an element off (O(1))
- FILO：First in, Last out

### Queue
- Queue is a list-based data structure.
- Head: The first(oldest) element in the queue.
- Tail: The last(newest) element in the queue.
- Enqueue: Add an element to the tail.
- Dequeue: Remove the head element.
- Peek: Look at the head element.
- FIFO: First in, First out
- Deques: Double-ended queue. Can enqueue or dequeue from either end. Like a generalized version of both stacks and queue.
- Priority queue: Each element is assigned with a numerical priority when inserted. When dequeue, start removing element with the highest priority.

### sets
- A collection without order and has no repeat elements.

### Map
- Key-value structure based on sets
- Keys in a map are a set

### Binary Search
- Efficiency: O(log(n))
- The constraint for binary search, elements need to be in increasing order.

### Recursion
1. A recursive function needs to call itself at some point
2. A recursive function needs a base case.
3. A recursive function needs to alter the input parameter at some point, or it’s going to be a infinite loop.



## Sorting 
- In place sorting algorithm: Rearrange the elements in the data structure they’re already in without needing to copy everything to a new data structure. Low space complexity.

### Bubble sort
- Bubble sort is a naive approach.
- In-place sorting algorithm.
- You will go through array comparing elements side by side and switching them whenever necessary.
- In each iteration the largest element in the array will bubble on up to the top.
- Efficiency: Worst and Average case: O(n²)
- Efficiency: Best case: O(n)
- Space complexity: O(1)

### Merge sort
- Split an array down as much as possible and build it back up doing comparisons and sorting at each step along the way.
- Divide and Conquer: Break up an array, sorting all the parts of it and building it back up again.
- Efficiency: Doing roughly n comparisons for log(n) steps, so time efficiency is O(nlog(n)). However, space efficiency, or Auxiliary Space is O(n).

### Quick sort
- Pick one of the values in the array at random. Move all values larger than it above it and all values below it, lower than it. Then continue on recursively, picking a pivot in the upper and lower sections of the array, sorting them until the whole array is sorted.
- The value picked initially is called a pivot. The convention is to pick the last one element.
- Efficiency: Worst case: O(n²). Average and best case: O(nlog(n)).
- In place sorting, so space efficiency is O(1).

### Hashing
- Using a data structure that employs a hash function allows you to do look-ups in **constant time**
- The purpose of hash function is to transform some value into one that can be stored and retrieved easily.
- Load Factor = Number of Entries / Number of Buckets
- The purpose of a load factor is to give us a sense of how "full" a hash table is. For example, if we're trying to store 10 values in a hash table with 1000 buckets, the load factor would be 0.01, and the majority of buckets in the table will be empty. We end up wasting memory by having so many empty buckets, so we may want to rehash, or come up with a new hash function with less buckets. We can use our load factor as an indicator for when to rehash—as the load factor approaches 0, the more empty, or sparse, our hash table is.   
On the flip side, the closer our load factor is to 1 (meaning the number of values equals the number of buckets), the better it would be for us to rehash and add more buckets. Any table with a load value greater than 1 is guaranteed to have collisions. 

### Tree
- A tree starts from a place called root and you add data to it called branches.
- A tree is just an extension of a linked list. Instead of having only one next element, a tree can have several next elements.
- A linked list is always drawn horizontally, but a tree normally drawn vertically.
- The individual elements in a tree that contain values are often called nodes.
- Constraints on tree:  
    - Connected: There must be some way to reach every node from the root.
    - Uncycled: There must not be any cycles in the tree.
- Levels: how many connections it takes to reach the root plus one. The root is level 1.
- Nodes in a tree are often having a parent child relationship.
- Leaves: The nodes at the end that don't have any children are called leaves or external nodes. A parent node is called an internal node.
- Edge: A connection of two nodes. 
- Path: A group of connections taken together.
- Height: Number of edges between it and the furthest leaf on the tree. A leaf has a height of zero. The height of the tree overall is just the height of the root node.
- Depth: The depth of a node is the number of edges to the root. The depth of root is 0.
- Height and depth should move inversely.
