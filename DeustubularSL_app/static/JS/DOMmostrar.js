
axios.get('http://127.0.0.1:8000/api/empleados/')
  .then(response => {
    const empleados = response.data;
    const empleadosBody = document.getElementById('empleados-body');

    empleados.forEach(empleado => {
        console.log(empleado)
      const row = document.createElement('tr');

      const nombreCell = document.createElement('td');
      const nombreLink = document.createElement('a');
      nombreLink.href = '/empleados/detalle_empleado' + empleado.id + '/';
      nombreCell.textContent = empleado.nombre;
      row.appendChild(nombreCell);
      nombreCell.appendChild(nombreLink);

      const apellidosCell = document.createElement('td');
      apellidosCell.textContent = empleado.apellidos;
      row.appendChild(apellidosCell);

      const dniCell = document.createElement('td');
      dniCell.textContent = empleado.DNI;
      row.appendChild(dniCell);

      const procesoCell = document.createElement('td');
      procesoCell.textContent = empleado.idProceso;
      row.appendChild(procesoCell);

      const detalleCell = document.createElement('td');
      const detalleButton = document.createElement('button');
      detalleButton.textContent = 'Ver detalle';
      detalleButton.addEventListener('click', () => {
        // Lógica para mostrar el detalle del empleado

        mostrarDetalleEmpleado(empleado.id);

      });
      detalleCell.appendChild(detalleButton);
      row.appendChild(detalleCell);
    
      empleadosBody.appendChild(row);
    
    });

    function mostrarDetalleEmpleado(empleadoId) {
      // Lógica para mostrar el detalle del empleado según el empleadoId
      const url = `detalle_empleado${empleadoId}/`;
      // Redirigir a la URL del detalle del empleado
      window.location.href = url;
    }
    
  })
  .catch(error => {
    console.error('Error al obtener los empleados:', error);
  });






