
document.addEventListener("DOMContentLoaded", function() {
    const botonFiltro = document.getElementById("boton-filtro");
    const optionsContainer = document.getElementById("options-container");
    const applyButton = document.getElementById("apply-button");

    botonFiltro.addEventListener("click", function() {
        // Combiar la visibilidad de options-container
        optionsContainer.classList.toggle("hidden");
    });
});