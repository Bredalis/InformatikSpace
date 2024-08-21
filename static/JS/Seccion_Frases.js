
// Conetidos de la seccion frases
const imgs = [
    "/static/IMG/Conexiones.jpg", "/static/IMG/Crecimiento.jpg", 
    "/static/IMG/Aprendizaje.jpg", "/static/IMG/Apoyo.jpg", "/static/IMG/Logros.jpg"
];

const temas = [
    "Inspiración y Conexión", "Comunidad y Crecimiento", 
    "Conocimiento y Aprendizaje", "Inclusividad y Apoyo", 
    "Pasión y Logros"
];

const frases = [
    "Donde las ideas se encuentran: en InformatikSpace, la inspiración fluye a través de la conexión entre mentes brillantes", 
    "Unidos por la pasión, crecemos juntos: en InformatikSpace, cada contribución fortalece nuestra comunidad.",
    "El conocimiento es poder compartido: en InformatikSpace, cada proyecto y experiencia es una oportunidad para aprender y enseñar.", 
    "Aquí todos tienen un lugar: en InformatikSpace, apoyamos a cada programador y entusiasta para que pueda brillar y avanzar",
    "Transforma tu pasión en logros: en InformatikSpace, cada reto es una oportunidad para alcanzar nuevas alturas en el mundo de la informática."
];

const seccion = document.getElementById("seccion");
const imagen = document.getElementById("img");
const frase = document.getElementById("frase");
const tema = document.getElementById("tema");

var contador = 0;

function botonDerecho() {
    seccion.classList.add("fade-out");

    setTimeout(() => {
        imagen.src = imgs[contador];
        frase.innerHTML = frases[contador];
        tema.innerHTML = "<span>Tema:</span> " + temas[contador];

        contador < 4 ? contador++ : contador = 0;

        seccion.classList.remove("fade-out");
    }, 500);
}

function botonIzquierdo() {
    seccion.classList.add("fade-out");

    setTimeout(() => {
        contador > 0 ? contador-- : contador = imgs.length - 1;

        imagen.src = imgs[contador];
        frase.innerHTML = frases[contador];
        tema.innerHTML = "<span>Tema:</span> " + temas[contador];

        seccion.classList.remove("fade-out");
    }, 500);    
}