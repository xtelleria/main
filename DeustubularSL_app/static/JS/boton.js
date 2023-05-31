const elementsList = document.getElementsByTagName("main");

function getElementFontSize(element) {

  const elementFontSize = window.getComputedStyle(element, null).getPropertyValue('font-size');
  return parseFloat(elementFontSize); 
}

function cambiarTexto(operador) {
  for (let element of elementsList) {
    const currentSize = getElementFontSize(element);


    const newFontSize = (operador === '+' ? (currentSize + 1) : (currentSize - 1)) + 'px';

    element.style.fontSize = newFontSize
  }
}