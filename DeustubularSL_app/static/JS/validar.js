function validarFormulario() {
    var correoInput = document.getElementById('correo').value;
    var dniInput = document.getElementById('DNI').value;
    var dominios_validos = ["@deustubular.es", "@deusto.es"];

    // Realizar validaciones
    var correoValido = false;
    for (var i = 0; i < dominios_validos.length; i++) {
        var dominio = dominios_validos[i];
        if (correoInput.endsWith(dominio)) {
          
          correoValido = true;
          // Impedir el envío del formulario
        }
      }
      if (!correoInput.endsWith(dominio)) {
        window.location.href = 'http://127.0.0.1:8000/errorEmail/';
        return false;
      }

    if (!/\d{8}[a-zA-Z]$/.test(dniInput)) {
        window.location.href = 'http://127.0.0.1:8000/errorDni/';

        return false; // Impedir el envío del formulario
      }
  
    // Validación exitosa, se puede enviar el formulario
    return true;
  }
