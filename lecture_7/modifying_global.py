# modifying global variable

counter=0
def increment():
    global counter
    counter=counter+1

increment()
print(counter)
