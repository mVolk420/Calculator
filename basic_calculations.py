def add (number_1 : float, number_2 : float) -> float :
    return number_1 + number_2

def sub (number_1 : float, number_2 : float) -> float :
    return number_1 - number_2

def mult (number_1 : float, number_2 : float) -> float :
    return number_1 * number_2

def div (number_1 : float, number_2 : float) -> float :
    return number_1 / number_2 

def calculate (number_1 : float, number_2: float, operator : str):
    if operator == "+":
        return add(number_1, number_2)
    elif operator == "-":
        return sub(number_1, number_2)
    elif operator == "*":
        return mult(number_1, number_2)
    
    return div(number_1, number_2)