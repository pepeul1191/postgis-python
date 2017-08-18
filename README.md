## Boilerplate Flask Python

Requisitos de software previamente instalado:

	+ Python 2.7
	+ Python PIP
	+ NodeJS - NPM - Gulp

### Descipción

Servicio web desarrollado en PHP usando el framework FlightPHP, con patrones de diseño front-controller y distpacher y la interfaz de Idiorm para interactuar con la base de datos.

Instalación de dependencias:

	$ sudo pip install -r requirements.txt && npm install && bower install 

### Rutas

	+ GET -> / : IndexController#index
	+ GET -> /error/404 : ErrorController#error_404
	+ POST -> /usuario/acceder : UsuarioController#acceder

### Generar 'dist'
	
	$ gulp layout && gulp app && gulp error-css

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]