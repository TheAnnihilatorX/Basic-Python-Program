#wap in py to demonstrate try and except using else
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"The result is {result}")

print("37.THIS PROGRAM IS WRITTEN BY Raghavv Gupta ERP :- 0221BCA032")