const elementsList = document.getElementsByTagName("main");

function getElementFontSize(element) {
  //getComputedStyle nos devuelve las propiedades css de cada elemento
  const elementFontSize = window.getComputedStyle(element, null).getPropertyValue('font-size');
  return parseFloat(elementFontSize);  //Devolvemos el total de pixeles
}

function cambiarTexto(operador) {
  for (let element of elementsList) {
    const currentSize = getElementFontSize(element);

    //Restar o sumar, dependiendo del operador.
    const newFontSize = (operador === '+' ? (currentSize + 1) : (currentSize - 1)) + 'px';
    //Aplicarle la lista actual el nuevo tamaño.
    element.style.fontSize = newFontSize
  }
}