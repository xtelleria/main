const API_URL= "http://127.0.0.1:8000/empleados"
fetch(API_URL)
    .then(response => response.json())
    .then(json=>{
        addRows(json);
    });

function addRows(empleados) {
    tbody = document.getElementById("tbody");
    empleados.forEach(element => {
        tbody.appendChild(createEmpleadosRow(element))
    });
}
function createEmpleadosRow(empleados){
    let row = document.createElement("tr")

    let nombre=document.createElement("td")
    nombre.textContent= empleados.nombre;
    row.appendChild(nombre);

    let apellidos = document.createElement("td")
    apellidos.textContent= empleados.apellidos;
    row.appendChild(telefono);

let enlace_empleado= document.createElement("td")
let enlace = document.createElement("a")
    enlace.setAttribute("href", "{% url 'detalle_empleado' empleado.id %}"+ empleados)
    enlace.innerHTML="ver detalles"
    enlace.className= "enlace"
    enlace_empleado.appendChild(enlace);
    row.appendChild(enlace_empleado);
return row;
}