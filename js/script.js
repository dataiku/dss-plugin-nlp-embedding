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
        $scope.showNewOutputFolder = false;
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

    $scope.getIsCustomFolder = function(){
        $scope.callPythonDo({method: "get_is_custom_folder"}).then(function(data){
            var is_cutom_folder = data["is_cutom_folder"]
            console.log("is_custom_folder")
            console.log(is_cutom_folder)
            if(is_cutom_folder){
                $scope.showNewOutputFolder = true;
            }
            else{
                $scope.showNewOutputFolder = false;
            }
        }); 

    };

    var init = function(){
        $scope.callPythonDo({method: "init_form"}).then(function(data){
            $scope.languages = data['languages']
            $scope.outputFolders = data['output_folders']
         }); 
        $scope.showLanguageList=true;
        $scope.showModelList=false;
        $scope.showTransformersModelversion=false;
        $scope.showOutputFolder=true;
        $scope.showModelDescription=false;
        
     };
         
     init();

});