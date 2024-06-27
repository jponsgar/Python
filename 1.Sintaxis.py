# Sintaxis
print("Hola, mundo") # se ejecuta en servidor, ordenador local, etc. No en "cliente" ( -> navegador de usuario )
# Python es de alto nivel, aprox con entender las palabras en inglés se entiende el propósito del programa
# Python <> se usa en backend:
# - Sintaxis simple
# - Mucha comunidad -> proyectos open source
# - Flexible para hacer cualquier tipo de desarrollo -> backend: base de datos,
# APIs, servir archivos, lógica de backend, IA...
# -------------------------------------------------------------------------------------
print("suma:", 1+1)
if 5 > 2:
  print("Five is greater than two!")
# Python no tiene {} -> usa indentación
# -------------------------------------------------------------------------------------
edad = 14
if edad > 18:
  print("Eres mayor de edad")
else:
  print("No eres mayor de edad")
# -------------------------------------------------------------------------------------
string = "Esto es un string"
numero = 1.5
string
numero
# -------------------------------------------------------------------------------------
# Esto es un comentario de 1 línea
"""
   Comentario
   mutilínea
"""
'''otro comentario'''
# -------------------------------------------------------------------------------------
# Variables
x = str(3)    # '3'
y = int(3)    # 3
z = float(3)  # 3.0
print(type(x), type(y), type(z))   # <class 'str'> <class 'int'> <class 'float'>
x
y
z
x = False # reasigno x a boolean
x
print(type(x), type(y), type(z))   #<class 'bool'> <class 'int'> <class 'float'>
# -------------------------------------------------------------------------------------
# En JS se usa el camelCase: `miVariableDeJs`
# En Python se usa el snake_case: `mi_variable_de_python`
# Snake case
mi_variable_python = "Python mola!"
# -------------------------------------------------------------------------------------
# Asignación múltiple
x, y, z = "X", "Y", "Z"
print(x, y, z)  # X Y Z