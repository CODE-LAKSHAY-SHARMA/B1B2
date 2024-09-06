# Behavior of mutable and immutable arguments

def modify_immutable(x):
    
    x += 1
    print(f"Inside function: {x}")
      
a = 5
modify_immutable(a)
print(f"Outside function: {a}")  # Output: 5 unchanged rahega!!!
  
