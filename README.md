# Tipti Descuentos

## Prueba Tecnica de descuentos
### Autor :Angel Quingaluisa

##Requerimientos
#### -Lenguage Python 3.7
 - django 3.0.7
 - djangorestframework
 - Pycharm Profesional 2019.2
 - drf-yasg (swagger)
 #### -Postgresql 11.8-1
 ### Descripción 
   - Motor de descuentos realizado en python aplicado tdd, code coverage :
   - Pasos para instalar codigo
        - Clonar el proyecto
        - Crear un entorno virtual
        - Ejecutar  pip install -r requirements.txt( si instalan en  windows validar el compilador C++ por libreria de postresql)
        - En caso de error actualizar pip(necesario 20.1.1<) con el comando : pip install --upgrade pip
        
 ### Data Pre Cargada
   - Se adjunto en la raiz del proyecto el respaldo de la base de datos bk.slq
   - En el caso de no restaurar se debe utilizar
        - Crear en postgres la bb con nombre tipti
        - Ejecutar manage.py makemigrations
        - Ejecutar manage.py migrate   
        - Los fixtures :
            - motor_descuento/fixtures/db.json(Data de todo el modelo de datos con exepcion de producto,stockItem y conf. descuento)
            - motor_descuento/fixtures/descuento.json(Data de el modelo de conf. descuentos).
            - comandos manage.py loaddata db/descuento
        - Comands :
            - motor_descuento/management/commands/articulos.py
            - motor_descuento/management/commands/retailer_articulos.py
            - ejemplo: manage.py articulos / manage.py retailer_articulos     
 ### Configuración
   - En el archivo descuentos/settings.py modificar los datos de la configuracion de la base de datos (DATABASES)
 ### Modelo de datos
![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/modelo.jpg)
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
 
|key|tipo|Descripción|
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

 ### PROCESOS DE DESCUENTO  REALIZADOS Y CON TEST
 |Item|Realizado|Notas|
|---|---|---|
|1. Descuentos que aplican a una o varias categorías de una tienda especifica o de todas|SI||
|2. Descuentos que aplican a una o varias subcategorías de una tienda especifica o de todas|SI||
|3. Descuentos que aplican únicamente a uno o varios productos de una tienda en específico o de todas|SI||
|4. Descuentos únicamente para clientes específicos|SI||
|5. Descontar un porcentaje x en tu carrito de compras hasta y monto. (descuento del 30% hasta que el valor descantado llegue a los $200)|NO||
|6. Descuento único para clientes prime - (prime es un modelo de suscripción exclusivo dentro del app)|SI||
|7. Descuentos en todos los productos de una marca específicas|SI||
|8. Descuentos de envíos gratis sin condiciones|NO|Nota :Es una configuracion difecten porque el motor esta hecho para descuentos sobre articulos|
|9. Descuento de envío gratis luego de comprar un monto mínimo de productos de una marca en específico.|NO|Nota :Es una configuracion difecten porque el motor esta hecho para descuentos sobre articulos|
|10. Descuentos de envíos gratis a partir de cierto monto en tu carrito de compras|NO|Nota :Es una configuracion difecten porque el motor esta hecho para descuentos sobre articulos|
|11. Descuentos con las configuraciones anteriores que aplican según el día de la semana en la que se creó la orden.|SI||
|12. Descuentos con las configuraciones anteriores que aplican según el día de la semana en se va a entregar la orden.|SI||
|13. Descuentos con las configuraciones anteriores que únicamente se aplican cuando la orden tenga fecha de entrega para el mismo día de la creación de la orden|SI|Nota: el motor de descuentos recibe una sola fecha para validar si existe conf. Descuentos   en la fecha ingresada y también validar por dias.Si necesita validar una fecha o varias fechas de ingreso o entrega debe  otro microservicio que decida qué fecha debe mandar al motor para que el lo resuelva.|  
 ### CONFIGURACIONES DE DESCUENTO  REALIZADOS Y CON TEST

 |Item|Realizado|Notas|
