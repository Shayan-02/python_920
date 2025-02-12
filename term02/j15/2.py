# f(x) = 2x + 3 = y
def f(x: int) -> str:
    """
    This function returns the value of y given the value of x.
    
    parameters:
        x (int): voroodi
    
    returns:
        y (str): khorooji
    """
    y = (2 * x) + 3
    return y

# voroodi barname
x = int(input("enter a number: "))
print(f"do barabar e {f(x)} = {f(x) * 2}")