# Without walrus
value = input("Enter something: ")
while value != "quit":
    print("You entered:", value)
    value = input("Enter something: ")

# With Walrus
while (value := input("Enter something: ")) != "quit":
    print("You entered:", value)

if (length := len("Hello world")) > 5:
    print(f"String is long ({length} characters)")