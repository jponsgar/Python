# bool 1
def example_bool(is_zero):
    # Convierte un valor en su valor booleano equivalente.
    is_true = bool(is_zero) # transforma el dato a False
    print(f"El valor {is_zero} se convierte a {is_true} en términos booleanos.")
    return is_true  # para 0 es False, para 1 es True
# Llamar a la función con el valor 0
#example_bool(0)    ->> False
#example_bool(1)    ->> True
# -------------------------------------------------------------------------------------
# bool 2
def example_bool(is_non_empty):
    # Convierte un valor en su valor booleano equivalente.
    is_non_empty = "Hola, no soy False"
    is_true = bool(is_non_empty) # transforma el dato a True
    print(f"El valor {is_non_empty} se convierte a {is_true} en términos booleanos.")
    return is_true  
# Puedes probar con...
#example_bool("Hola, no soy False")
#example_bool("")
#example_bool([])
#example_bool([1, 2, 3])
#example_bool(None)
# -------------------------------------------------------------------------------------
# int 1
def example_int(numero):
    # Convierte un valor en un entero.
    entero = int(numero)            # entero
    print(entero)
    return entero
# >>> example_int(4.0)
# 4
# 4
# -------------------------------------------------------------------------------------
# int 2
def example_int(numero):
    # Convierte un valor en un entero.
    num_hex = int(numero, base=16)  # base 16 (hex)
    print(num_hex)
    return num_hex
# example_int("a")
# 10
# 10
# -------------------------------------------------------------------------------------
# float
def example_float(numero):
    # Convierte un valor en un número flotante.
    flota = float(numero)
    print(flota)
    return flota
# >>> example_float(3)
# 3.0
# 3.0
# -------------------------------------------------------------------------------------
# complex
def example_complex(numero):
    # Convierte un valor en un número complejo.
    complejo = complex(numero)
    print(complejo)
    return complejo
# >>> example_complex(1+2j)
# (1+2j)
# (1+2j)
# -------------------------------------------------------------------------------------
# max
def example_max(numero):
    # Devuelve el valor máximo de una lista de valores.
    # max() acepta listas:
    mis_numeros = (1, 5, 3, 2, 7)
    num_maximo = max(mis_numeros) # 7
    assert num_maximo == numero, (f"El valor máximo es {num_maximo}")
    print(f"El valor máximo es {num_maximo}")
# >>> example_max(8)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 6, in example_max
# AssertionError: El valor máximo es 7
# >>> example_max(7)
# El valor máximo es 7
# >>>
# -------------------------------------------------------------------------------------
# min
def example_min(numero):
    #Devuelve el valor mínimo de una lista de valores.
    mis_numeros = (1, 5, 3, 7, 2)
    num_min = min(mis_numeros) # 1
    assert num_min == numero, (f"El valor mínimo es {num_min}")
    print(f"El valor mínimo es {num_min}")
# >>> example_min(7)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 5, in example_min
# AssertionError: El valor mínimo es 1
# >>> example_min(1)
# El valor mínimo es 1
# -------------------------------------------------------------------------------------
# divmod
def example_divmod(numero1, numero2):
    # Devuelve el cociente y el resto de una división.
    quotient, remainder = divmod(numero1, numero2)
    # print("La división de 7 / 3 con divmod devuelve:", divmod(7, 3)) # (2, 1)
    print(f"El cociente es {quotient}")
    print(f"El resto es {remainder}")
# >>> example_divmod(7,3)
# El cociente es 2
# El resto es 1
# -------------------------------------------------------------------------------------
# abs
def example_abs(numero):
    # Devuelve el valor absoluto de un número.
    absolute = abs(numero) # puede ser número negativo con decimales -5.0
    my_abs = abs(int(numero)) # hay que convertir a int o float
    print(f"El valor absoluto es {absolute}")
    print(f"El valor entero es {my_abs}")
# >>> example_abs(-5.0)
# El valor absoluto es 5.0
# El valor entero es 5
# -------------------------------------------------------------------------------------
# pow
def example_pow(numero, elevo):
    # Devuelve el resultado de elevar un número a una potencia.
    result = pow(numero, elevo) # 2**3=8 # 2**-1=0.5 # 2**0=1
    print(f"{numero} elevado a {elevo} es {result}")
# >>> example_pow(2,3)
# 2 elevado a 3 es 8
# >>> example_pow(2,-1)
# 2 elevado a -1 es 0.5
# >>> example_pow(2,0)
# 2 elevado a 0 es 1
# -------------------------------------------------------------------------------------
# round
def example_round(numero,decimales):
    # Redondea un número al entero más cercano.
    redeondeo = round(numero,decimales) # 3.14159, 2 # 2.99999, 3 # 2.55, 1
    print(f"El redondeo de {numero} con {decimales} decimales, es {redeondeo}")
# >>> example_round(3.14159, 2)
# El redondeo de 3.14159 con 2 decimales, es 3.14
# >>> example_round(2.99999, 3)
# El redondeo de 2.99999 con 3 decimales, es 3.0
# >>> example_round(2.55, 1)
# El redondeo de 2.55 con 1 decimales, es 2.5
# -------------------------------------------------------------------------------------
# sum
def example_sum():
    # Devuelve la suma de una lista de números.
    total = sum([1, 2, 3, 4, 5]) # recibe lista
    total_acumulado = sum([1, 2, 3, 4, 5], start=10) # start es una suma de partida
    print(f"La suma de [1, 2, 3, 4, 5] es {total}")
    print(f"La suma de [1, 2, 3, 4, 5] mas start=10 es {total_acumulado}")
# >>> example_sum()
# La suma de [1, 2, 3, 4, 5] es 15
# La suma de [1, 2, 3, 4, 5] mas start=10 es 25