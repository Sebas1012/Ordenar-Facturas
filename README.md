# Script para Ordenar Facturas

Script en python que permite ordenar facturas por carpetas en base a un archivo excel que contiene el codigo de la factura y tipo de factura..

## Uso:

El script cuenta con una unica funcion llamada **move_invoices()** la cual recibe 4 parametros obligatorios para su funcionamiento, dichos parametros son:

| Parametro | Definición |
| --- | --- |
| book_path | Recibe un string con la ruta en donde se encuentra el archivo de excel. |
| sheet_name | Recibe el nombre de la hoja donde se encuentra la informacion necesaria para ordenar, en caso de que no se necesite elejir una hoja especifica pasarle **None** como parametro. |
| json_path | Recibe un string con la ruta del archivo JSON que contiene las rutas de las carpetas a donde iran las facturas. |
| invoices_path | Recibe un string con la ruta donde se encuentran las facturas sin ordenar. |
