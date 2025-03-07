# Variables in functions (Global & Local Scope)

x = 101 #Global Variable/scope

def func():
  x = 102 #local/function scope
  print(x)

func()
print(x)

# when a function execution is complete, the local/function variable gets destroyed

