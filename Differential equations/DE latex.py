#import climage
# converts the image to print in terminal
# inform of ANSI Escape codes
#output = climage.convert('banana.jpg')
# prints output on console.
#print(output)
#from PIL import Image                                                                                
#img = Image.open('DE.png')
#img.show() 

from sympy import symbols, Eq, latex, cos, sin

def quadratic_formula(a, b, c):
    m1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    m2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return m1, m2

def quadratic_complex_formula(a, b, c):
    m = ((4*a*c - b**2)**0.5) / (2*a)
    n = -b / (2*a)
    return m, n

# Function to print equation in LaTeX format
def print_equation(latex_equation):
    print(latex_equation)

# Main function
def second_order_dif():
    # Define symbols
    x, A, B,e = symbols('x A B e')

    # Get input values
    a = int(input("Enter the value of d2y/dx2: "))
    b = int(input("Enter the value of dy/dx: "))
    c = int(input("Enter the value of y: "))

    if (b**2 - 4*a*c) > 0:
        m1, m2 = quadratic_formula(a, b, c)
        if int(m1) == 0:
            latex_equation = latex(A + B * e**(m2*x))
            print_equation(latex_equation)
        elif int(m2) == 0:
            latex_equation = latex(A + B * e**(m1*x))
            print_equation(latex_equation)
        else:
            latex_equation = latex(A * 2**(m1*x) + B * e**(m2*x))
            print_equation(latex_equation)

    elif int(b**2 - 4*a*c) == 0:
        m = (b**2 - 4*a*c) / (2*a)
        if int(m) == 0:
            latex_equation = latex(A + B*x)
            print_equation(latex_equation)
        else:
            latex_equation = latex((A + B*x) * e**m*x)
            print_equation(latex_equation)

    elif (b**2 - 4*a*c) < 0:
        m, n = quadratic_complex_formula(a, b, c)
        latex_equation = latex(e**n * (A*cos(m*x) + B*sin(m*x)))
        print_equation(latex_equation)

# Call the main function
second_order_dif()


    

    