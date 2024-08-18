
// Conetidos de la seccion maestros
const imgs = [
    "Perfil.jpg", "Perfil.jpg", "Perfil.jpg", 
    "Perfil.jpg", "Perfil.jpg"
];

const nombres = ["1", "2", "3", "4", "5"];
const modulos = ["1", "2", "3", "4", "5"];

const parrafos = [
    "Lorem ipsum dolor sit, amet consectetur adipisicing 1", 
    "Lorem ipsum dolor sit, amet consectetur adipisicing 2",
    "Lorem ipsum dolor sit, amet consectetur adipisicing 3", 
    "Lorem ipsum dolor sit, amet consectetur adipisicing 4",
    "Lorem ipsum dolor sit, amet consectetur adipisicing 5"
];

const seccion = document.getElementById("seccion");
const imagen = document.getElementById("img");
const parrafo = document.getElementById("parrafo");
const nombre = document.getElementById("nombre");
const modulo = document.getElementById("modulo");

var contador = 0;

function botonDerecho() {
    seccion.classList.add("fade-out");

    setTimeout(() => {
        imagen.src = "../IMG/" + imgs[contador];
        parrafo.innerHTML = parrafos[contador];
        nombre.innerHTML = nombres[contador];
        modulo.innerHTML = "<span>Módulo:</span> " + modulos[contador];

        contador < 4 ? contador++ : contador = 0;

        seccion.classList.remove("fade-out");
    }, 500);
}

function botonIzquierdo() {
    seccion.classList.add("fade-out");

    setTimeout(() => {
        contador > 0 ? contador-- : contador = imgs.length - 1;

        imagen.src = "../IMG/" + imgs[contador];
        parrafo.innerHTML = parrafos[contador];
        nombre.innerHTML = nombres[contador];
        modulo.innerHTML = "<span>Módulo:</span> " + modulos[contador];

        seccion.classList.remove("fade-out");
    }, 500);    
}