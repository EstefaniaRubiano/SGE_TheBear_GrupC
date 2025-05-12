// URL del endpoint de la API
const API_URL = "http://localhost:8000/empleados/";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const empleados = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(empleados); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los empleados:", error);
    }
}

// Función para mostrar los empleados en la tabla
function displayUsers(empleados) {
    const tableBody = document.querySelector("#empleadosTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de empleados y creamos las filas de la tabla
    empleados.forEach(empleado => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del gasto
        const idCell = document.createElement("td");
        idCell.textContent = empleado.empleado.id;
        row.appendChild(idCell);

        const nombreCell = document.createElement("td");
        nombreCell.textContent = empleado.empleado.nombre;
        row.appendChild(nombreCell);

        const puestoCell = document.createElement("td");
        puestoCell.textContent = empleado.empleado.puesto;
        row.appendChild(puestoCell);

        const emailCell = document.createElement("td");
        emailCell.textContent = empleado.empleado.email;
        row.appendChild(emailCell);

        const telefonoCell = document.createElement("td");
        telefonoCell.textContent = empleado.empleado.telefono;
        row.appendChild(telefonoCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);