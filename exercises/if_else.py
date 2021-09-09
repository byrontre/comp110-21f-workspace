"""If-then-else example problems."""

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
else: 
    if choice < 50:  # includes >= 25
        print("B")
    else:
        if choice <= 75:  # includes >= 50
            print("D")
        else:
            print("C")