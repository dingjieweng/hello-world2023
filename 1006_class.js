var pokemonModule = function(inName){
    var name = inName;
    function sayHello(){
        console.log("hello i'm",name);
    }
    return{
        sayHello: sayHello
    }

}
var pikachu = new pokemonModule('pikachu');
pikachu.sayHello()