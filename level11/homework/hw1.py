def calculator(x, y, op):
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y if y != 0 else "unknown value"
    
    return "unknown value"
 
