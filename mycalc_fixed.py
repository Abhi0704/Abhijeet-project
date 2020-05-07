def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y
#try catching the zzerodivisionerror by try and except method here
def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print("0, Anything you divide by 0 is always 0")
print("select 1 = add, 2 = subtraction, 3= multiplication, 4= divison")
choice = input("Enter your choice (1/2/3/4): ")
num1 = float(input("please enter your first number : "))
num2 = float(input("please enter your second number : "))
if choice == '1':
    print(num1,'+' , num2, '=' , add(num1,num2))
elif choice == '2':
    print(num1 , '-' , num2 , '=' , subtract(num1,num2))
elif choice == '3':
    print(num1 , '*' , num2 , '=' , multiply(num1,num2))
elif choice == '4':
    print(num1 , '/' , num2 , '=' , divide(num1,num2))
else:
    print("invalid choice PLease choose between 1,2,3,4")

