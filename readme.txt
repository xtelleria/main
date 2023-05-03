Grupo 9 ----> Reto 4 (Deustubular)


Repositorio de GitHub : https://github.com/xtelleria/main.git (De momento esta todo en la branch "master"
problemas con el main)

Funcionalidades Extra: 

Comprobar DNI --->Deustubular SL ha mostrado su descontento ya que varios de sus empleados rellenaban el campo de el DNI de una manera diferente cada uno, a veces con espacios entre los numeros, a veces juntos o a veces no añadian ni la ultima letra.Por ello, se ha implementado la funcionalidad de comprobar, por un lado, 
que el DNI que se pretende insertar por parte de un empleado, primero cumple el formato de 8 números y 1 letra
y segundo que no exista ningún DNI idéntico en la base de datos. En caso de que no se cumpla alguna de estas
condiciones se mostrara una página .html mostrando al usuario un mensaje de aviso y no se guardaran los datos
que pretende insertar en la base de datos.

Comprobar Email --->Deustubular SL ha mostrado varias veces su descontento por el motivo de que los empleados
usualmente, se registran con distintos dominios de email y le gustaría englobar todos bajo dos dominios: 
"@deustublar.es y @deusto.es" por ello se ha implementado una funcionalidad para comprobar que el dominio con él
que el empleado registra su dirección de correo coincida con alguno de estos dos. En caso contrario se mostrará una ventana avisando de que el dominio no es válido.

Esto se ha realizado mediante los métodos llamados "comprobar_email" y "comprobar_dni" que se encuentran en "views.py" y se implementan justo antes de guardar el objeto empleado en la base de datos.
_________________________________________________________________________________________________________________

El método para comprobar un DNI se ha logrado gracias a la informacion que se encuentra en: https://www.dev-util.com/python/validar-un-dni-en-python








