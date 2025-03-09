# Question 1: Basic Variable Manipulation
# #variables
name = "Alice"  
age = 25  

print(f"Hello, my name is {name} and I am {age} years old.")


# Question 2: User Input and Output
favorite_color = input("Enter your favorite color: ")

print(f"Your favorite color is {favorite_color}. That’s a great choice!")


# Question 3: Simple Calculator with Conditionals
# Asking user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asking user to choose an operation
operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

# Performing the selected operation
if operation == "add":
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == "divide":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of division is: {result}")
else:
    print("Invalid operation. Please choose from add, subtract, multiply, or divide.")



#Question 4: Even or Odd Checker
# Asking the user to enter a number
num = int(input("Enter a number: "))

# Checking if the number is even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")



#Question 5: Age-based Category Checker
# Asking user to enter their age
user_age = int(input("Enter your age: "))

# Categorizing based on age
if user_age < 13:
    print("You are a child.")
elif 13 <= user_age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")