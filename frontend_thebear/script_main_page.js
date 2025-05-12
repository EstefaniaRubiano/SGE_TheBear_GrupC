document.addEventListener('DOMContentLoaded', () => {
    // Mòdul: Empleados
    const empleadosModule = document.getElementById('empleadosModule');

    empleadosModule.addEventListener('click', () => {
        window.location.href = 'empleados/index_form.html';
    });

    empleadosModule.addEventListener('mouseenter', () => {
        empleadosModule.style.borderColor = '#714B67';
    });

    empleadosModule.addEventListener('mouseleave', () => {
        empleadosModule.style.borderColor = '#e0e0e0';
    });

    // Mòdul: Eventos
    const eventosModule = document.getElementById('eventosModule');

    eventosModule.addEventListener('click', () => {
        window.location.href = 'eventos/index_form.html';
    });

    eventosModule.addEventListener('mouseenter', () => {
        eventosModule.style.borderColor = '#714B67';
    });

    eventosModule.addEventListener('mouseleave', () => {
        eventosModule.style.borderColor = '#e0e0e0';
    });

    // Mòdul: Gastos
    const gastosModule = document.getElementById('gastosModule');

    gastosModule.addEventListener('click', () => {
        window.location.href = 'gastos/index_form.html';
    });

    gastosModule.addEventListener('mouseenter', () => {
        gastosModule.style.borderColor = '#714B67';
    });

    gastosModule.addEventListener('mouseleave', () => {
        gastosModule.style.borderColor = '#e0e0e0';
    });

    // Mòdul: Pedidos
    const pedidosModule = document.getElementById('pedidosModule');

    pedidosModule.addEventListener('click', () => {
        window.location.href = 'pedidos/index_form.html';
    });

    pedidosModule.addEventListener('mouseenter', () => {
        pedidosModule.style.borderColor = '#714B67';
    });

    pedidosModule.addEventListener('mouseleave', () => {
        pedidosModule.style.borderColor = '#e0e0e0';
    });

    // Mòdul: Productos
    const productosModule = document.getElementById('productosModule');

    productosModule.addEventListener('click', () => {
        window.location.href = 'productos/index_form.html';
    });

    productosModule.addEventListener('mouseenter', () => {
        productosModule.style.borderColor = '#714B67';
    });

    productosModule.addEventListener('mouseleave', () => {
        productosModule.style.borderColor = '#e0e0e0';
    });
});