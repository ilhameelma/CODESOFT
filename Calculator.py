while True:
    # Input numbers with conversion to float
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue  # Restart the loop if input is invalid

    # Display the menu
    print("------------------ Calculator Menu ------------------")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit the calculator")
    print("-----------------------------------------------------")

    # Get user choice and convert to integer
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number between 1 and 5.")
        continue  # Restart the loop if the choice is invalid

    # Using match-case
    match choice:
        case 1:
            print("You chose Addition")
            result = a + b
            print(f"The result of the operation is {result}")

        case 2:
            print("You chose Subtraction")
            result = a - b
            print(f"The result of the operation is {result}")

        case 3:
            print("You chose Multiplication")
            result = a * b
            print(f"The result of the operation is {result}")

        case 4:
            print("You chose Division")
            if b == 0:
                print("Impossible to divide by zero")
            else:
                result = a / b
                print(f"The result of the operation is {result}")

        case 5:
            print("Goodbye!")
            break  # Exit the loop and stop the calculator

        case _:
            print("Invalid choice, please enter a number between 1 and 5.")
