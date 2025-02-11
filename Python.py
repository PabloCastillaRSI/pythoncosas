# Definición de variables
x = 10
y = 5
nombre = "Pablo"
es_estudiante = True

# Operadores lógicos
print("Operadores lógicos:")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"es_estudiante and x > y: {es_estudiante and x > y}")
print(f"es_estudiante or x < y: {es_estudiante or x < y}")
print()

# Bucles
print("Bucles:")
for i in range(5):
    print(f"for loop iteration {i}")

i = 0
while i < 5:
    print(f"while loop iteration {i}")
    i += 1
print()

# Listas
print("Listas:")
frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")
frutas.append("naranja")
print(f"Lista de frutas después de agregar naranja: {frutas}")
print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
print()

# Diccionarios
print("Diccionarios:")
persona = {
    "nombre": "Pablo",
    "edad": 30,
    "ciudad": "Madrid"
}
print(f"Diccionario persona: {persona}")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Ciudad: {persona['ciudad']}")
persona["edad"] = 31
print(f"Diccionario persona después de actualizar la edad: {persona}")

# Manejo de strings
print("Manejo de strings:")
saludo = "Hola, Mundo!"
print(f"String original: {saludo}")
print(f"Longitud del string: {len(saludo)}")
print(f"String en mayúsculas: {saludo.upper()}")
print(f"String en minúsculas: {saludo.lower()}")
print(f"Reemplazar 'Mundo' con 'Python': {saludo.replace('Mundo', 'Python')}")
print(f"Dividir el string por ',': {saludo.split(',')}")
print(f"Concatenar strings: {'Hola' + ' ' + 'Mundo'}")

# Funciones
print("Funciones:")
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(f"Suma de 3 y 4: {resultado}")
print()

# Condicionales
print("Condicionales:")
if x > y:
    print(f"{x} es mayor que {y}")
elif x < y:
    print(f"{x} es menor que {y}")
else:
    print(f"{x} es igual a {y}")
print()

# Manejo de archivos
print("Manejo de archivos:")
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de prueba.\n")

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(f"Contenido del archivo: {contenido}")

# Tuplas
print("Tuplas:")
tupla = (1, 2, 3, 4, 5)
print(f"Tupla: {tupla}")
print(f"Primer elemento: {tupla[0]}")
print(f"Último elemento: {tupla[-1]}")
print()

# Conjuntos
print("Conjuntos:")
conjunto = {1, 2, 3, 4, 5}
print(f"Conjunto: {conjunto}")
conjunto.add(6)
print(f"Conjunto después de agregar 6: {conjunto}")
conjunto.remove(3)
print(f"Conjunto después de eliminar 3: {conjunto}")
print()

# Comprensiones de listas
print("Comprensiones de listas:")
cuadrados = [x**2 for x in range(10)]
print(f"Cuadrados de 0 a 9: {cuadrados}")
print()

# Manejo de excepciones
print("Manejo de excepciones:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Bloque finally ejecutado")

# Clases y Objetos
print("Clases y Objetos:")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

persona = Persona("Pablo", 30)
print(persona.saludar())
print()

# Módulos e Importaciones
print("Módulos e Importaciones:")
# Crea un archivo llamado `modulo.py` con el siguiente contenido:
# def saludar(nombre):
#     return f"Hola, {nombre}!"

# Luego, en el archivo principal:
# from modulo import saludar
# print(saludar("Pablo"))

# Decoradores
print("Decoradores:")
def decorador(func):
    def nueva_funcion(*args, **kwargs):
        print("Función decorada")
        return func(*args, **kwargs)
    return nueva_funcion

@decorador
def funcion_simple():
    print("Función simple")

funcion_simple()

# Iteradores y Generadores
print("Iteradores y Generadores:")
def generador():
    for i in range(5):
        yield i

gen = generador()
for valor in gen:
    print(f"Generador produce: {valor}")
print()

# Expresiones Lambda
print("Expresiones Lambda:")
suma = lambda a, b: a + b
print(f"Suma usando lambda: {suma(3, 4)}")
print()

# Context Managers
print("Context Managers:")
class Recurso:
    def __enter__(self):
        print("Recurso adquirido")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Recurso liberado")

with Recurso() as recurso:
    print("Usando el recurso")

# Manejo de fechas y horas
print("Manejo de fechas y horas:")
from datetime import datetime, timedelta

ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")

manana = ahora + timedelta(days=1)
print(f"Fecha y hora de mañana: {manana}")

fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha y hora formateada: {fecha_formateada}")
print()

