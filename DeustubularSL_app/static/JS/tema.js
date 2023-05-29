function cambiarTema() {
    var body = document.body;
    var celdas = document.getElementsByTagName('td');
    var urls = document.getElementsByTagName('a');
    var header = document.getElementsByTagName('header')
    var footer = document.getElementsByTagName('footer')

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
      for (var i = 0; i < footer.length; i++) {
        footer[i].classList.toggle('invertir-footer');
      }



    
    
  }