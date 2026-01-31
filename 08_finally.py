
# def divide(a,b):
    
#     try:
#         c=a/b
#         print(c)
#         return c
#     except Exception as e:
#         print(e)
#         return None
#     finally: # This will always executed no matter if try completely execute or not..
#         print("This is always executed")

# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# divide(a,b)

def divide (a,b):
    try:
        c=a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    finally:
        print("thik ahhe tar")

a=int(input("Enter the first number:"))
b=int(input("Enter second number:"))
divide(a,b)