# exploring ID in both local and global variable

def modify(x):
    print(f"Before:{id(x)}")
    x=x+1
    print(f"After:{id(x)}")

a=5
modify(a)
