// URL del endpoint de la API
const API_URL = "http://localhost:8000/users/productos/";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const productos = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(productos); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los productos:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayUsers(productos) {
    const tableBody = document.querySelector("#productosTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    productos.forEach(producto => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const idCell = document.createElement("td");
        idCell.textContent = producto.producto.id;
        row.appendChild(idCell);

        const nombreCell = document.createElement("td");
        nombreCell.textContent = producto.producto.nombre;
        row.appendChild(nombreCell);

        const precioCell = document.createElement("td");
        precioCell.textContent = producto.producto.precio;
        row.appendChild(precioCell);

        const cantidadCell = document.createElement("td");
        cantidadCell.textContent = producto.producto.cantidad;
        row.appendChild(cantidadCell);

        const stockCell = document.createElement("td");
        stockCell.textContent = producto.producto.stock;
        row.appendChild(stockCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);