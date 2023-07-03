def quadratic_formula(a,b,c):
    m1=(-b+(b**2 -4*a*c)**0.5)/(2*a)
    m2=(-b-(b**2 -4*a*c)**0.5)/(2*a)
    return m1,m2
def quadratic_complex_formula(a,b,c):
    m=((4*a*c-b**2)**0.5)/(2*a)
    n=-b/(2*a)
    return m,n
#this is where the fun begins
a=int(input("Enter the value of d2y/dx2"))
b=int(input("Enter the value of dy/dx"))
c=int(input("Enter the value of y"))

if (b**2 -4*a*c) > 0:
    m1,m2=quadratic_formula(a,b,c)
    if int(m1) == 0:
        print(f"A + Be^({m2}x)")
    if int(m2) == 0:
        print(f"A + Be^({m1}x)")
    else:
        print(f"Ae^({m1}x) + Be^({m2}x)")
    
elif int(b**2 -4*a*c) == 0:
    m=(b**2 -4*a*c)/(2*a)
    if int(m) == 0:
        print("A+Bx")
    else:
        print(f"(A+Bx)e^{m}x")

elif (b**2 -4*a*c) < 0:
    m,n=quadratic_complex_formula(a,b,c)
    print(f"e^{n} (Acos({m}x)+Bsin({m}x))")

