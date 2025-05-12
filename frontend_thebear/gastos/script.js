// URL del endpoint de la API
const API_URL = "http://localhost:8000/gastos/";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const gastos = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(gastos); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los gastos:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayUsers(gastos) {
    const tableBody = document.querySelector("#gastosTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    gastos.forEach(gasto => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del gasto
        const idCell = document.createElement("td");
        idCell.textContent = gasto.gasto.id;
        row.appendChild(idCell);

        const descripcionCell = document.createElement("td");
        descripcionCell.textContent = gasto.gasto.descripcion;
        row.appendChild(descripcionCell);

        const categoriaCell = document.createElement("td");
        categoriaCell.textContent = gasto.gasto.categoria;
        row.appendChild(categoriaCell);

        const importeCell = document.createElement("td");
        importeCell.textContent = gasto.gasto.importe;
        row.appendChild(importeCell);

        const fechaCell = document.createElement("td");
        fechaCell.textContent = gasto.gasto.fecha;
        row.appendChild(fechaCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);