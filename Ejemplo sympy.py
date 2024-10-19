import sympy as sp

# Definir variables simbólicas
x, y = sp.symbols('x y')

# 1. Simplificar una expresión algebraica
expr = (x**2 - 2*x + 1) / (x - 1)
simplified_expr = sp.simplify(expr)
print("Expresión simplificada:", simplified_expr)

# 2. Derivar una función simbólica
f = sp.sin(x) * sp.exp(x)
derivada = sp.diff(f, x)
print("Derivada de f:", derivada)

# 3. Integrar una función simbólica
integral = sp.integrate(sp.sin(x) * sp.exp(x), x)
print("Integral de f:", integral)

# 4. Resolver una ecuación algebraica
ecuacion = sp.Eq(x**2 - 4, 0)  # Ecuación: x^2 - 4 = 0
soluciones = sp.solve(ecuacion, x)
print("Soluciones de la ecuación:", soluciones)

# 5. Expansión y factorización de una expresión
expresion_a_expandir = (x + y)**3
expresion_expandida = sp.expand(expresion_a_expandir)
expresion_factorizada = sp.factor(expresion_expandida)
print("Expresión expandida:", expresion_expandida)
print("Expresión factorizada:", expresion_factorizada)
