


var img = document.getElementById("imagenLogin");
var IconoWeb = document.getElementById("iconPagWeb");

//console.log(csrftoken);


    var resultados = "Cargando...";
    console.log("Probando", resultados);
	fetch("/api_login",{
            method:"GET",
            headers:{
                "X-CSRFToken":csrftoken,
                "X-Requestd-With":"XMLGttpRequest"//Con esto indicamos que es una peticion ajax
            }

    //Promesa de javascript
    }).then(
        function(response){
            return response.json();
            //console.log(response.data);
        }
    ).then(
        function(data){

            //console.log(data);

            //console.log(data.FondoLogin);
            

            IconoWeb.setAttribute("href",data.ImagenLogin);
            //{% static 'src/img/logo_login.jpg' %} esto lo quitamos del login.html
            


            //AQUI PARA MODIFICAR EL ICONO

            

        }
    ) 