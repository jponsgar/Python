# Concatenación
hola = "Hola, "
msg = "mundo"
print(hola + msg)
# >>> Hola, mundo
# -------------------------------------------------------------------------------------
# No se puede sumar o concatenar tipos incompatibles:
1 + '1' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# -------------------------------------------------------------------------------------
# Se puede sumar números:
1 + 1.0 # 2.0
# -------------------------------------------------------------------------------------
# Solo puedes concatenar si tienes str:
"Teléfono: " + str(123456789)  # 'Teléfono: 123456789'
# -------------------------------------------------------------------------------------
# Funciones
def saludar():
  print("Hola!")
# >>> saludar()
# >>> Hola!
