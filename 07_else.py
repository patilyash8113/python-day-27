
try:
    a=325/0
except Exception as e:
    print(e)
#gets executed when there is not a error in the try block
else:
    print("Hey i am good")

# def check_age(age):
#     if age<18:
#         raise ValueError ("Age must be under 18")
#     return "access granted!"
# try:
#     # print(check_age(20))
#     print(check_age(15))
# except Exception as e:
#     print(f"Error:{e}")