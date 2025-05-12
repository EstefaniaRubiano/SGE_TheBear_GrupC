document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('eventoForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const nombre = document.getElementById('nombre').value.trim();
        const fecha = document.getElementById('fecha').value.trim();
        const lugar = document.getElementById('lugar').value.trim();
        const descripcion = document.getElementById('descripcion').value.trim();
        const responsable_id = parseInt(document.getElementById('responsable_id').value);

         try {
            // Enviar datos al servidor
            //TODO: CAMBIAR URL
            const url = `http://localhost:8000/clients/post?nombre=${encodeURIComponent(nombre)}&fecha=${encodeURIComponent(fecha)}&lugar=${encodeURIComponent(lugar)}&descripcion=${encodeURIComponent(descripcion)}&responsable_id=${encodeURIComponent(responsable_id)}`;
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                //body: JSON.stringify({
                //    nombre,
                //    puesto,
                //    email,
                //    telefono
                //})
            });

            if (response.ok) {
                showMessage('Evento creado correctamente!', 'success');
                form.reset(); // Netejar el formulari
            } else {
                showMessage(`Error: ${data.detail || 'Error desconocido'}`, 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});