
document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById("file-input");
    const botonCambioFoto = document.querySelector(".boton-cambio-foto");
    const imageContainer = document.getElementById("image-container");

    // Cargar la imagen desde localStorage al cargar la página
    function loadImage() {
        const storedImage = localStorage.getItem("profileImage");
        if (storedImage) {
            imageContainer.src = storedImage;
        }
    }

    // Guardar la imagen en localStorage
    function saveImage(src) {
        localStorage.setItem("profileImage", src);
    }

    // Mostrar la imagen seleccionada
    function displayImage(file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            imageContainer.src = event.target.result;
            saveImage(event.target.result); // Guardar la imagen en localStorage
        };
        reader.readAsDataURL(file);
    }

    // Manejar click en el botón de cambio de foto
    botonCambioFoto.addEventListener("click", function() {
        fileInput.click();
    });

    // Manejar selección de archivo
    fileInput.addEventListener("change", function() {
        if (fileInput.files.length > 0) {
            displayImage(fileInput.files[0]);
        }
    });

    // Cargar la imagen al inicio
    loadImage();
});