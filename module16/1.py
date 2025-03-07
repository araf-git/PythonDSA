# Time Complexity

# Data er sathe 2 ta jinish kori
# 1. Data Store korte chai
# 2. Data'r upor complex Computation/Algorithm chalai

# In the modern world
# the amount of data is huge
# so
# i want the storage to be effecient. kom space e beshi data store korte chai
# i want the computation to be super fast

# Data Structure ekhane help kore

# Data Structure
# 1. Structuring data so that storage become efficient
# 2. faster computation



# Data Structure is 2 types
# 1. Linear Data Structure
# 2. Non Linear Data Structure


# 1. Linear DS
    #  - Storing Data in one dimension(linear) . example: array, linked list, queue, stack

# 2. Non Linear DS
    #  - Storing Data in multiple dimension . example: Tree, PQ, Graph, Map/Dictionary


# Algorithm
# q. what is algorithm?
# ans: i have a problem and i want to solve it. the logical steps that i take to solve this problem is Algorithm
# a problem can have multiple solutions
# so to solve a problem, there can be multiple algorithm's
# some algorithm can be good, some may be bad.
# so i need to know which algorithm is better
# i need to analyze algorithm 
# one of the tools that we use to analyze the algorithm is time complexity


# Time Complexity definition
# 1. should be independent of programming language
# 2. independent of operating system/processor

# Time Complexity definition
# How the number of operations are proportional to the input size
# no of operation = how many time the loop will run

# def func(n): 
#     for i in range(n): 
#         print('Hello')

# func(1)
# func(10)

#     # if n = 1, hello will be printed 1 times, operation = 1
#     # if n = 10, hello will be printed 10 times, operation = 10

#     so no of operations proportional to n
#     or no of operations are proportional to n and grow linearly
#     so TC = O(n) = Order of n (Big O Notation)





# TC have 3 case
# 1. best
# 2. average
# 3. worst

# TC = O(n) = Big O Notation is the worst case
# by TC we calculate the worst case. cause if my software performes good at worst case, it will automatically perform best at the best case









# Here are more time complexities to know:

# O(1): Constant time — The operation doesn’t depend on the input size.
# O(n): Linear time — Operations grow directly with input size (e.g., simple loops).
# O(log n): Logarithmic time — Operations grow slower as input size increases (e.g., binary search).
# O(n²): Quadratic time — Operations grow with the square of the input size (e.g., bubble sort).
# For most DSA, focusing on O(1), O(n), O(log n), O(n²) will cover most cases.



# O(n log n): Log-linear time — Common in efficient sorting algorithms (e.g., merge sort).
# O(2ⁿ): Exponential time — Operations grow exponentially with input size (e.g., brute-force solutions to some problems).
# O(n³): Cubic time — Operations grow with the cube of the input size (e.g., 3 nested loops).
# O(n!): Factorial time — Operations grow with the factorial of the input size (e.g., brute-force solutions for permutations).
# O(√n): Square root time — Operations grow with the square root of the input size (e.g., some algorithms for searching or number theory).
# These are helpful for more complex algorithms.
# For most DSA, O(n), O(log n), O(n²), and O(1) will be enough.





















# Common Time Complexities

# 1. O(1) (Constant Time)
# No dependence on input size.
# def constant(n):
#     print("Hello")  # 1 operation, regardless of n
# constant(100)  # 1 op
# constant(1000) # 1 op




# 2. O(n) (Linear Time)
# Operations scale linearly with input size.
# def linear(n):
#     for i in range(n):  # Runs n times
#         print("Hello")
# linear(5)  # 5 ops
# linear(20) # 20 ops




# 3. O(log n) (Logarithmic Time)
# Operations grow slowly (halved at each step).
# def logarithmic(n):
#     i = 1
#     while i < n:
#         print("Hello")
#         i *= 2  # Loop runs log₂(n) times
# logarithmic(8)  # 3 ops (log₂(8) = 3)
# logarithmic(16) # 4 ops





# 4. O(n²) (Quadratic Time)
# Operations scale with the square of input size.
# def quadratic(n):
#     for i in range(n):      # Runs n times
#         for j in range(n):  # Runs n times
#             print("Hello")  # Total: n × n = n² ops
# quadratic(2)  # 4 ops
# quadratic(3)  # 9 ops






