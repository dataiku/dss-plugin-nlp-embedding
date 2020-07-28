var app = angular.module('modelDownloader.build', []);
var non_transformer_models = ["Word2Vec","FastText","Glove","ELMo",'USE']

app.controller('modelDownloaderController', function($scope) {

    $scope.$watch('config', function(nv) {
        // if (!nv || !$scope.version.create) {
        //     return;
        // }
        // $scope.version.id = $scope.suggestNextName($scope.packages.map(p => p.id));
        console.log("###### watch",{nv})
    });

    $scope.getModels = function(){
        $scope.callPythonDo({method: "get_models"}).then(function(data){
        $scope.models = data['models']
        }); 
        $scope.showLanguageList=true;
        $scope.showModelList=true;
        $scope.showTransformersModelversion=false;
        $scope.showOutputFolder=true;
        console.log("###### init models")
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
        console.log("###### init transformer")

    };

    var init = function(){
        $scope.callPythonDo({method: "get_languages"}).then(function(data){
         $scope.languages = data['languages']
         }); 
         $scope.showLanguageList=true;
         $scope.showModelList=false;
         $scope.showTransformersModelversion=false;
         $scope.showOutputFolder=true;
         console.log("###### init")
         
     };
         
     init();

});