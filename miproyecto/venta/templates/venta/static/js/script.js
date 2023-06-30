/*Formulario Inicio Sesion*/
$(document).ready(function(){
    $(".error").hide();

    $("#ingresar").click(function(){
        var email = "";
        email = $("#email").val();

        if (email.length == 0){
            $(".error").show();
        }else{
            $(".error").hide();
        }

    });

    
});