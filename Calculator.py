import re

print("My AI Calculator")
print("Type 'end' to exit")

previous = 0
run = True

def solveMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter your equations:")
    else:
        equation = input(str(previous))

    if equation == "end":
        print("Adios Human!")
        run = False
    else:
        equation =re.sub('[a-zA-Z,.:()" "]', '',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)

while run:
    solveMath()