# Módulos en Python - Guía Detallada 📦

## ¿Qué es un Módulo?
Un módulo es como una biblioteca de código reutilizable. Imagina que estás escribiendo un libro (tu programa) y en lugar de escribir todo desde cero, puedes tomar capítulos ya escritos (módulos) y usarlos en tu libro.

## Tipos de Módulos (Con Ejemplos Detallados)

### 1. Módulos Integrados de Python
```python
# Importamos módulos útiles
import random
import datetime
import math

# Ejemplos de uso:
numero_aleatorio = random.randint(1, 100)  # Genera un número entre 1 y 100
fecha_actual = datetime.datetime.now()      # Obtiene la fecha y hora actual
raiz_cuadrada = math.sqrt(16)              # Calcula la raíz cuadrada de 16

print(f"Número aleatorio: {numero_aleatorio}")
print(f"Fecha actual: {fecha_actual}")
print(f"Raíz cuadrada de 16: {raiz_cuadrada}")
```
**Explicación Detallada:**
- `random`: Te permite generar números o selecciones aleatorias
- `datetime`: Para todo lo relacionado con fechas y tiempo
- `math`: Contiene funciones matemáticas avanzadas

### 2. Módulos de Terceros
```python
# Primero instalar:
# pip install requests
# pip install pandas

import requests
import pandas as pd

# Ejemplo de uso de requests:
response = requests.get('https://api.ejemplo.com/datos')
if response.status_code == 200:
    datos = response.json()

# Ejemplo de uso de pandas:
df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'María'],
    'Edad': [25, 30, 35]
})
print(df)
```
**Explicación Detallada:**
- `requests`: Para hacer peticiones HTTP a internet
- `pandas`: Para análisis y manipulación de datos
- Estos módulos necesitan ser instalados primero usando pip

### 3. Módulos Propios (Con Ejemplos Completos)

```python
# utils.py
def validar_email(email):
    """
    Valida si un email tiene formato correcto
    """
    return '@' in email and '.' in email

def formatear_nombre(nombre):
    """
    Capitaliza cada palabra en un nombre
    """
    return nombre.title()

# constantes.py
EDAD_MINIMA = 18
EDAD_MAXIMA = 65
DIAS_SEMANA = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

# main.py
from utils import validar_email, formatear_nombre
from constantes import EDAD_MINIMA, DIAS_SEMANA

# Uso de las funciones y constantes
email = "usuario@ejemplo.com"
nombre = "juan garcía"

if validar_email(email):
    print(f"Email válido: {email}")
    print(f"Nombre formateado: {formatear_nombre(nombre)}")
    print(f"Edad mínima requerida: {EDAD_MINIMA}")
    print(f"Días laborables: {DIAS_SEMANA}")
```

## Formas de Importar (Explicadas en Detalle)

### 1. Importación Completa
```python
import math

# Debemos usar el nombre del módulo como prefijo
resultado = math.sqrt(16)
seno = math.sin(math.pi/2)
```
**¿Cuándo usar?** Cuando necesitas varias funciones del módulo y quieres evitar conflictos de nombres.

### 2. Importación Específica
```python
from math import sqrt, pi, sin

# Podemos usar las funciones directamente
resultado = sqrt(16)
seno = sin(pi/2)
```
**¿Cuándo usar?** Cuando solo necesitas algunas funciones específicas y quieres un código más limpio.

### 3. Importación con Alias
```python
import pandas as pd
import numpy as np

# Uso con nombres más cortos
df = pd.DataFrame({'A': [1, 2, 3]})
array = np.array([1, 2, 3])
```
**¿Cuándo usar?** Para módulos con nombres largos o cuando hay convenciones establecidas.

## Estructura de Proyecto Completa
```
mi_proyecto/
    ├── main.py              # Archivo principal
    ├── config/
    │   ├── __init__.py
    │   └── settings.py      # Configuraciones
    ├── utils/
    │   ├── __init__.py
    │   ├── validators.py    # Funciones de validación
    │   └── helpers.py       # Funciones auxiliares
    └── models/
        ├── __init__.py
        └── user.py          # Clase Usuario
```

### Ejemplo de Contenido de los Archivos:
```python
# settings.py
DATABASE_URL = "postgresql://localhost:5432/db"
API_KEY = "your-api-key"

# validators.py
def validar_telefono(numero):
    return len(numero) == 9 and numero.isdigit()

# helpers.py
def formatear_fecha(fecha):
    return fecha.strftime("%d/%m/%Y")

# user.py
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
```

## Buenas Prácticas con Ejemplos 🎯

### 1. Documentación Clara
```python
# matematicas.py
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Lista de números
    
    Returns:
        float: Promedio calculado
    
    Ejemplo:
        >>> calcular_promedio([1, 2, 3])
        2.0
    """
    return sum(numeros) / len(numeros)
```

### 2. Manejo de Errores
```python
# utils.py
def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    except TypeError:
        print("Error: Tipos de datos incorrectos")
        return None
```

### 3. Constantes en Módulos Separados
```python
# constantes.py
LIMITE_INTENTOS = 3
TIMEOUT_SEGUNDOS = 30
ESTADOS_VALIDOS = ['activo', 'inactivo', 'pendiente']

# main.py
from constantes import LIMITE_INTENTOS, ESTADOS_VALIDOS

def procesar_usuario(estado):
    if estado in ESTADOS_VALIDOS:
        # Procesar...
        pass
```

¡Con estos ejemplos y explicaciones, ya puedes empezar a crear y usar módulos en Python de manera efectiva! 🚀