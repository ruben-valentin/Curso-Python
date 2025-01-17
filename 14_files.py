import os
import json
import csv

# ========================
# Trabajando con .txt Files
# ========================

# Abrir y escribir en un archivo de texto (crea o sobrescribe si ya existe)
with open("example.txt", "w+") as txt_file:
    # Escribir contenido en el archivo
    txt_file.write("Hola, este es un archivo de texto.\n")
    txt_file.write("Python es genial para manejar archivos.\n")

# Leer el contenido del archivo de texto
with open("example.txt", "r") as txt_file:
    print("Contenido completo del archivo:")
    print(txt_file.read())

# Agregar más contenido al archivo de texto existente
with open("example.txt", "a") as txt_file:
    txt_file.write("Esta es una nueva línea añadida al archivo.\n")

# Leer línea por línea
with open("example.txt", "r") as txt_file:
    print("Leyendo línea por línea:")
    for line in txt_file:
        print(line.strip())  # strip() elimina espacios o saltos de línea extra

# ========================
# Trabajando con .json Files
# ========================

# Crear un diccionario de ejemplo
example_data = {
    "nombre": "Juan",
    "edad": 30,
    "lenguajes": ["Python", "JavaScript", "C++"],
    "es_desarrollador": True
}

# Guardar el diccionario en un archivo JSON
with open("example.json", "w") as json_file:
    json.dump(example_data, json_file, indent=4)
    print("Datos guardados en example.json")

# Leer el contenido del archivo JSON
with open("example.json", "r") as json_file:
    data = json.load(json_file)
    print("Datos cargados del archivo JSON:")
    print(data)

# ========================
# Trabajando con .csv Files
# ========================

# Crear un archivo CSV y escribir encabezados y datos
with open("example.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Escribir encabezados
    csv_writer.writerow(["Nombre", "Edad", "Lenguaje Principal"])
    # Escribir filas de datos
    csv_writer.writerow(["Ana", 25, "Python"])
    csv_writer.writerow(["Carlos", 28, "JavaScript"])
    csv_writer.writerow(["Maria", 32, "C++"])
    print("Datos escritos en example.csv")

# Leer el contenido del archivo CSV
with open("example.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    print("Contenido del archivo CSV:")
    for row in csv_reader:
        print(row)

# ========================
# Limpieza opcional
# ========================

# Eliminar los archivos creados (descomentar si deseas limpiar los archivos después de ejecutarlo)
# os.remove("example.txt")
# os.remove("example.json")
# os.remove("example.csv")

print("\nEjecución completada.")
