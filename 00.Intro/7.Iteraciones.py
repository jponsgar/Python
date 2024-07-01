# iter
def example_iter():
    """
    Crea un iterador a partir de un objeto iterable.
    """
    numbers = [1, 2, 3, 4]
    iterator = iter(numbers)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    print(iterator)
# >>> example_iter()
# <list_iterator object at 0x0000019EDC90F670>
# -------------------------------------------------------------------------------------
# next
def example_next():
    """
    Obtiene el siguiente elemento de un iterador.
    """
    numbers = iter([1, 2, 3])
    first = next(numbers)
    second = next(numbers)
    third = next(numbers)
    assert first == 1
    assert second == 2
    assert third == 3
    print(first)
    print(second)
    print(third)
# >>> example_next
# <function example_next at 0x0000019EDC935E40>
# -------------------------------------------------------------------------------------
# enumerate
def example_enumerate():
    """
    Devuelve un enumerador que contiene pares índice-valor.
    """
    fruits = ["apple", "banana", "cherry"]
    enumerated_fruits = list(enumerate(fruits))
    assert enumerated_fruits == [(0, "apple"), (1, "banana"), (2, "cherry")]
    print(enumerated_fruits)
# >>> example_enumerate()
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# -------------------------------------------------------------------------------------
# zip
def example_zip():
    """
    Empareja elementos de múltiples iterables.
    """
    names = ["Alice", "Bob", "Charlie"]
    ages =  [25, 30, 35]
    paired = list(zip(names, ages))
    assert paired == [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    print(paired)
# >>> example_zip()
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# -------------------------------------------------------------------------------------
# reversed
def example_reversed():
    """
    Devuelve un iterador que accede a los elementos en orden inverso.
    """
    numbers = [1, 2, 3, 4]
    reversed_numbers = list(reversed(numbers))
    assert reversed_numbers == [4, 3, 2, 1]
    print(reversed_numbers)
# >>> example_reversed()
# [4, 3, 2, 1]
# -------------------------------------------------------------------------------------
# sorted
def example_sorted():
    """
    Devuelve una lista ordenada a partir de un iterable.
    """
    numbers = [4, 2, 3, 1]
    sorted_numbers = sorted(numbers)
    assert sorted_numbers == [1, 2, 3, 4]
    print(sorted_numbers)
# >>> example_sorted()
# [1, 2, 3, 4]
# -------------------------------------------------------------------------------------
# filter
def example_filter():
    """
    Filtra elementos de un iterable que cumplen con una función.
    """
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    assert even_numbers == [2, 4]
    print(even_numbers)
# >>> example_filter()
# [2, 4]
# -------------------------------------------------------------------------------------
# map
def example_map():
    """
    Aplica una función a todos los elementos de un iterable.
    """
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    assert squared_numbers == [1, 4, 9, 16]
    print(squared_numbers)
# >>> example_map()
# [1, 4, 9, 16]