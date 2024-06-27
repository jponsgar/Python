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