# Expresiones regulares
print("Expresiones regulares:")
import re

texto = "Mi número de teléfono es 123-456-7890"
patron = r"\d{3}-\d{3}-\d{4}"
coincidencia = re.search(patron, texto)

if coincidencia:
    print(f"Número de teléfono encontrado: {coincidencia.group()}")
else:
    print("Número de teléfono no encontrado")

# Manejo de argumentos de línea de comandos
print("Manejo de argumentos de línea de comandos:")
import sys

if len(sys.argv) > 1:
    print(f"Argumentos de línea de comandos: {sys.argv[1:]}")
else:
    print("No se pasaron argumentos de línea de comandos")
print()

# Serialización y deserialización
print("Serialización y deserialización:")
import json

# Serialización
persona = {
    "nombre": "Pablo",
    "edad": 30,
    "ciudad": "Madrid"
}
persona_json = json.dumps(persona)
print(f"Objeto JSON: {persona_json}")

# Deserialización
persona_obj = json.loads(persona_json)
print(f"Objeto Python: {persona_obj}")
print()

# Manejo de hilos (threads)
print("Manejo de hilos (threads):")
import threading

def tarea():
    print("Hilo en ejecución")

hilo = threading.Thread(target=tarea)
hilo.start()
hilo.join()
print("Hilo terminado")
print()

# Manejo de procesos (multiprocessing)
print("Manejo de procesos (multiprocessing):")
import multiprocessing

def tarea():
    print("Proceso en ejecución")

proceso = multiprocessing.Process(target=tarea)
proceso.start()
proceso.join()
print("Proceso terminado")
print()

# Programación asíncrona
print("Programación asíncrona:")
import asyncio

async def tarea():
    print("Tarea asíncrona en ejecución")
    await asyncio.sleep(1)
    print("Tarea asíncrona completada")

async def main():
    await asyncio.gather(tarea(), tarea())

asyncio.run(main())
print()

# Manejo de paquetes
print("Manejo de paquetes:")
# Crea un directorio llamado `mi_paquete` con un archivo `__init__.py` vacío y un archivo `modulo.py` con el siguiente contenido:
# def saludar(nombre):
#     return f"Hola, {nombre}!"

# Luego, en el archivo principal:
# from mi_paquete.modulo import saludar
# print(saludar("Pablo"))

# Manejo de bases de datos
print("Manejo de bases de datos:")
import sqlite3

# Conectar a la base de datos (o crearla)
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Insertar un registro
cursor.execute('''INSERT INTO usuarios (nombre, edad) VALUES ('Pablo', 30)''')

# Guardar los cambios
conexion.commit()

# Consultar registros
cursor.execute('''SELECT * FROM usuarios''')
usuarios = cursor.fetchall()
print(f"Usuarios: {usuarios}")

# Cerrar la conexión
conexion.close()
print()

# Pruebas unitarias
print("Pruebas unitarias:")
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 4), 7)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)
        self.assertNotEqual(suma(3, 4) == 8)

if __name__ == '__main__':
    unittest.main()


# Manejo de excepciones personalizadas
print("Manejo de excepciones personalizadas:")

class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def dividir(a, b):
    if b == 0:
        raise MiExcepcion("No se puede dividir por cero")
    return a / b

try:
    resultado = dividir(10, 0)
except MiExcepcion as e:
    print(f"Error: {e.mensaje}")
print()

# Documentación del código
print("Documentación del código:")

def suma(a, b):
    """
    Suma dos números.

    Args:
        a (int): El primer número.
        b (int): El segundo número.

    Returns:
        int: La suma de los dos números.
    """
    return a + b

print(suma(3, 4))
print()

# Manejo de dependencias
print("Manejo de dependencias:")
# Crear un entorno virtual
# python -m venv mi_entorno

# Activar el entorno virtual
# En Windows: mi_entorno\Scripts\activate
# En Unix o MacOS: source mi_entorno/bin/activate

# Instalar dependencias
# pip install nombre_paquete

# Guardar dependencias en un archivo requirements.txt
# pip freeze > requirements.txt

# Instalar dependencias desde un archivo requirements.txt
# pip install -r requirements.txt
print("Entorno virtual y dependencias manejadas con pip y virtualenv")
print()

# Manejo de configuraciones
print("Manejo de configuraciones:")
import os

# Usar variables de entorno
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '5432')

print(f"Conectando a la base de datos en {db_host}:{db_port}")

# Usar un archivo de configuración
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_host = config['database']['host']
db_port = config['database']['port']

print(f"Conectando a la base de datos en {db_host}:{db_port}")
print()