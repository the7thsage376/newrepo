# Basic calculator program
print("Enter your numbers for basic calculations")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
Math_Operation=input("Enter your math operation: ")

# If statements for arithmetic operations
if(Math_Operation == '+'):
    print(f'{num1} + {num2} results to {num1 + num2}' )
elif(Math_Operation == '-'):
      print(f'{num1} - {num2} results to {num1 - num2}' )
elif(Math_Operation == '*'):
       print(f'{num1} * {num2} results to {num1 * num2}' )
elif(Math_Operation == '/'):
        print(f'{num1} / {num2} results to {num1 / num2}' )