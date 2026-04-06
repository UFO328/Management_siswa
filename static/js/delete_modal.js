document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("deleteModal");
  const modalText = document.getElementById("modalText");
  const deleteForm = document.getElementById("deleteForm");
  const closeModal = document.getElementById("closeModal");

  document.querySelectorAll(".btn-delete").forEach(button => {
    button.addEventListener("click", function () {
      const id = this.dataset.id;
      const nama = this.dataset.nama;

      modal.style.display = "block";
      modalText.innerText = `Yakin ingin menghapus ${nama}?`;

      deleteForm.action = `/siswa/delete/${id}/`;
    });
  });

  closeModal.addEventListener("click", () => {
    modal.style.display = "none";
  });

  window.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.style.display = "none";
    }
  });
});