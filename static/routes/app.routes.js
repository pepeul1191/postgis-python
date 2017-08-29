app.config(function($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl : STATIC_URL + 'pages/home.html'
  })
  .when('/contacto', {
    templateUrl : STATIC_URL + 'pages/contacto.html'
  })
  .otherwise({ redirectTo: '/' });
});