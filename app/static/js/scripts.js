// app/static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Cuando el documento esté cargado, mostrar un mensaje en la consola
    console.log('La página se ha cargado correctamente!');
    
    // Ejemplo: cambiar el color del encabezado al hacer clic en él
    const header = document.querySelector('header');
    header.addEventListener('click', function() {
        header.style.backgroundColor = '#444';
    });
});
