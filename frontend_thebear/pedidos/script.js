// URL del endpoint de la API
const API_URL = "http://localhost:8000/users/pedidos/";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const pedidos = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(pedidos); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los pedidos:", error);
    }
}

// Función para mostrar los pedidos en la tabla
function displayUsers(pedidos) {
    const tableBody = document.querySelector("#pedidosTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    pedidos.forEach(pedido => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const idCell = document.createElement("td");
        idCell.textContent = pedido.pedido.id;
        row.appendChild(idCell);

        const fechaCell = document.createElement("td");
        fechaCell.textContent = pedido.pedido.fecha;
        row.appendChild(fechaCell);

        const precioTotalCell = document.createElement("td");
        precioTotalCell.textContent = pedido.pedido.precio_total;
        row.appendChild(precioTotalCell);

        const idEmpleadoCell = document.createElement("td");
        idEmpleadoCell.textContent = pedido.pedido.id_empleado;
        row.appendChild(idEmpleadoCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);