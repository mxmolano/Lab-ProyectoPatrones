async function listarComentarios() {
    const res = await fetch(API_BASE + ENDPOINTS.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaComentarios");
    lista.innerHTML = "";
    data.forEach(c => {
        const item = document.createElement("li");
        item.textContent = `ID: ${c.id} - ${c.usuario_email} - ${c.texto} (${c.calificacion})`;
        lista.appendChild(item);
    });
}

document.getElementById("formComentario").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        texto: document.getElementById("texto").value,
        usuario_email: document.getElementById("email").value,
        calificacion: parseInt(document.getElementById("calificacion").value)
    };
    await fetch(API_BASE + ENDPOINTS.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Comentario creado.");
    listarComentarios();
    mostrarSeccion('lista');
});

async function buscarComentario() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("textoAccion").value = data.texto;
        document.getElementById("emailAccion").value = data.usuario_email;
        document.getElementById("calificacionAccion").value = data.calificacion;
        mostrarSeccion('acciones');
        alert("Comentario cargado para edición.");
    } else {
        alert("Comentario no encontrado.");
    }
}

async function actualizarComentario() {
    const id = document.getElementById("idBuscar").value;
    const body = {
        texto: document.getElementById("textoAccion").value,
        usuario_email: document.getElementById("emailAccion").value,
        calificacion: parseInt(document.getElementById("calificacionAccion").value)
    };
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarComentarios();
    mostrarSeccion('lista');
}

async function eliminarComentario() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarComentarios();
    mostrarSeccion('lista');
}

function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}

listarComentarios();
mostrarSeccion('crear');
