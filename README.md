# SGE_TheBear_GrupC

# ACTIVIDAD ERP+FASTAPI - The Bear

---

## Autoras del proyecto

- **Estefanía Rubiano**  
  Responsable de los módulos de **Empleados** y **Eventos**

- **Alba Melendres**  
  Responsable de los módulos de **Compras** y **Gastos**

---
## Introducción
Este proyecto es una API REST desarrollada con FastAPI y PostgreSQL, pensada como un sistema ERP básico para la gestión de un restaurante (The Bear). La aplicación permite administrar de forma sencilla los módulos: Empleados, Eventos, Gastos y Compras. Cada módulo dispone de operaciones CRUD completas, documentadas y probadas mediante SwaggerUI.

## Diseño Bases de Datos
<img src="DIAGRAMA_NEW.drawio (2).png" width="800">

---
## Demostración en SwaggerUI

**Módulo: Empleados**

GET /empleados
<img src="img_swagger/EMPLEADOS/get.png" width="800">
Captura del endpoint que devuelve un listado completo de todos los empleados almacenados en la base de datos.

GET /empleados/{id}
<img src="img_swagger/EMPLEADOS/get_id.png" width="800">
Captura del endpoint que permite buscar y visualizar la información de un empleado específico a partir de su ID.

POST /empleados
<img src="img_swagger/EMPLEADOS/post_01.png" width="800">
<img src="img_swagger/EMPLEADOS/post_02.png" width="800">
Captura del formulario SwaggerUI para crear un nuevo empleado introduciendo su nombre, puesto, email y teléfono.

PUT /empleados/{id}
<img src="img_swagger/EMPLEADOS/put.png" width="800">
Captura del endpoint que permite modificar el nombre de un empleado existente, proporcionando su ID.

DELETE /empleados/{id}
<img src="img_swagger/EMPLEADOS/delete.png" width="800">
Captura del endpoint utilizado para eliminar a un empleado del sistema mediante su identificador.

**Módulo: Eventos**

GET /eventos
<img src="img_swagger/EVENTOS/get_all.png" width="800">
Captura del endpoint que muestra una lista completa de los eventos registrados en el sistema.

GET /eventos/{id}
<img src="img_swagger/EVENTOS/get_id.png" width="800">
Captura del endpoint que permite consultar los detalles de un evento específico según su ID.

POST /eventos
<img src="img_swagger/EVENTOS/post_01.png" width="800">
<img src="img_swagger/EVENTOS/post_02.png" width="800">
Captura del formulario para registrar un nuevo evento indicando su nombre, fecha y descripción.

PUT /eventos/{id}
<img src="img_swagger/EVENTOS/put.png" width="800">
Captura del endpoint que permite actualizar el nombre de un evento determinado.

DELETE /eventos/{id}
<img src="img_swagger/EVENTOS/delete.png" width="800">
Captura del endpoint usado para eliminar un evento del sistema según su ID.

**Módulo: Gastos**

GET /gastos
<img src="img_swagger/GASTOS/get_all_01.png" width="800">
<img src="img_swagger/GASTOS/get_all_02.png" width="800">
Captura del endpoint que devuelve una lista de todos los gastos registrados en la aplicación.

GET /gastos/{id}
<img src="img_swagger/GASTOS/get_id_01.png" width="800">
<img src="img_swagger/GASTOS/get_id_02.png" width="800">
Captura del endpoint que permite obtener los datos detallados de un gasto individual mediante su ID.

POST /gastos
<img src="img_swagger/GASTOS/post_01.png" width="800">
<img src="img_swagger/GASTOS/post_02.png" width="800">
Captura del formulario para añadir un nuevo gasto, incluyendo su concepto, importe y fecha.

PUT /gastos/{id}
<img src="img_swagger/GASTOS/put.png" width="800">
Captura del endpoint que permite actualizar la descripción de un gasto concreto.

DELETE /gastos/{id}
<img src="img_swagger/GASTOS/delete.png" width="800">
Captura del endpoint que elimina un gasto específico del sistema utilizando su identificador.

**Módulo: Compras**

GET /productos/
<img src="img_swagger/PRODUCTOS/get_all.png" width="800">
Captura del endpoint que muestra todos los productos disponibles en el sistema.
Devuelve una lista con información como nombre, precio, cantidad y stock de cada producto.

GET /productos/{id}
<img src="img_swagger/PRODUCTOS/get_id.png" width="800">
Captura del endpoint que devuelve los detalles de un producto específico mediante su ID.

POST /productos/post
<img src="img_swagger/PRODUCTOS/post_01.png" width="800">
<img src="img_swagger/PRODUCTOS/post_02.png" width="800">
Captura del formulario para crear un nuevo producto introduciendo su nombre, precio, cantidad y stock.

PUT /productos/put
<img src="img_swagger/PRODUCTOS/put.png" width="800">
Captura del formulario para actualizar el nombre de un producto existente mediante su ID.

DELETE /productos/delete
<img src="img_swagger/PRODUCTOS/delete.png" width="800">
Captura del endpoint que permite eliminar un producto específico del catálogo mediante su ID.

GET /pedidos/
<img src="img_swagger/PEDIDOS/get.png" width="800">
Captura del endpoint que devuelve una lista de todos los pedidos registrados, con información como fecha, precio total, producto y empleado asociado.

GET /pedidos/{id}
<img src="img_swagger/PEDIDOS/get_id.png" width="800">
Captura del endpoint que muestra los detalles de un pedido específico a través de su ID.

POST /pedidos/post
<img src="img_swagger/PEDIDOS/post_01.png" width="800">
<img src="img_swagger/PEDIDOS/post_02.png" width="800">
Captura del formulario para registrar un nuevo pedido, seleccionando el producto, el empleado, la fecha y especificando el precio total.

PUT /pedidos/put
<img src="img_swagger/PEDIDOS/put.png" width="800">
Captura del formulario para actualizar el precio total de un pedido existente.

DELETE /pedidos/delete
<img src="img_swagger/PEDIDOS/delete.png" width="800">
Captura del endpoint que permite eliminar un pedido específico del sistema mediante su ID.

