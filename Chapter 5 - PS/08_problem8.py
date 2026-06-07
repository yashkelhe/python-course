# List comprehension is a compact way to create new lists from existing iterables (like lists, tuples, or ranges) using a single line of code. It replaces traditional for loops and makes code faster and easier to read.The Anatomy of List ComprehensionEvery list comprehension follows this core structural blueprint:

# new_list = [expression for item in iterable if condition]



# Traditional Loop
squares = []

for x in range(1, 5):
    squares.append(x**2)

# List Comprehension
squares = [x**2 for x in range(1, 5)]
print(squares)  # Output: [1, 4, 9, 16]



# Variant B: Filtering Elements (if at the end)Acts like a filter. It only processes elements that evaluate to True

nums = [1, 2, 3, 4, 5, 6]

# Keeps only the even numbers
evens = [x for x in nums if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]

"""
Variant C: Conditional Selection (if-else at the start)Use this when you need to retain all items but change their values based on a condition.Crucial Syntax Rule: The if-else block must move to the front of the for statement
"""

nums = [1, 2, 3, 4, 5]

# Label numbers as 'Even' or 'Odd'
labels = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(labels)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

"""
Variant D: Nested Loops (Flattening or Matrix creation)Runs multiple loops sequentially from left to right inside the brackets
"""

# Flattening a 2D matrix into a 1D flat list
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)  # Output: [1, 2, 3, 4]

# Step-by-step logic equivalent:
# for row in matrix:
#     for num in row:
#         flat.append(num)

"""
Speed Execution: List comprehensions run at C-speed inside Python's runtime environment because the appending process is optimized natively, making them faster than using .append() in a standard python loop.Local Scope Isolation: Variables defined inside the comprehension (like x in [x for x in nums]) do not leak into the rest of your program. They disappear once the line finishes running.
"""
raw_cities = [" New York  ", "london", "  PARIS "]
clean_cities = [city.strip().title() for city in raw_cities]
print(clean_cities)  # Output: ['New York', 'London', 'Paris']


users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
user_ids = [user for user in users] 
print(user_ids)  # Output: [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]


string_prices = ["10.50", "22.00", "4.99"]
float_prices = [float(p) for p in string_prices]
print(float_prices)  # Output: [10.5, 22.0, 4.99]


"""
 When NOT to Use List ComprehensionToo many steps: If your line requires multiple nested loops or 3+ conditional states, a regular for loop is better for readability. Clean code beats short code.Large Datasets (Memory Bottleneck): List comprehension builds the entire list in RAM instantly. If processing millions of rows, use a Generator Expression instead by changing the square brackets [] to round parentheses ()
"""