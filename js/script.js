var app = angular.module('modelDownloader.build', []);

app.controller('modelDownloaderController', function($scope) {

    var init = function(){
        $scope.callPythonDo({method: "get_languages"}).then(function(data){
         $scope.languages = data['languages']
         }); 
         $scope.showLanguageList=true;
 
         
     };
         
     init();

});