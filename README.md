# Taller práctico: análisis de datos con Pandas

Programa de consola que lee datos de ventas y clientes, los limpia, los une y los analiza. Se ejecuta desde un menú en la terminal, y cada opción corresponde a un módulo que vas a completar paso a paso.

Recuerda consultar la guía adjunta en PDF donde se te dará el paso a paso del trabajo.

## Requisitos

- Python 3.10 o superior
- Git (para clonar el repositorio)
- Conocimientos básicos de variables, listas y funciones

## Cómo empezar

1. Clona el repositorio y entra a la carpeta del proyecto:

   ```
   git clone <URL-DEL-REPOSITORIO>
   cd <NOMBRE-DE-LA-CARPETA>
   ```

2. Crea y activa un ambiente virtual. Las instrucciones completas, para Windows y Mac/Linux, están en `LEEME_ambiente.txt`.

3. Instala las librerías:

   ```
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```
   python main.py
   ```

Ejecuta siempre los comandos desde la carpeta del proyecto. Los módulos buscan los archivos a partir de su ubicación.

## Estructura del proyecto

```
├── main.py            Menú principal. No lo modifiques.
├── carga.py           Lee los CSV. Ya está completo.
├── limpieza.py        Limpia clientes y ventas. TODO 1 a 5.
├── merge.py           Valida y une las tablas. TODO 6 y 7.
├── analisis.py        Responde las preguntas de negocio. TODO 8 a 12.
├── graficos.py        Dibuja dos gráficos sencillos. TODO 13 y 14.
├── exploracion.py     Ejemplos de indexación, .loc, .iloc y concat. Se ejecuta por separado.
├── requirements.txt   Versiones de las librerías.
├── LEEME_ambiente.txt Pasos para crear el ambiente virtual.
└── Data/
    ├── raw/           Datos originales (cliente.csv, ventas.csv). No los modifiques.
    └── processed/     Resultados que genera el programa.
```

## Menú

| Opción | Qué hace |
|---|---|
| 1 | Carga los archivos CSV |
| 2 | Limpia los datos |
| 3 | Valida y une las tablas con merge |
| 4 | Muestra el análisis y las respuestas del desafío |
| 5 | Dibuja los gráficos de introducción |
| 6 | Sale del programa |

Las opciones se usan en orden: primero cargar (1), luego limpiar (2), después unir (3) y finalmente analizar (4) o graficar (5).

## Cómo completar el taller

1. Abre el archivo indicado en cada TODO. Cada función tiene un docstring con pistas.
2. Completa el TODO y ejecuta `python main.py` para probar la opción correspondiente.
3. Usa `exploracion.py` para practicar indexación, `.loc`, `.iloc` y `concat()` antes de aplicarlos en tu código.

El programa permite cargar, limpiar y unir los datos, y luego ejecutar el análisis y generar los gráficos desde el menú.

## Entregables

Consulta el documento del taller (`guia_Taller_Pandas.pdf`) para ver el detalle de cada entregable y la rúbrica. En resumen:

- Entregable 0: pantallazo del ambiente virtual activo y de la instalación.
- Entregable 1: pantallazos de `.shape`, `.info()` y `.describe()`, y salida de `exploracion.py`.
- Entregable 2: limpieza, con pantallazos antes y después y explicación.
- Entregable 3: validación, merge y análisis, con pantallazos de las opciones 3 y 4.
- Entregable 4: los dos gráficos (`.png`) y el código de `graficos.py`.
- Desafío final: respuestas a las cinco preguntas, con el criterio usado en cada una.

Para entregar, agrega al final de este `README.md` una sección con tu nombre y tus respuestas a las preguntas del desafío. Sube tus cambios al repositorio y envía el enlace por el formulario de entrega. La entrega es individual.

## Preguntas de negocio
Nombre: Jacobo Piedrahita

1. ¿Qué categoría genera más ingresos?

Tecnología, con ingresos de $14.290.000. Criterio: sumé la columna total agrupando las ventas por categoria y ordené los resultados de mayor a menor.

2. ¿Qué canal vende más?
Online, con 35 ventas, frente a 33 de Tienda. Criterio: comparé la cantidad de ventas por canal, contando los registros; también se calcularon los ingresos por canal.

3. ¿Los clientes VIP compran más que los Regulares?
Sí. Los clientes VIP tienen un promedio de 1,21 compras por cliente, frente a 1,08 de los Regulares. Criterio: comparé el promedio de compras por cliente de cada segmento, no los totales.

4. ¿Qué método de pago es el más usado?
Efectivo, con 30 compras. Tarjeta tuvo 25 y Transferencia 13. Criterio: conté las ventas de cada método de pago.

5. ¿Cuáles son los cinco clientes con más compras?
Nicolás Cardona, Matías Rodríguez, Mía Quintero, Luna Montoya y Luis Pérez, con 2 compras cada uno. Criterio: ordené los clientes por cantidad de compras y usé el gasto total como desempate.
## Explicaciones del taller

### Limpieza de datos
En las ventas encontré un producto vacío y lo reemplacé por `Sin especificar` para conservar la venta y su total. No eliminé la fila porque los demás datos de la transacción siguen siendo útiles. También quité espacios sobrantes, normalicé el formato de las ciudades, convertí `fecha_venta` a fecha y eliminé filas duplicadas. No había filas duplicadas y se conservaron las 60 filas de clientes y las 68 ventas.

### Resultado del merge
El merge tiene 14 columnas porque ventas aporta 10 columnas y clientes 5; `id_cliente` está en ambas tablas y queda una sola vez: 10 + 5 - 1 = 14. Se conservaron las 68 ventas mediante un merge left. La validación encontró identificadores de cliente únicos, tipos compatibles y ninguna venta sin cliente asociado.

### ¿Por qué `.iloc[2, 6]` devuelve el total de V003?
Después de usar `set_index("id_venta")`, V001 queda en la posición 0, V002 en la 1 y V003 en la 2. Las posiciones de columna empiezan en 0: la columna `total` está en la posición 6. Por eso `.iloc[2, 6]` devuelve el total de V003, que es 520000.
