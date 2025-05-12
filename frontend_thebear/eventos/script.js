// URL del endpoint de la API
const API_URL = "http://localhost:8000/eventos/";

// Función para obtener los datos de los eventos
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const eventos = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(eventos); // Mostramos los datos en la tabla
        //console.log(users)
    } catch (error) {
        console.error("Error al obtener los eventos:", error);
    }
}

// Función para mostrar los empleados en la tabla
function displayUsers(eventos) {
    const tableBody = document.querySelector("#eventosTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de eventos y creamos las filas de la tabla
    eventos.forEach(evento => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del evento
        const idCell = document.createElement("td");
        idCell.textContent = evento.evento.id;
        row.appendChild(idCell);

        const nombreCell = document.createElement("td");
        nombreCell.textContent = evento.evento.nombre;
        row.appendChild(nombreCell);

        const fechaCell = document.createElement("td");
        fechaCell.textContent = evento.evento.fecha;
        row.appendChild(fechaCell);

        const lugarCell = document.createElement("td");
        lugarCell.textContent = evento.evento.lugar;
        row.appendChild(lugarCell);

        const descripcionCell = document.createElement("td");
        descripcionCell.textContent = evento.evento.descripcion;
        row.appendChild(descripcionCell);

        const responsableidCell = document.createElement("td");
        responsableidCell.textContent = evento.evento.responsable_id;
        row.appendChild(responsableidCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);