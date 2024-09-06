x = 10  # Global variable can be access anywhere 
def outer_function():
    print(f"Value of X in outer function {x}") 
    x = 20  # Enclosing variable
    #print(f"Value of X in enclosed function {x}")
    def inner_function():
        x = 30  # Local variable
        print(f"Value of X in enclosed function {x}")  # Output: 30
    inner_function()
    print(x)  # Output: 20

print(x) 
outer_function()
print(x)  # 10 aayega output (global variable)

    
