num1 = input(range())

def fizzbuzz():
    for num in num1():
        if num%3 == 0 and num%5 == 0:
            print("fizzbuzz")
        elif num%3 == 0:
            print("fizz")
        elif num%5 == 0:
            print('buzz')
        else:
            print(num)

print(fizzbuzz())