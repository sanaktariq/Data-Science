x = int(input("What is your first number?: "))
y = int(input("What is your second number?: "))

print("""
Choose an operation:
1.add
2.subtract
3.multiply
4.divide
""")

choice = input("Enter choice(1, 2, 3, 4): ")

def add(x,y):
   return x + y

def subtract(x,y):
   return x - y

def multiply(x,y):
   return x * y

def divide (x,y):
   return x / y

if choice == '1':   
    print(add(x,y))

elif choice == '2':
    print(subtract(x,y))

elif choice == '3':
    print(multiply(x,y))

elif choice == '4':
    print(int(divide(x,y)))

else:
    print("This operation is not allowed")







