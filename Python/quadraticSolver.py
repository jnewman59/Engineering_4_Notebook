#quadratic solver
from math import sqrt
print('quadratic solver')
print('enter the coefficients of the quad. equation ax^2 + bx + c = 0')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
print( (lambda a, b, c: ("no real roots" if b**2-4*a*c<0 else ( -b/(2*a) if b**2-4*a*c==0 \
        else ([(-b+sqrt(b**2-4*a*c))/(2*a),(-b-sqrt(b**2-4*a*c))/(2*a)]) ) ) )(a, b, c) )
