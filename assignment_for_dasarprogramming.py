#LIST

#Definition: A list is an ordered, mutable collection of items

#Characteristics:
    #Ordered: Items have a defined order.
    #Mutable: Items can be added, removed, or changed.
    #ndexed: Each item can be accessed using an index.

#Usage: Useful when you need a collection of items that can be changed

# Creating a list
fruits = ["apple", "banana", "cherry"]
# Accessing an item by index
print(fruits[1])  # Output: banana
# Modifying an item
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
# Adding an item
fruits.append("date")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

#TUPLE

#Definition: A tuple is an ordered, immutable collection of items
#Characteristics:
     #Ordered: Items have a defined order.
     #Immutable: Once created, items cannot be changed.
      #Indexed: Each item can be accessed using an index.
#Usage: Useful for fixed collections of items where the order and content should not change.

# Creating a tuple
coordinates = (10.0, 20.0)
# Accessing an item by index
print(coordinates[0])  # Output: 10.0
# Attempting to modify an item (this will raise an error)
# coordinates[0] = 15.0  # Uncommenting this line will raise a TypeError
# Tuples can be used to return multiple values from a function
def get_min_max(numbers):
    return (min(numbers), max(numbers))

min_max = get_min_max([2, 4, 6, 8])
print(min_max)  # Output: (2, 8)


#Dictionary
#Definition: A dictionary is an unordered collection of key-value pairs.
#Characteristics:
  #Unordered: Items have no defined order (insertion order is preserved in Python 3.7+).
  #Mutable: Keys and values can be added, removed, or changed.
  #Keyed: Each item is accessed using a key.
  #Usage: Useful for mapping unique keys to values, such as storing information in a structured way.

# Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing a value by key
print(person["name"])  # Output: Alice

# Modifying a value
person["age"] = 31

print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# Adding a new key-value pair

person["email"] = "alice@example.com"
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}
# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

#In summary:

#List: Ordered and mutable (e.g., ["apple", "banana", "cherry"]).
#Tuple: Ordered and immutable (e.g., (10.0, 20.0)).
#Dictionary: Unordered collection of key-value pairs (e.g., {"name": "Alice", "age": 30}).




    