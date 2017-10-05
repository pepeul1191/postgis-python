$("#upload_file_dni").on("click", function(event){
    $("#view_file_dni").addClass("oculto");
    $("#input_file_dni").upload(
        BASE_URL + "subir",
        {
            nombre : "Imagen 1 nombre",
            descripcion : "Imagen 1 descripcion"
        }, 
        function(mensaje){
            console.log(mensaje);
            event.preventDefault();
        },  
        $("#progbar_dni"),
        $("#upload_file_dni")
    );
    event.preventDefault();
});