
// Cargar comentarios al cargar la página
document.addEventListener("DOMContentLoaded", loadComments);

// Agregar comentario al enviar el formulario
document.getElementById("formulario-comentario").addEventListener("submit", function(e) {
    e.preventDefault();

    const commentText = document.getElementById("comentario").value.trim();
    if (commentText) {
        addComment(commentText);
        document.getElementById("comentario").value = ""; // Limpiar el textarea
    }
});

function loadComments() {
    const commentsSection = document.getElementById("seccion-comentarios");
    const comments = JSON.parse(localStorage.getItem("comentarios")) || [];

    comments.forEach(comment => {
        const commentDiv = document.createElement("div");
        commentDiv.classList.add("comentario");
        commentDiv.textContent = comment;
        commentsSection.appendChild(commentDiv);
    });
}

function addComment(comment) {
    const commentsSection = document.getElementById("seccion-comentarios");

    const commentDiv = document.createElement("div");
    commentDiv.classList.add("comentario");
    commentDiv.textContent = comment;
    commentsSection.appendChild(commentDiv);

    saveComment(comment);
}

function saveComment(comment) {
    const comments = JSON.parse(localStorage.getItem("comentarios")) || [];
    comments.push(comment);
    localStorage.setItem("comentarios", JSON.stringify(comments));
}