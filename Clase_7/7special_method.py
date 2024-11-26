class SpecialMethodsDemo:
    # __init__: Método constructor
    def __init__(self, name, value):
        self.name = name
        self.value = value

    # __str__: Representación amigable para usuarios
    # def __str__(self):
    #     return f"Item: {self.name}, Value: {self.value}"

    # __repr__: Representación para desarrolladores
    def __repr__(self):
        return f"SpecialMethodsDemo(name={self.name!r}, value={self.value!r})"

    # __add__: Suma entre objetos
    def __add__(self, other):
        if isinstance(other, SpecialMethodsDemo):
            return self.value + other.value
        return NotImplemented

    # __len__: Retorna la longitud del nombre
    def __len__(self):
        return len(self.name)

    # __eq__: Compara objetos por valor
    def __eq__(self, other):
        if isinstance(other, SpecialMethodsDemo):
            return self.value == other.value and self.name == other.name
        return NotImplemented

    # __getitem__: Acceso a valores simulando una lista
    def __getitem__(self, index):
        return (self.name, self.value)[index]

    # __call__: Hace que el objeto sea invocable
    def __call__(self):
        return f"Calling {self.name} with value {self.value}"


# Ejemplos de uso
if __name__ == "__main__":
    # __init__, __str__, __repr__
    item1 = SpecialMethodsDemo("Item1", 10)
    item2 = SpecialMethodsDemo("Item2", 20)
    print("=======================================")
    print(item1)  # Item: Item1, Value: 10
    
    print(repr(item1))  # SpecialMethodsDemo(name='Item1', value=10)

    # __add__
    print(item1 + item2)  # 30

    # __len__
    print(len(item1))  # Longitud de "Item1" => 5

    # __eq__
    item3 = SpecialMethodsDemo("Item1", 10)
    print(item1 == item3)  # True

    # __getitem__
    print(item1[0])  # "Item1"
    print(item1[1])  # 10

    # __call__
    print(item1())  # Calling Item1 with value 10
