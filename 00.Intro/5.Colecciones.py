# dict
def example_dict():
    # Crea un diccionario y accede a sus valores.
    # Son útiles cuando viene bien acceder por llave (key) a los datos (values)
    person = dict(name="Alice", age=30, city="New York") # objeto en JS
    user = {
        "name": "Pepe",
        "age" : "45",
        "city" : "New York",
        "id": 1
    }
    coche = {}
    coche["matricula"] = "GPT123"
    coche["año"] = 2099
    coche["color"] = "Blanco"
    assert person["name"] == "Alice"
    assert person["age"] == 30
    assert person["city"] == "New York"
    x = user.keys()
    print(x)
    print(coche)
    print(person)
# >>> example_dict()
# dict_keys(['name', 'age', 'city', 'id'])
# {'matricula': 'GPT123', 'año': 2099, 'datos': 'Blanco'}
# {'name': 'Alice', 'age': 30, 'city': 'New York'}
# -------------------------------------------------------------------------------------
# list
def example_list(fruta):
    # Crea una lista y accede a sus elementos.
    # Vienen bien cuando quiere acceder secuencialmente (en orden) a los datos
    # por índices
    # max_size: 536_870_912 por lista -> https://stackoverflow.com/questions/855191/how-big-can-a-python-list-get
    fruits = list(["apple", "banana", "cherry"]) # array en JS
    assert fruits[0] == "apple"
    assert fruits[1] == "banana"
    assert fruits[2] == "cherry"
    print(fruits)
# >>> example_list()
# ['apple', 'banana', 'cherry']
# -------------------------------------------------------------------------------------
# tuple
def example_tuple():
    # Crea una tupla y accede a sus elementos.
    # Vienen bien cuando queremos evitar que los datos se puedan modificar
    # Requiere reasignar variable para que se guarden otros datos
    colors = tuple(["red", "green", "blue"])
    assert colors[0] == "red"
    assert colors[1] == "green"
    assert colors[2] == "blue"
    print(colors)
# >>> example_tuple()
# ('red', 'green', 'blue')
# -------------------------------------------------------------------------------------
# set
def example_set(numero):
    # Crea un conjunto y verifica la pertenencia de un elemento.
    # Vienen bien para evitar duplicados en una colección => optimizados para esto
    numbers = set([1, 2, 3, 4, 5, 1, 1, 1, 1])
    mi_set = {1, 1, 1, 3} # {1, 3} -> forma corta
    assert numero in numbers, (f"El numero {numero} no existe.")
    print(f"El numero {numero} si está.")
# >>> example_set(1)
# El numero 1 si está.
# >>> example_set(7)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 6, in example_set
# AssertionError: El numero 7 no existe.
# -------------------------------------------------------------------------------------
# frozenset
def example_frozenset():
    # Crea un conjunto inmutable y verifica la pertenencia de un elemento.
    frozen_numbers = frozenset([1, 2, 3, 4, 5])
    assert 3 in frozen_numbers
    assert 6 not in frozen_numbers
    print(frozen_numbers)
# >>> example_frozenset()
# frozenset({1, 2, 3, 4, 5})