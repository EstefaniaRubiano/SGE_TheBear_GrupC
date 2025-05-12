document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('pedidosForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const fecha = document.getElementById('fecha').value.trim();
        const precio_total = parseInt(document.getElementById('precio_total').value);
        const id_empleado = parseInt(document.getElementById('id_empleado').value);

         try {
            const url = `http://localhost:8000/pedidos/post?fecha=${encodeURIComponent(fecha)}&precio_total=${encodeURIComponent(precio_total)}&id_empleado=${encodeURIComponent(id_empleado)}`;
            // Enviar dades al servidor amb body JSON
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                //body: JSON.stringify({
                //    name: name,
                //    email: email,
                //    age: age
                //})
            });

            if (response.ok) {
                showMessage('Gasto creado correctamente!', 'success');
                form.reset(); // Netejar el formulari
            } else {
                showMessage(`Error: ${data.detail || 'Error desconegut'}`, 'error');
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