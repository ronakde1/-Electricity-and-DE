def quadratic_formula(a,b,c):
    m1=(-b+(b**2 -4*a*c)**0.5)/(2*a)
    m2=(-b-(b**2 -4*a*c)**0.5)/(2*a)
    return m1,m2
def quadratic_complex_formula(a,b,c):
    m=((4*a*c-b**2)**0.5)/(2*a)
    n=-b/(2*a)
    return m,n
#this is where the fun begins
a=int(input("Enter the value of d2y/dx2 "))
b=int(input("Enter the value of dy/dx "))
c=int(input("Enter the value of y "))
print("Enter 0 if no value for each ")
Y2=int(input("Enter value of x^2 coefficient "))
Y1=int(input("Enter value of x coefficient "))
Y0=int(input("Enter value of constant "))
#x^2
p=Y2/a
#x
q=(Y1-2*b*p)/a
#constant
r=(Y0-2*c*p-b*q)/a
x=f"+ {p}x^2 + {q}x + {r}"

if (b**2 -4*a*c) > 0:
    m1,m2=quadratic_formula(a,b,c)
    if int(m1) == 0:
        print(f"A + Be^({m2}x) {x}")
    if int(m2) == 0:
        print(f"A + Be^({m1}x) {x}")
    else:
        print(f"Ae^({m1}x) + Be^({m2}x) {x}")
    
elif int(b**2 -4*a*c) == 0:
    m1,m2=quadratic_formula(a,b,c)
    if int(m1) == 0:
        print(f"A+Bx {x}")
    else:
        print(f"(A+Bx)e^{m1}x {x}")

elif (b**2 -4*a*c) < 0:
    m,n=quadratic_complex_formula(a,b,c)
    print(f"e^{n} (Acos({m}x)+Bsin({m}x)) {x}")

