# Fibonaci numbers are 3 in total
# The third one is created from the sum of the first two
num1 = 0
num2 = 1
# Just creating the 3rd number 
next_number = None
print("Let's me show you the Fibonnaci sequence!")
loops = int(input("How many sequences do you want to see?: "))
next_number = num1 + num2
for i in range(loops):
    print(f"{num1} + {num2} = {next_number}")
    num1 = num2
    num2 = next_number
    next_number = num1 + num2
