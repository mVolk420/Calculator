import basic_calculations

con = ""
result = 0
while True:
    if con != "y":
        number_1 = float(input("First Number: "))
    else:
        number_1 = result
    number_2 = float(input("Second Number: "))
    operator = input("pick an operator: ")
    result = basic_calculations.operations[operator](number_1, number_2)
    print(str(number_1) + " " + operator + " " + str(number_2) + " = " + str(result))
    con = input("type y to continue calculating with " + str(result)+ "or n for another calculation ")
