# write a python program to swap values of two variables using various methods

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
 
temp = x
x = y
y = temp

x,y = y,x

x = x+y
y = x-y
x = x-y

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
print("28.THIS PROGRAM IS WRITTEN BY Raghavv Gupta ERP :- 0221BCA032")