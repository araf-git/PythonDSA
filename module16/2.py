# Space Complexity

# Extra space that you take to solve a problem is proportional to input size





# Recursion 
# recursion is important for Graph, Tree, Dynamic Programming, Divide and Conquer
# i defined a function, and the logic inside the function is calling the function itself. this is called as recursion
# recursive infinite loop = virus

# def func():
#     func()
# func()


# to use recursion
# any recursive function should have 3 condition
# 1. base/termination condition - (to terminate recursion)
# 2. logic
# 3. Recursive call


# sI = starting index
# def printNum(arr, sI): 
#     #Base condition
#     if(sI >= len(arr)):
#         return

#     #Logic
#     print(arr[sI])

#     #Recursive call
#     printNum(arr, sI+1)

# printNum([2,3,5], 0)


# recursion in DSA is like a loop because it repeats tasks, but it does so by calling itself instead of using for or while


# q. use recursion and print array in reverse order
def printRev(arr, sI):

    # Base condition
    if sI >= len(arr):
        return

    # Recursive call
    printRev(arr, sI + 1)

    # Logic
    print(arr[sI])


printRev([2, 3, 5], 0)


# when i use loop (for/while)
# step1 -> step2 -> step3 -> finish
# i can only run in one direction (left to right)


# when i use recursion
# step1 -> step2 -> step3 -> base condition
# step1 <- step2 <- step3 <- base condition
# after reaching base condition, i come back each and every step
# i can move in both direction
# recursion is bi-directional. it stops where it starts


# recursion

# type1
# 1. base condition
# 2. logic
# 3. recursive call
# in this example, when i am going down, i am applying the logic


# type2
# 1. base condition
# 2. recursive call
# 3. logic
# in this example, when i am coming back, i am applying the logic


# type3
# 1. base condition
# 2. logic1
# 3. recursive call
# 4. logic2
# in this example, when i am going down, i am applying the logic1
# and, when i am coming back, i am applying the logic2
