document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('gastosForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const descripcion = document.getElementById('descripcion').value.trim();
        const categoria = document.getElementById('categoria').value.trim();
        const importe = parseInt(document.getElementById('importe').value);
        const fecha = document.getElementById('fecha').value.trim();

         try {
            const url = `http://localhost:8000/gastos/post?descripcion=${encodeURIComponent(descripcion)}&categoria=${encodeURIComponent(categoria)}&importe=${encodeURIComponent(importe)}&fecha=${encodeURIComponent(fecha)}`;
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