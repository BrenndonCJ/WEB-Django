const mModal = document.getElementById('modal_cadastro')

function openModalCadastro(){
    mModal.style.display = 'flex'
}

window.onclick = function(event) {
    if (event.target == mModal) {
        mModal.style.display = "none";
    }
}
