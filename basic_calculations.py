def add (number_1 : float, number_2 : float) -> float :
    return number_1 + number_2

def sub (number_1 : float, number_2 : float) -> float :
    return number_1 - number_2

def mult (number_1 : float, number_2 : float) -> float :
    return number_1 * number_2

def div (number_1 : float, number_2 : float) -> float :
    return number_1 / number_2 

operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div,
}
