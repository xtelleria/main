function cambiarTema() {
    var body = document.body;
    var celdas = document.getElementsByTagName('td');
    var urls = document.getElementsByTagName('a');
    var header = document.getElementsByTagName('header')
    body.classList.toggle('invertir-fondo');
    for (var i = 0; i < celdas.length; i++) {
        celdas[i].classList.toggle('invertir-td');
      }
    for (var i = 0; i < urls.length; i++) {
        urls[i].classList.toggle('invertir-urls');
      }
      for (var i = 0; i < header.length; i++) {
        header[i].classList.toggle('invertir-header');
      }

    
    
  }