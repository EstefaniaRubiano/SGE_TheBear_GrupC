document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('productosForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtenir valors del formulari
        const nombre = document.getElementById('nombre').value.trim();
        const precio = parseInt(document.getElementById('precio').value);
        const cantidad = parseInt(document.getElementById('cantidad').value);
        const stock = parseInt(document.getElementById('stock').value);

         try {
            const url = `http://localhost:8000/productos/post?nombre=${encodeURIComponent(nombre)}&precio=${encodeURIComponent(precio)}&cantidad=${encodeURIComponent(cantidad)}&stock=${encodeURIComponent(stock)}`;
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
                showMessage('Producto creado correctamente!', 'success');
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