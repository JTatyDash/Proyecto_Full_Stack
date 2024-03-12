const btnEliminar = document.querySelectorAll('.btn-eliminar');
if (btnEliminar) {
  const btnArray = Array.from(btnEliminar);
  btnArray.forEach((btn) => {
    if (btn) {  // Comprueba si el elemento del botón existe
      btn.addEventListener('click', (e) => {
        if (!confirm('¿Estás seguro que quieres eliminar?')) {
          e.preventDefault();
        }
      });
    }
  });
}
