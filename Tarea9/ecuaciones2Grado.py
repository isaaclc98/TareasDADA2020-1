'''
ecuaciones2Grado.py
La formula chicharronera
'''

def chicharronera(a, b, c):
    d  = b * b - 4 * a * c #discriminante
    if d >= 0: #raices reales
        return ((-b + (d ** .5)) / (2.0 / a),
                (-b - (d ** .5)) / (2.0 / a))
    else:
        d = -d #raices complejas
        return (complex(-b, (d ** .5)) / (2.0 * a),
                complex(-b, -(d ** .5)) / (2.0 * a))

#pruebas
x1, x2 = chicharronera(10, 10, 6)
if x1 == x2:
    print ("Soluciones reales e iguales: x1 = x2 = %.2f" % x1)
elif type(x1) == complex:
    print ("Soluciones complejas y conjugadas x1 = %.2f+%.2fi x2 = %.2f+%.2fi" % (x1.real, x1.imag, x2.real, x2.imag))
else:
    print ("Soluciones reales y diferentes x1 = %.2f, x2 = %.2f" % (x1, x2))