document.addEventListener("DOMContentLoaded", function () {

  // ================= DELETE =================
  const deleteModal = document.getElementById("deleteModal");
  const modalText = document.getElementById("modalText");
  const deleteForm = document.getElementById("deleteForm");
  const closeDelete = document.getElementById("closeModal");

  document.querySelectorAll(".btn-delete").forEach(btn => {
    btn.addEventListener("click", function () {
      const id = this.dataset.id;
      const nama = this.dataset.nama;

      deleteModal.style.display = "block";
      modalText.innerText = `Yakin ingin menghapus ${nama}?`;

      deleteForm.action = `/siswa/delete/${id}/`;
    });
  });

  closeDelete.onclick = () => deleteModal.style.display = "none";


  // ================= UPDATE =================
  const updateModal = document.getElementById("updateModal");
  const closeUpdate = document.getElementById("closeUpdateModal");
  const updateForm = document.getElementById("updateForm");

  document.querySelectorAll(".btn-edit").forEach(btn => {
    btn.addEventListener("click", function () {
      const d = this.dataset;

      updateModal.style.display = "block";

      // set value ke form
      document.getElementById("editNama").value = d.nama;
      document.getElementById("editNik").value = d.nik;
      document.getElementById("editNis").value = d.nis;
      document.getElementById("editNisn").value = d.nisn;
      document.getElementById("editTahun").value = d.tahun;
      document.getElementById("editAlamat").value = d.alamat;
      document.getElementById("editKontak").value = d.kontak;

      updateForm.action = `/siswa/update/${d.id}/`;
    });
  });

  closeUpdate.onclick = () => updateModal.style.display = "none";


  // ================= GLOBAL CLOSE =================
  window.onclick = function(e) {
    if (e.target === deleteModal) deleteModal.style.display = "none";
    if (e.target === updateModal) updateModal.style.display = "none";
  };

});