# Advanced Time Complexities


# 5. O(n log n) (Log-Linear Time)
# Common in efficient sorting algorithms.
# def log_linear(n):
#     for i in range(n):      # Runs n times
#         j = 1
#         while j < n:        # Runs log₂(n) times per outer loop
#             print("Hello")
#             j *= 2          # Total: n × log₂(n) ops
# log_linear(4)  # 4 × 2 = 8 ops
# log_linear(8)  # 8 × 3 = 24 ops



# 6. O(2ⁿ) (Exponential Time)
# Operations double with each step (e.g., recursive Fibonacci).
# def exponential(n):
#     if n <= 1:
#         return
#     exponential(n-1)  # Two recursive calls per step → ~2ⁿ ops
#     exponential(n-1)
# exponential(3)  # 7 ops
# exponential(4)  # 15 ops



# 7. O(n³) (Cubic Time)
# Three nested loops (e.g., matrix multiplication).
# def cubic(n):
#     for i in range(n):        # n × n × n = n³ ops
#         for j in range(n):
#             for k in range(n):
#                 print("Hello")
# cubic(2)  # 8 ops
# cubic(3)  # 27 ops



# 8. O(n!) (Factorial Time)
# Generating all permutations of a list.
# def factorial(n, prefix=[]):
#     if n == 0:
#         print(prefix)  # n! permutations (extremely slow for large n)
#         return
#     for i in range(n):
#         factorial(n-1, prefix + [i])
# factorial(2)  # 2! = 2 ops
# factorial(3)  # 6 ops



# 9. O(√n) (Square Root Time)
# Checking if a number is prime.
# def square_root(n):
#     for i in range(2, int(n**0.5) + 1):  # Runs √n times
#         if n % i == 0:
#             return False
#     return True
# square_root(16)  # Checks up to 4 → 3 ops
# square_root(25)  # Checks up to 5 → 4 ops



# Key Takeaways
# Focus on O(1), O(n), O(log n), and O(n²) for most coding interviews.
# Use O(n log n) for sorting discussions (e.g., merge sort).
# Avoid O(2ⁿ) and O(n!) unless explicitly required (they’re impractical for large inputs).

































# For DSA in Python and MERN stack development, focusing on O(1), O(n), O(log n), and O(n²) is sufficient for most practical scenarios, but here’s the nuance:

# Why These Are Enough?
# O(1):

# Used for hash maps/dictionaries (Python), accessing arrays by index, or cached operations.

# Example: dict[key] in Python, or localStorage.getItem() in MERN.

# O(n):

# Common in loops, API calls fetching lists, or traversing arrays/linked lists.

# Example: Filtering a list of users in React or processing MongoDB query results.

# O(log n):

# Critical for efficient searches (binary search) or tree operations (BSTs, heaps).

# Example: Searching a sorted array in Python or indexing in MongoDB.

# O(n²):

# Seen in nested loops, brute-force comparisons, or simple sorting (bubble sort).

# Example: Comparing all pairs of items in a cart (avoid in production for large n!).

# Where You Might Need More
# O(n log n):

# Used in sorting (merge sort, quick sort).

# Example: Sorting data in Python with .sort() (Timsort) or optimizing MongoDB queries.

# Key for interviews, even if labeled "advanced".

# O(√n) or O(2ⁿ):

# Rare in web dev, but useful for niche number theory (primality checks) or recursive backtracking (small n only).

# MERN Stack Specifics
# Frontend (React): Most operations are O(n) (rendering lists) or O(1) (state updates). Avoid O(n²) in renders (e.g., nested loops).

# Backend (Node.js): Focus on O(n)/O(log n) for scalable APIs (e.g., database queries with indexes).

# MongoDB: Indexed queries are O(log n); unindexed scans are O(n).

# Yes, O(1), O(n), O(log n), and O(n²) cover 90% of DSA needs in Python/MERN.

# Add O(n log n) for sorting/optimization questions in interviews.

# Avoid O(n²) in production for large datasets (optimize to O(n) or O(n log n)).