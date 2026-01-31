# #try and except statement are used to handle Errors..
# while True:
#     try:
#         a=int(input("Enter the first number:"))
#         b=int(input("Enter the second number:"))

#         print(f"the divison of the number is {a/b}")

#     except ValueError:
#         print("please dont perform bad typecast")

#     except ZeroDivisionError:
#         print("hey dont divide by zero")

#     except :
#         print("Some error occured!")


# while True:
#     try:
#         a=int(input("Enter 1st number:"))
#         b=int(input("Enter 2nd number:"))
#         print(f"the divison is {a/b}")
#     except (ZeroDivisionError,ValueError) as e:
#         print(f"there is error: {e}")

# raising exception (raise)
 
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if b==0:
    raise ValueError("Please dont divide by 0")
print(f"the division is {a/b}") 


