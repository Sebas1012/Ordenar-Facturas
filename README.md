# Script para Ordenar Facturas

Script en python que permite ordenar facturas por carpetas en base a un archivo excel que contiene el codigo de la factura y tipo de factura.

## Detalles:

- El archivo excel debe contar con la siguiente estructura:

| numero_factura | tipo_factura |
| --- | --- |

- El archivo JSON de configuracion debe contar con la siguiente estructura:

```JSON
  {
    "tipo_factura": "Ruta donde se movera la factura"
  }
```

- Como recomendacion y para llevar un orden, se pueden usar 2 carpetas para ubicar los archivos dentro de la raiz de este codigo, la carpeta llamada book para ubicar el excel y la carpeta llamada invoices para ubicar las facturas sin ordenar. **OJO** *no es necesario que sea asi, los archivos pueden estar en cualquier ruta.*



## Uso:

- Primero se deben instalar las dependencias usando el comando:

```
pip install -r requirements.txt
```
- El script cuenta con una unica funcion llamada **move_invoices()** la cual recibe 4 parametros obligatorios para su funcionamiento, dichos parametros son:

| Parametro | Definición |
| --- | --- |
| book_path | Recibe un string con la ruta en donde se encuentra el archivo de excel. |
| sheet_name | Recibe el nombre de la hoja donde se encuentra la informacion necesaria para ordenar, en caso de que no se necesite elejir una hoja especifica pasarle **None** como parametro. |
| json_path | Recibe un string con la ruta del archivo JSON que contiene las rutas de las carpetas a donde iran las facturas. |
| invoices_path | Recibe un string con la ruta donde se encuentran las facturas sin ordenar. |


<p align="center">
  <b>Hecho con ❤️ por: Sebastián. </b>
</p>
