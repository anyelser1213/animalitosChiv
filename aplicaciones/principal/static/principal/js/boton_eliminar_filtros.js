//Con esta funcion quitamos la opcion para que busque por filtro
function EliminarFiltros(){


    //console.log("Estamos eliminando el filtro");


    if (document.getElementById("divFiltroFecha").children[1].value != "") {
        console.log("El elemento tiene una fecha establecida");
        //document.getElementById("divFiltroFecha").value="";

        //console.log("1",document.getElementById("divFiltroFecha").children[1]);
        //console.log("1",document.getElementById("divFiltroFecha").children[1].value);
        document.getElementById("divFiltroFecha").children[1].value ="";

    }
    else {
        console.log("El elemento no tiene fecha establecida");
    }

}