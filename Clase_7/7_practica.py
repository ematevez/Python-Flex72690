"""Paso 1: Diseño del Diagrama de Clases
El sistema tiene las siguientes clases principales:

Vehículo (Clase base): Define atributos y métodos comunes a todos los vehículos.
Auto y Camioneta (Herencia simple): Heredan de Vehículo y especializan sus atributos y comportamientos.
Flota (Encapsulamiento): Maneja un conjunto de vehículos, protegiendo la lista interna.
Mantenimiento (Herencia múltiple): Gestiona los registros de mantenimiento, combinando funcionalidades de otras clases.
Implementación en Python
"""
# --- Gestión de Flota de Vehículos: Práctica Integral de POO ---

# ------------------------------------------------
# Clase Base: Vehículo
# ------------------------------------------------
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def describir(self):
        print(f"{self.marca} {self.modelo} ({self.anio})")

    def tipo_vehiculo(self):
        raise NotImplementedError("Este método debe ser implementado por subclases.")


# ------------------------------------------------
# Herencia Simple: Autos y Camionetas
# ------------------------------------------------
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, pasajeros):
        super().__init__(marca, modelo, anio)
        self.pasajeros = pasajeros

    def tipo_vehiculo(self):
        return "Auto"

    def capacidad(self):
        print(f"Este auto puede llevar hasta {self.pasajeros} pasajeros.")


class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, anio, carga):
        super().__init__(marca, modelo, anio)
        self.carga = carga

    def tipo_vehiculo(self):
        return "Camioneta"

    def capacidad(self):
        print(f"Esta camioneta puede cargar hasta {self.carga} kg.")


# ------------------------------------------------
# Encapsulamiento: Manejo de la Flota
# ------------------------------------------------
class Flota:
    def __init__(self):
        self.__vehiculos = []  # Lista interna protegida

    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.__vehiculos.append(vehiculo)
            print(f"Vehículo {vehiculo.marca} {vehiculo.modelo} agregado a la flota.")
        else:
            print("Error: Solo se pueden agregar objetos de tipo Vehiculo.")

    def listar_flota(self):
        print("\n--- Flota de Vehículos ---")
        for vehiculo in self.__vehiculos:
            vehiculo.describir()


# ------------------------------------------------
# Herencia Múltiple: Mantenimiento
# ------------------------------------------------
class Mantenimiento:
    def __init__(self):
        self.__registros = []  # Lista interna protegida

    def registrar_mantenimiento(self, vehiculo, descripcion):
        self.__registros.append((vehiculo, descripcion))
        print(f"Mantenimiento registrado para {vehiculo.marca} {vehiculo.modelo}.")

    def listar_mantenimientos(self):
        print("\n--- Historial de Mantenimiento ---")
        for vehiculo, descripcion in self.__registros:
            print(f"{vehiculo.marca} {vehiculo.modelo}: {descripcion}")


# ------------------------------------------------
# Polimorfismo: Gestión de Múltiples Tipos de Vehículos
# ------------------------------------------------
def procesar_vehiculo(vehiculo):
    print("\nProcesando Vehículo:")
    vehiculo.describir()
    print(f"Tipo: {vehiculo.tipo_vehiculo()}")
    vehiculo.capacidad()


# ------------------------------------------------
# Ejecución: Sistema de Flota
# ------------------------------------------------

# Crear vehículos
auto1 = Auto("Toyota", "Corolla", 2020, 5)
camioneta1 = Camioneta("Ford", "Ranger", 2019, 1000)

# Crear una flota y agregar vehículos
mi_flota = Flota()
mi_flota.agregar_vehiculo(auto1)
mi_flota.agregar_vehiculo(camioneta1)

# Listar flota
mi_flota.listar_flota()

# Crear sistema de mantenimiento
mantenimiento = Mantenimiento()
mantenimiento.registrar_mantenimiento(auto1, "Cambio de aceite.")
mantenimiento.registrar_mantenimiento(camioneta1, "Revisión general.")

# Listar mantenimientos
mantenimiento.listar_mantenimientos()

# Usar polimorfismo para procesar los vehículos
procesar_vehiculo(auto1)
procesar_vehiculo(camioneta1)

"""Explicación:
Clase Vehiculo: Es la clase base con métodos comunes, como describir y tipo_vehiculo.
Herencia simple: Las clases Auto y Camioneta heredan de Vehiculo y añaden métodos específicos (capacidad).
Encapsulamiento: La clase Flota protege la lista de vehículos con un atributo privado (__vehiculos) y métodos controlados.
Herencia múltiple: La clase Mantenimiento gestiona registros de mantenimiento protegidos (__registros).
Polimorfismo: La función procesar_vehiculo interactúa con diferentes tipos de vehículos de forma uniforme.
"""


"""
Vehículo Toyota Corolla agregado a la flota.
Vehículo Ford Ranger agregado a la flota.

--- Flota de Vehículos ---
Toyota Corolla (2020)
Ford Ranger (2019)

Mantenimiento registrado para Toyota Corolla.
Mantenimiento registrado para Ford Ranger.

--- Historial de Mantenimiento ---
Toyota Corolla: Cambio de aceite.
Ford Ranger: Revisión general.

Procesando Vehículo:
Toyota Corolla (2020)
Tipo: Auto
Este auto puede llevar hasta 5 pasajeros.

Procesando Vehículo:
Ford Ranger (2019)
Tipo: Camioneta
Esta camioneta puede cargar hasta 1000 kg.



"""