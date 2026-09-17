try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("What operation do you want to perform?\n"
          "Press + for addition\nPress - for subtraction\n"
          "Press * for multiplication\nPress / for division\n")

    o = input("Enter Operation: ").strip()

    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            if b == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"The result is: {a / b}")
        case _:  
            print("Invalid operation selected.")

except ValueError:
    print("Please enter valid numeric values for a and b.")