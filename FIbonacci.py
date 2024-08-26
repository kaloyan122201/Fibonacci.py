# Fibonaci chislata sa 3 , 3toto e suzdadeno ot kombinaciqta ot purvite 2 chisla
num1 = 0
num2 = 1
next_number = None
print("Let's me show you the Fibonnaci sequence!")
loops = int(input("How many sequences do you want to see?: "))
next_number = num1 + num2
for i in range(loops):
    print(f"{num1} + {num2} = {next_number}")
    num1 = num2
    num2 = next_number
    next_number = num1 + num2
