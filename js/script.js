var app = angular.module('modelDownloader.build', []);
var non_transformer_models = ["Word2Vec","FastText","Glove","ELMo",'USE']

app.controller('modelDownloaderController', function($scope) {

    $scope.$watch('config', function(nv) {
        if(nv && nv.language){
            return;
        }
        $scope.showLanguageList=true;
        $scope.showModelList=false;
        $scope.showTransformersModelversion=false;
        $scope.showOutputFolder=true;
        $scope.showModelDescription=false;
    });

    $scope.getModels = function(){
        $scope.callPythonDo({method: "get_models"}).then(function(data){
            $scope.models = data['models']
        }); 
        $scope.showLanguageList=true;
        $scope.showModelList=true;
        $scope.showTransformersModelversion=false;
        $scope.showOutputFolder=true;
        $scope.showModelDescription=false;
    };

    $scope.getTransformerModelVersions = function(){      
        $scope.callPythonDo({method:"get_transformer_model_versions"}).then(function(data){
            $scope.transformersModelVersions = data['transformer_model_versions'];
            var model_name = data['model_name'];
            if(non_transformer_models.includes(model_name)){
                $scope.showTransformersModelversion=false;
            }
            else{
                $scope.showTransformersModelversion=true;
            }

        });
        $scope.showLanguageList=true;
        $scope.showModelList=true;
        $scope.showOutputFolder=true;
        $scope.showModelDescription=false;

    };

    $scope.getModelDescription = function(){
        $scope.callPythonDo({method: "get_model_description"}).then(function(data){
            $scope.modelDescription = data['model_description']
        }); 
        $scope.showLanguageList=true;
        $scope.showModelList=true;
        $scope.showTransformersModelversion=true;
        $scope.showOutputFolder=true;
        $scope.showModelDescription=true;
    };

    var init = function(){
        $scope.callPythonDo({method: "get_languages"}).then(function(data){
         $scope.languages = data['languages']
         }); 
         $scope.showLanguageList=true;
         $scope.showModelList=false;
         $scope.showTransformersModelversion=false;
         $scope.showOutputFolder=true;
         $scope.showModelDescription=false;
         
     };
         
     init();

});