|---|---|---|
|1.-Todo descuento aplicara un porcentaje definido como descuento sobre cada producto de la orden no sobre el valor final de la misma.|SI||
|2. Los descuentos deben poderse configurar de tal forma que yo ingrese la prioridad de un descuento sobre otro y si un descuento se puede o no combinar con uno o más descuentos.|||
|3. Los descuentos pueden configurarse para que se apliquen a todo el país en todas sus tiendas o en tiendas seleccionadas.|||
|4. Los descuentos pueden configurarse para que se apliquen a toda una o varias ciudades para todas sus tiendas o en tiendas seleccionadas.|||
|5. Los descuentos pueden configurarse para que se apliquen a toda uno o varios sectores de una ciudad para todas sus tiendas o en tiendas seleccionadas.|||
|6. Que se pueda definir cuantas veces puede ocupar ese descuento un cliente |||
|7. Que se pueda configurar cualquiera de los tipos de descuento para que se aplique según la forma de pago o la marca de tarjeta de crédito con la que cancela un cliente su orden.|SI||
|8. Que la vigencia de un descuento se pueda definir desde una fecha hasta otra y que días de las semanas aplican durante esa vigencia,|SI||
| 9. Que el descuento pueda activarse por horas es decir desde el primero de mayo al 5 de mayo desde las 3 y 30 hasta las 18 horas aplica este descuento.|SI||
|10. Un descuento se puede marcar para que únicamente se active luego de agregar un código en la aplicación.|SI||
|11. Se debe registrar en cada order item que descuento se aplico|SI||
|12. Se debe registrar en cada orden el descuento que aplico |SI|Nota: el motor devuelve un dic con una estructura  que puede ser utlizada despues  para colocar en un order_item, order , etc|
|13. Un descuento debe tener la capacidad de configurar hasta que monto acumulado de descuentos aplica. Ejemplo (yo configuro un 30% de descuentos en toda una tienda y como este descuento me lo patrocina cierta empresa externa me indica que el descuento debe estar activo hasta que la suma de todos los montos descontados en cada orden me llegue a un total de 5 mil dólares)|||  


 ### Test
 ![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/test.png)
   - Los test  del motor estan en el path motor_descuento/test/test_descuento.py
   - Para poder realizar los test se utiliza los fixtures :
        - motor_descuento/fixtures/db.json(Data de todo el modelo de datos con exepcion de producto,stockItem y conf. descuento)
        - motor_descuento/fixtures/descuento.json(Data de el modelo de conf. descuentos).
   - Para cargar la data de  articulos y stock item se utiliza  los metodos.
        - motor_descuento/test/util_test/product
        - motor_descuento/test/util_test/stok_items.
        - Nota: Estos metodos  y los fixtures se ejecutan en test_descuento  metodo setUp antes de ejecutar los test
        - Para validar code coverage utilizar Run with coverage de la herramienta Pycharm
        ![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/coverage.png)
        
