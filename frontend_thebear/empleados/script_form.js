document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('empleadoForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const nombre = document.getElementById('nombre').value.trim();
        const puesto = document.getElementById('puesto').value.trim();
        const email = document.getElementById('email').value.trim();
        const telefono = parseInt(document.getElementById('telefono').value);

         try {
            // Enviar datos al servidor
            //TODO: CAMBIAR URL
            const url = `http://localhost:8000/empleados/post?nombre=${encodeURIComponent(nombre)}&puesto=${encodeURIComponent(puesto)}&email=${encodeURIComponent(email)}&telefono=${encodeURIComponent(telefono)}`;
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
                showMessage('Empleado creado correctamente!', 'success');
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