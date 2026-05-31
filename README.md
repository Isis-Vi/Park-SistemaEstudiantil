# Sistema Inteligente de Parqueadero

## Descripción

Este proyecto consiste en un sistema básico de gestión de parqueadero desarrollado en Python.
El sistema fue diseñado como una simulación de un control de acceso vehicular para instituciones educativas, empresas u organizaciones que requieran llevar un registro de ingresos y salidas.

---

## Características

* Registro de entrada de vehículos.
* Registro de salida de vehículos.
* Almacenamiento permanente mediante SQLite.
* Registro automático de fecha y hora de ingreso.
* Consulta de vehículos actualmente presentes en el parqueadero.
* Conservación del historial de registros en la base de datos.
* Interfaz de consola sencilla e intuitiva.

---

## Tecnologías Utilizadas

* Python 3.x
* SQLite3
* Datetime

---

## Estructura de la Base de Datos

Tabla: `vehiculos`

| Campo        | Tipo     | Descripción                               |
| ------------ | -------- | ----------------------------------------- |
| id_registro  | INTEGER  | Identificador único autoincremental       |
| placa        | TEXT     | Placa del vehículo                        |
| hora_entrada | DATETIME | Fecha y hora de ingreso                   |
| estado       | TEXT     | Estado actual del vehículo (Dentro/Fuera) |

---

## Instalación

1. Descargar o clonar el proyecto.
2. Verificar que Python 3 esté instalado.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python main.py
```

o

```bash
py main.py
```

La base de datos `parking.db` se creará automáticamente durante la primera ejecución.

---

## Uso

Al iniciar el programa se mostrará el siguiente menú:

1. Registrar entrada
2. Registrar salida
3. Mostrar estado
4. Salir

### Registrar entrada

Permite ingresar la placa de un vehículo y registrar su ingreso al parqueadero junto con la fecha y hora actuales.

### Registrar salida

Actualiza el estado del vehículo a "Fuera" cuando abandona el parqueadero.

### Mostrar estado

Muestra los vehículos que actualmente se encuentran dentro del parqueadero.


## Autor

Proyecto desarrollado con fines académicos para demostrar conceptos de programación orientada a objetos, manejo de bases de datos SQLite y persistencia de información mediante Python.
