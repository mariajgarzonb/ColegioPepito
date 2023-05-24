// Obtener referencias a los elementos del DOM
const formularioAlumno = document.getElementById('formularioAlumno');
const txtNombre = document.getElementById('txtNombre');
const txtApellido = document.getElementById('txtApellido');
const fechaNacimiento = document.getElementById('fechaNacimiento');

// Validar el formulario al enviarlo
formularioAlumno.addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar que se envíe el formulario de forma predeterminada

    // Validar los campos del formulario
    if (validarCampos()) {
        // Enviar el formulario si los campos son válidos
        formularioAlumno.submit();
    }
});

// Función para validar los campos del formulario
function validarCampos() {
    let valid = true;

    // Validar el campo de nombre
    if (txtNombre.value.trim() === '') {
        mostrarError(txtNombre, 'El nombre es requerido');
        valid = false;
    } else {
        mostrarExito(txtNombre);
    }

    // Validar el campo de apellido
    if (txtApellido.value.trim() === '') {
        mostrarError(txtApellido, 'El apellido es requerido');
        valid = false;
    } else {
        mostrarExito(txtApellido);
    }

    // Validar el campo de fecha de nacimiento
    if (fechaNacimiento.value.trim() === '') {
        mostrarError(fechaNacimiento, 'La fecha de nacimiento es requerida');
        valid = false;
    } else {
        mostrarExito(fechaNacimiento);
    }

    return valid;
}

// Función para mostrar un mensaje de error en un campo
function mostrarError(campo, mensaje) {
    campo.classList.add('is-invalid');
    campo.classList.remove('is-valid');

    const mensajeError = campo.nextElementSibling;
    mensajeError.innerText = mensaje;
    mensajeError.classList.add('invalid-feedback');
    mensajeError.classList.remove('valid-feedback');
}

// Función para mostrar un mensaje de éxito en un campo
function mostrarExito(campo) {
    campo.classList.remove('is-invalid');
    campo.classList.add('is-valid');

    const mensajeError = campo.nextElementSibling;
    mensajeError.innerText = '';
    mensajeError.classList.remove('invalid-feedback');
    mensajeError.classList.add('valid-feedback');
}
