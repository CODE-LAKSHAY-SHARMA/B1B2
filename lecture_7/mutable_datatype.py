# mutable object modification in function
def modify_mutable(lst):
    lst.append(4)
    print(f"Inside function: {lst}")


my_list = [1, 2, 3]
modify_mutable(my_list)
print(f"Outside function: {my_list}")  # Output: [1, 2, 3, 4] (modified)
