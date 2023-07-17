
// SCRIPTS PAGINA LISTA =============================================================
var modal = document.getElementById("modal_lista");
// var btns = document.getElementsByClassName("openmodal");
var span = document.getElementsByClassName("close")[0];

// Associar evento de clique a todos os botões
// for (var i = 0; i < btns.length; i++) {
//   btns[i].addEventListener("click", function() {
//       modal.style.display = "block";
//   });
// }

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
      modal.style.display = "none";
  }
}

function openModal(foto,nome, idade) {
  modal.style.display = "block";
  document.getElementById('modal-foto').src = foto
  document.getElementById('modal-nome').textContent = nome
  document.getElementById('modal-idade').textContent = "Idade: "+idade+" anos"
}
// FIM PAGINA LISTA =============================================================