var app = angular.module('modelDownloader.build', []);

app.controller('modelDownloaderController', function($scope) {

    $scope.getModels = function(){
        $scope.callPythonDo({method: "get_models"}).then(function(data){
        $scope.models = data['models']
        }); 
        
        $scope.showModelList=true;
        $scope.showLanguageList=false;

    };

    var init = function(){
        $scope.callPythonDo({method: "get_languages"}).then(function(data){
         $scope.languages = data['languages']
         }); 
         $scope.showLanguageList=true;
         $scope.showModelList=false;
         
     };
         
     init();

});