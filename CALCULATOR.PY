# CalCode - Calculator in Python 
while(1):
    print("\nCalCode - Calculator\nChoose a operation to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = int(input("\nEnter your choice (1-5): "))

    # Taking User Input only if choice is not equal to 5
    if(choice >=1 and choice<= 5):
        num1 = int(input("Enter 1st Number: "))
        num2 = int(input("Enter 2nd Number: "))
    
    # Performing Operations
    if choice == 1:
        print(f"\nAddition of {num1} + {num2} = {num1 + num2}")

    elif choice == 2:
        print(f"\nSubtraction of {num1} - {num2} = {num1 - num2}")

    elif choice == 3:
        print(f"\nMultiplication of {num1} x {num2} = {num1 * num2}")

    elif choice == 4:
        print(f"\nDivision of {num1} ÷ {num2} = {num1 / num2}")

    elif choice == 5:
        print("\nThank you for using CalCode. Goodbye!\n")
        break
    
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
