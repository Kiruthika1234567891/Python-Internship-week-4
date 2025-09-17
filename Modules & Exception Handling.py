#____---------------MODULES & EXCEPPTION HANDLING-----------------_______________

# _______MATH MODULE TO CALC SQUARE ROOT______
# import math
# n = float(input("Enter a number:"))
# result = math.sqrt(n)
# print(f"The square root of {n} is {result:.2f}")

# ______DATETIME MODULE TO PRINT TODAY'S DATE & TIME_______
# import datetime
# now = datetime.datetime.now()
# print(f"Today's Date & Time:{now}")
# # or       
# print(f"Today's Date & Time:{now.strftime('%y-%m-%d %H:%M:%S')}")

# ____________MODULE Calc.py with FUNCTIONS(add,sub,multi,divide) & IMPORT_________
# NOTE: For execution, create calc.py and main.py in the project folder and run main.py.
# def add(a,b):
#     return a + b
# def sub(a,b):
#     return a - b
# def multiply(a,b):
#     return a * b
# def divide(a,b):
#     if b == 0:
#         return "Error!Division by Zero."
#     return a / b

# import calc
# x = float(input("Enter a number:"))
# y = float(input("Enter a number:"))
# print("Add:",calc.add(x,y))
# print("Subtract:",calc.sub(x,y))
# print("Multiply:",calc.multiply(x,y))
# print("Divide:",calc.divide(x,y))

# ______PROGRAM TO HANDLE DIVISION BY ZERO with TRY/EXCEPT_______
# try:
#     x = int(input("Enter a numerator:"))
#     y = int(input("Enter a denominator:"))
#     result = x/y
#     print("Result:",result)
# except ZeroDivisionError:
#     print("Error!Division by Zero.")

# ______PROGRAM that RAISES a CUSTOM EXCEPTION IF MARKS < 35_______
# class FailException(Exception):
#     def __init__(self,marks):
#         super().__init__(f"Fail!.Your mark {marks} is less than 35.")  
# try:
#     marks = int(input("Enter the mark:"))
#     if  marks < 35:
#         raise FailException(marks)
#     else:
#         print(f"Pass!.Your mark is:",marks) 
# except FailException as fail:
#     print(fail)                