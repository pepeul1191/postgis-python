var app = angular.module("myApp", ["ngRoute"]); 

app.config(['$locationProvider', function($locationProvider) {
  $locationProvider.hashPrefix('');
}]);