### LOGICA DE NEGOCIO
   - La logica de negocio para el motor de descuento se encuentra en   motor_descuento/logica_negocio/ln_descuento.py
 ![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/ln.png)
 ### API REST
    Se entrega los siguientes rest
   - http://127.0.0.1:8000/calcular-descuento
        - Api encargado de calcular y retornar los  datos de descuento por stock item    dependiendo de la configuración
        - Tipo POST
        - Formato Entra
            - Ejemplo: { "fecha_actual":"2019-04-10", "stock_item":[ { "product_id":14, "retailer_id":1 }, { "product_id":32, "retailer_id":1 }, { "product_id":43, "retailer_id":1 } ], "cliente_id":1, "codigo_forma_pago":1, "codigo_aplicacion":null }
        - Formatos:  
            - fecha_actual : "YYYY-MM-DD" :
            - stock_item :  json que incluue product_id(id_producto) /retailer_id(id tienda)
            - cliente_id :  id del cliente 
            - codigo_forma_pago :forma de pago valores 1(efectivo) 2(Visa) 3(Mastercard)
            - codigo_aplicacion :si  aplica codigo descuento colocar el mismo (String) caso contrario null
        - Nota: para poder   utilizar los codigos de productos, retailer , cliente se debe validar en base de datos los registros creados en prueba, los mismo no sotro los mismo de  los test.
        - Adjunto sql para ver stock de productos por tienda
            - select p.id,p.name,r.id,r.name from stock_item s inner join product p on s.product_id =p.id inner join retailer r on r.id=s.retailer_id where s.retailer_id =1 ;
        - Salida 
            - Collecion de productos que aplica el descuento   
            - [ { "product_id": 14, "retailer_id": 1, "pvp": 8.53, "descuento": 2.4737, "descuento_porcentaje": 29, "tipo_descuento": "mar" }, { "product_id": 32, "retailer_id": 1, "pvp": 5.56, "descuento": 1.6124, "descuento_porcentaje": 29, "tipo_descuento": "mar" }, { "product_id": 43, "retailer_id": 1, "pvp": 7.38, "descuento": 2.1402, "descuento_porcentaje": 29, "tipo_descuento": "mar" } ]
    - ![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/calcularDescuento.png)
   -  http://127.0.0.1:8000/descuento-retailer
   -  Api encargado de calcular y retornar los  datos de descuento   por  tienda 
        - Tipo POST
        - Formato Entra
            - Ejemplo: { "fecha_actual":"2019-04-10", "retailer_id":1 }
        - Formatos:  
            - fecha_actual : "YYYY-MM-DD" :
            - retailer_id :  id de la tienda
        - Nota:  validar en base de datos los codigos de las tiendas en retailer
        - Salida 
            - Collecion de productos que aplica el descuento   
            - { "product_id": 101099, "retailer_id": 1, "pvp": 6.27, "descuento": 1.8183, "descuento_porcentaje": 29, "tipo_descuento": "mar" }, { "product_id": 101512, "retailer_id": 1, "pvp": 6.73, "descuento": 1.9517, "descuento_porcentaje": 29, "tipo_descuento": "mar" }]
        - ![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/descuentoxtienda.png)
 ### DOCUMENTACION API REST
   - La docuemntacion se puede ver mediante el api de swagger(http://127.0.0.1:8000/swagger/)
   - ![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/swagger.png)
 
### CONFIGURACION PRONT END
   - url  front end http://127.0.0.1:8000/descuentos
   - El front end se realizo con  :
        - vue.js
        - vietify framework
        - django templates
        - django api rest
   - El mismo muestra las configuraciones actuales de la base de datos.
   - ![alt text](https://raw.githubusercontent.com/angelquin1986/tiptopDescuentos/master/archivos/frontEnd.png)
### FALTANTES
   - Por motivo tiempo no se puedo terminar con el front en, el mismo que por el momento  solo muestra las configuraciones , pero  no persiste ni valida todos los casos para guardar las configuraciones.
   - En el caso de que se requiera  persistir una configuracion la forma mas facil el leer la documentacion de Columna Json Congf y poder crear un fixture siempre teniendo en cuenta las conbinaciones que debew tomar para una configuracion correcta de descuento.
   -  Un ejemplo ode fixtures para almacenar conf, descuento esta en  motor_descuento\fixtures\descuento.json
   - Para correr con fixture se debe ejecutar el comando    manage.py loaddata nombre_fixture.py
   - Conf descuento Faltantes.
       - Descuentos por  envio gratis (Este descuento se clasifica como tipo de descuento y debe ser parametrizado en la tabla como un tipo mas, por el momento solo articulos)
       - Descuentos  relacionados, por motivo tiempo no se desarrollo esta funcionalidad
       - Pruebas de estres con  concurrecia de usarios ( Por motivo tiempo falta de desarrollar.)    
### Algunos Comandos  
-   pip install -r requirements.txt instalar dependencias 
-   python manage.py makemigrations ( validar cambios en los modelos)
-   python manage.py migrate (migrar modelo a la base de datos)
-   manage.py dumpdata motor_descuento --exclude motor_descuento.Product --exclude motor_descuento.StockItem --indent 2  > db.json (copiar la data de la db en file json)
-   python manage.py createsuperuser admin/adminadmin (crear un super usuario en django admin)
-   manage.py loaddata descuento (cargar la data desde fictures a la base de datos)
-   manage.py runserver 8000 (ejecutar el proyecto)
