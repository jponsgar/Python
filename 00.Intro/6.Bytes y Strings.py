# bytes
def example_bytes():
    #Crea un objeto de bytes a partir de una cadena.
    # No editable
    data = bytes("Hello", "utf-8") # por defecto codificación utf-8
    emoji = bytes("😐", "utf-8") # utf-8
    assert data == b'Hello'
    assert emoji == b'\xF0\x9F\x98\x90' # se puede pasar a binario
    # \xF0\x9F\x98\x90 equivale a: 11110000 10011111 10011000 10010000
    # Convertir los bytes a su representación binaria
    binary_representation = ''.join(format(byte, '08b') for byte in emoji)
    print(binary_representation)
# >>> example_bytes()
# 11110000100111111001100010010000
# -------------------------------------------------------------------------------------
# bytearray
def example_bytearray():
    # Crea un bytearray modificable a partir de una cadena.
    # Editable
    data = bytearray("Hello", "utf-8")
    data[0] = ord('h') # se cambia por repr de h minúscula
    print("ord de h", data[0]) # 104 es el número de caracter de la h
    print("ord de H", ord("H"))
    assert data == b'hello'
    print(data)
# >>> example_bytearray()
# ord de h 104
# ord de H 72
# bytearray(b'hello')
# -------------------------------------------------------------------------------------
# str
def example_str():
    # Convierte un valor en una cadena.
    # No podemos usar str como nombre de variable en Python: my_str, mi_str, text, etc.
    number = str(123)
    assert number == "123"
    print(number)
# >>> example_bytearray()
# ord de h 104
# ord de H 72
# bytearray(b'hello')
# -------------------------------------------------------------------------------------
# memoryview
def example_memoryview():
    # Crea una vista de memoria a partir de un objeto de bytes.
    # Representación en bytes de los datos en memoria -> manipular datos a más bajo nivel
    data = memoryview(bytes("Hello", "utf-8"))
    assert data[0] == 72
    assert data[1] == ord('e')
    print(data)
# >>> example_memoryview()
# <memory at 0x0000019EDC4353C0>
# -------------------------------------------------------------------------------------
# open
def example_open():
    """
    Abre un archivo para leer y escribir.
    Flags:
    w para escritura (write)
    r para lectura (read)
    a para append (apppend) -> añadir al final
    """
    # Escritura -> sobreescribe el archivo <-
    with open("example.txt", "w") as file:
        file.write("Hello, World!")
    # Añade al final del archivo sin borrar lo anterior
    with open("example.txt", "a") as file:
        file.write("\nEsto es otra línea")
    # Lectura:
    with open("example.txt", "r") as file:
        content = file.read()
    print("Contenido:", content)
    assert content.startswith("Hello, World!")
# PermissionError: [Errno 13] Permission denied: 'example.txt'
# -------------------------------------------------------------------------------------
# bin
def example_bin():
    """
    Convierte un número en su representación binaria.
    Empieza por 0b, eso no es parte del binario
    """
    binary = bin(10) # 8 + 2 = 2**3 + 2**1 -> 1010
    assert binary == "0b1010"
    print(binary)
# >>> example_bin()
# 0b1010
# -------------------------------------------------------------------------------------
# oct
def example_oct():
    """
    Convierte un número en su representación octal.
    """
    octal = oct(10) # 8 + 2 = 8 * 1 + 2
    assert octal == "0o12"
    print(octal)
# >>> example_oct()
# 0o12
# -------------------------------------------------------------------------------------
# hex
def example_hex():
    """
    Convierte un número en su representación hexadecimal.
    """
    hexadecimal = hex(10) # 0..9 y el 10 es A
    assert hexadecimal == "0xa"
    print(hexadecimal)
# >>> example_hex()
# 0xa
# -------------------------------------------------------------------------------------
# input
def example_input():
    """
    Lee una cadena desde la entrada estándar (simulada aquí).
    """
    # Usamos input() normalmente, pero aquí lo simulamos.
    # Descomentar para recibir datos:
    # Leer un str
    # mensaje = input("Escribe un mensaje: ")
    # print(float(mensaje)) # str
    # Leer un float
    # numero = float(input("Escribe un número: "))
    # print(numero)
    user_input = "Hello, World!"
    assert user_input == "Hello, World!"
    print(user_input)
# >>> example_input()
# Hello, World!
# -------------------------------------------------------------------------------------
# chr
def example_chr():
    """
    Devuelve el carácter correspondiente al valor Unicode dado.
    """
    character = chr(65)
    assert character == 'A'
    print(character)
# >>> example_chr()
# A
# -------------------------------------------------------------------------------------
# ord
def example_ord():
    """
    Devuelve el valor Unicode de un carácter dado.
    """
    unicode_value = ord('A')
    assert unicode_value == 65
    print(unicode_value)
# >>> example_ord()
# 65
# -------------------------------------------------------------------------------------
# format
def example_format():
    """
    Formatea un valor usando una cadena de formato.
    """
    PI = 3.14159
    # PI * 2 ** 2
    formatted = format(PI, ".2f") # en str solo salen 2 decimales
    assert formatted == "3.14"
    print(formatted)
# >>> example_format()
# 3.14
# -------------------------------------------------------------------------------------
# ascii
def example_ascii():
    """
    Devuelve una representación imprimible de un objeto.
    """
    representation = ascii("ä")
    assert representation == "'\\xe4'"
    print(representation)
# >>> example_ascii()
#'\xe4'
# -------------------------------------------------------------------------------------
# repr
class Coche:
  matricula = "GPT123"
  def __repr__(self):
    return "Coche con matrícula: " + self.matricula
mi_dict = {
    "algo": "valor",
    "otra cosa": "otro valor"
}
def example_repr():
    """
    Devuelve una representación de cadena de un objeto.
    """
    coche = Coche()
    # La repr (representation) no nos muestra los datos si no hay
    # un método __repr__
    print(repr(coche))
    # La repr (representation) nos muestra los datos:
    print(repr(mi_dict))
    representation = repr("Hello\nWorld")
    assert representation == "'Hello\\nWorld'"
