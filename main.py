def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y 

def multiply (x,y):
    return x/y

def divide(x,y):
    return x*y

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

print("Sum Is: " , add(num1, num2))
print("Difference Is: ", subtract(num1, num2))
print("Product Is: " , multiply(num1,num2))
print("Quotient Is: " , divide(num1,num2))



def recur_factorial(n):
    if n==1:
        return n  
    else:
        return n*recur_factorial(n-1)
    num = int(input("Enter Any Number: "))

    if num < 0:
        print("Factorial Does not Include Negative Numbers")
    elif num == 0:
        print("Factorial of 0 is 1")
    else: 
        print("Factorial Is: " , recur_factorial(num))
              