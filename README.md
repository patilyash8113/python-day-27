# python-day-27
Day 22 of python journey

Today i 

1) raising exception = in raising exception you can manually raise exception by using raise keyword. this is useful for signaling error condition in your own word.

lets understand it in simple words

eg. supose there is two inputs both asking user for number and we use if statement and type if : b==0 raise ValueError and print("please dont divide by zero")

and then i divide by some x value with 0 it show me valuerror and print like taht "Please dont divide by zero".



2) the else block is optional and is executed only if no exception occur within the try block.  It’s useful for code that should run only when the try block succeeds.

lets undestand it

eg. suppose i create try statement and inside of that statement i create a variable called a and a store x/y values. And then i create except statement with exception as e and print e after that i use an else statement and print("hey i am good") so whenever i try to print x/y it show me output like hey i am good but whenever i try x divide by zero it show me divison by zero.



3)finally :The finally block is also optional and is always executed, regardless of whether an exception occurred or not. It’s typically used for cleanup operations, such as closing files or releasing resources.



lets understand it

eg. suppose i create a function called divide and that divide method have two parameters a and b, and then I use try and create variable called c and that c stores x divide y and then i print c and return c and use except statement and write exception as e after thati print e and return none and use "Finally"  and print("ok")



and now ask user using input method that enter the values of x and y 

it give output z right ? thats right but it also give finally's print("ok")

thats where it use "finally" 

so now whenever i print output is always gives that ok no matter the division by zero error come it always shows me. the ok.

