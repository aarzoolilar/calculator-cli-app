# Task 1 : Build a Calculator CLI App

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Error! Division by 0 is not allowed"
    return a/b

def main():
    print("*******************")
    print(" Simple calculator ")
    print("*******************")

    while True:
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = int(input("Enter choice(1-5)"))

        if choice == 5:
            print("Exiting calculator :)")
            break

        try: 
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))
            
            match choice:
                case 1:
                    print("Result : ", add(num1, num2))
                case 2:
                    print("Result : ", subtract(num1, num2))
                case 3:
                    print("Result : ", multiply(num1, num2))
                case 4:
                    print("Result : ", division(num1, num2))
                case _:
                    print("Invalid choice!!")

        except ValueError:
            print("Invalid input! Please enter numeric values")

if __name__ == "__main__":
    main()