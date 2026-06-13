try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")



def doSomeMagic(a):
    print(f"you know the name which starts with {a[0]} those people are really genius and they are really good at programming")

try:
    a = input("Enter your name: ")
    doSomeMagic(a)
except NameError as v:
    print("This function is not defined")

