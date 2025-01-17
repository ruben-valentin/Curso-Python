# Manejo de Archivos en Python - Código Comentado 📁

## 1. Importación de Módulos Necesarios

```python
# Importamos los módulos necesarios para trabajar con diferentes tipos de archivos
import xml        # Para trabajar con archivos XML
import csv        # Para trabajar con archivos CSV
import json       # Para trabajar con archivos JSON
import os         # Para operaciones del sistema de archivos
```

## 2. Manejo de Archivos de Texto (.txt)

```python
# Abrimos/creamos un archivo de texto en modo escritura y lectura (w+)
txt_file = open("Intermediate/my_file.txt", "w+")

# Escribimos varias líneas de texto en el archivo
txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

# Leemos los primeros 10 caracteres del archivo
print(txt_file.read(10))

# Leemos una línea del archivo
print(txt_file.readline())

# Leemos otra línea del archivo
print(txt_file.readline())

# Iteramos sobre todas las líneas restantes del archivo
for line in txt_file.readlines():
    print(line)

# Añadimos una nueva línea al archivo
txt_file.write("\nAunque también me gusta Kotlin")

# Leemos una línea más
print(txt_file.readline())

# Cerramos el archivo
txt_file.close()

# Abrimos el archivo en modo append (añadir) usando 'with' (manejo seguro)
with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")  # Añadimos otra línea

# Línea comentada para eliminar el archivo
# os.remove("Intermediate/my_file.txt")
```

## 3. Manejo de Archivos JSON (.json)

```python
# Abrimos/creamos un archivo JSON en modo escritura y lectura
json_file = open("Intermediate/my_file.json", "w+")

# Creamos un diccionario con datos para guardar en JSON
json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"
}

# Escribimos el diccionario en el archivo JSON con formato indentado
json.dump(json_test, json_file, indent=2)

# Cerramos el archivo JSON
json_file.close()

# Abrimos el archivo JSON para lectura usando 'with'
with open("Intermediate/my_file.json") as my_other_file:
    # Imprimimos cada línea del archivo
    for line in my_other_file.readlines():
        print(line)

# Cargamos el contenido del archivo JSON en un diccionario
json_dict = json.load(open("Intermediate/my_file.json"))

# Imprimimos el diccionario completo
print(json_dict)

# Imprimimos el tipo de datos del diccionario
print(type(json_dict))

# Imprimimos solo el valor de la clave "name"
print(json_dict["name"])
```

## 4. Manejo de Archivos CSV (.csv)

```python
# Abrimos/creamos un archivo CSV en modo escritura y lectura
csv_file = open("Intermediate/my_file.csv", "w+")

# Creamos un objeto escritor CSV
csv_writer = csv.writer(csv_file)

# Escribimos la primera fila (encabezados)
csv_writer.writerow(["name", "surname", "age", "language", "website"])

# Escribimos una fila de datos
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])

# Escribimos otra fila de datos
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

# Cerramos el archivo CSV
csv_file.close()

# Abrimos el archivo CSV para lectura usando 'with'
with open("Intermediate/my_file.csv") as my_other_file:
    # Imprimimos cada línea del archivo
    for line in my_other_file.readlines():
        print(line)
```

## 5. Comentarios Adicionales

```python
# Para trabajar con archivos Excel (.xlsx)
# import xlrd # Requiere instalación del módulo

# Para trabajar con archivos XML
# Se pueden implementar funciones específicas para XML
```

## Notas Importantes 📝

1. **Modos de Apertura**:
   - `"w+"`: Escritura y lectura (crea nuevo archivo)
   - `"a"`: Append (añadir al final)
   - `"r"`: Solo lectura

2. **Manejo de Archivos**:
   - Siempre es recomendable usar `with` para garantizar que el archivo se cierre
   - Es importante cerrar los archivos cuando se abren con `open()`

3. **Tipos de Datos**:
   - CSV: Para datos tabulares simples
   - JSON: Para datos estructurados
   - TXT: Para texto plano
   - XML: Para datos estructurados más complejos

4. **Buenas Prácticas**:
   - Manejar excepciones al trabajar con archivos
   - Verificar la existencia de archivos antes de operarlos
   - Usar rutas relativas o absolutas según el caso

Este código muestra las operaciones básicas con diferentes tipos de archivos en Python, incluyendo lectura, escritura y manipulación de datos. 🚀