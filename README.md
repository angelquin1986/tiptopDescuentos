# Tipti Descuentos

## Prueba Tecnica de descuentos
### Autor :Angel Quingaluisa

##Requerimientos
#### -Lenguage Python 3.8
 - django 3.0.7
 - djangorestframework
 - Pycharm Profesional 2019.2
 
 #### -Postgresql 11.8-1
 ### Descripción 
   - Motor de descuentos realizado en python aplicado tdd, code coverage :
   - Pasos para instalar codigo
        - Clonar el proyecto
        - Crear un entorno virtual
        - Ejecutar  pip install -r requirements.txt( si instalan en  windows validar el compilador C++ por libreria de postresql)
        
 ### Data Pre Cargada
   - Se adjunto en la raiz del proyectto el respaldo de la base de datos db.slq
   - En el caso de no restaurar se debe utilizar
        - Ejecutar manage.py makemigrations
        - Ejecutar manage.py migrate   
        - Los fixtures :
            - motor_descuento/fixtures/db.json(Data de todo el modelo de datos con exepcion de producto,stockItem y conf. descuento)
            - motor_descuento/fixtures/descuento.json(Data de el modelo de conf. descuentos).
        - Comands :
            - motor_descuento/management/commands/articulos.py
            - motor_descuento/management/commands/retailer_articulos.py
            - ejemplo: manage.py articulos / manage.py retailer_articulos     
 ### Configuración
   - En el archivo descuentos/settings.py modificar los datos de la configuracion de la base de datos (DATABASES)
 ### Modelo de datos
![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/modelo.png)
 ### Modelo de datos Descuentos
   - Se trabaja con un modelo simple donde por la configuración dinamica  que puede tener los descuentos se toma la decision de tener parametrizado varios de los campos en formato Json
        
| Columna  | Tipo Data  |  Descripción |
|---|---|---|
| descuento_id  | integer  |  pk  |
|  json_data | Json   | datos de conf de los descuentos por articulo  |
| monto_maximo  |  Double |  monto maximo descuento |
| monto_actual  | Double  | monto artual descuento  |
| fecha_inicio  | date  | Fecha inicio del descuento mandatorio  |
| fecha_fin  | date  | Fecha fin del descuento mandatorio |
| hora_inicio  | time  | Hora inicio del descuento  |
| hora_fin  | time  |  Hora fin de descuento |
 ### COLUMNA JSON CONF
 
|key|tipo|Descripción
|---|---|---|
|product_id|integer|Código del producto, nulo si se requiere descuento por otros parámetros
|retailer_id|[]|Lista de tiendas donde aplica la promoción
|category_id|[]|Lista de categorias donde aplica la promoción
|sub_category_id|[]|Lista de sub categorias donde aplica la promoción
|client_id|integer|Código del cliente al que se le aplica la promoción
|monto_maximo_orden|double|Monto máximo a aplicar descuento , - si es indefinido
|es_cliente_prime|Boolean|Válida si se aplica a un cliente Prime
|brand_id|integer|Marca del producto al que se le aplica el descuento
|contador_descuentos|integer|Número de veces que  puede ocupar el descuento  si es -1 es indefinido(por cliente)
|forma_pago|1(efectivo) 2(Visa) 3(Mastercard)|Dependiendo si la forma de pago es efectivo o tarjeta
|codigo_aplicacion|String|Solo y solo tiene el codigo de verificacion 



 ### Test
   - Los test  del motor estan en el path motor_descuento/test/test_descuento.py
   - Para poder realizar los test se utiliza los fixtures :
        - motor_descuento/fixtures/db.json(Data de todo el modelo de datos con exepcion de producto,stockItem y conf. descuento)
        - motor_descuento/fixtures/descuento.json(Data de el modelo de conf. descuentos).
   - Para cargar la data de  articulos y stock item se utiliza  los metodos.
        - motor_descuento/test/util_test/product
        - motor_descuento/test/util_test/stok_items.
        - Nota: Estos metodos  y los fixtures se ejecutan en test_descuento  metodo setUp antes de ejecutar los test
        - Para validar code coverage utilizar Run with coverage de la herramienta Pycharm
        

        
        
1.-instalar requirements.txt
2.- postgres version 11.8
3.-python manage.py makemigrations
4.-python manage.py migrate
5.-manage.py dumpdata motor_descuento --exclude motor_descuento.Product --exclude motor_descuento.StockItem --indent 2  > db.json
6.-
