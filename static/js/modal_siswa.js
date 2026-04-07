document.addEventListener("DOMContentLoaded", function () {

  // ================= ELEMENT =================
  const updateModal = document.getElementById("updateModal");
  const deleteModal = document.getElementById("deleteModal");

  const closeUpdate = document.getElementById("closeUpdateModal");
  const closeDelete = document.getElementById("closeModal");

  const updateForm = document.getElementById("updateForm");
  const deleteForm = document.getElementById("deleteForm");

  const modalText = document.getElementById("modalText");


  // ================= UPDATE MODAL =================
  document.querySelectorAll(".btn-edit").forEach(btn => {
    btn.addEventListener("click", function () {
      const d = this.dataset;

      // tampilkan modal
      updateModal.style.display = "flex";

      // isi form
      document.getElementById("editNama").value = d.nama;
      document.getElementById("editNik").value = d.nik;
      document.getElementById("editNis").value = d.nis;
      document.getElementById("editNisn").value = d.nisn;
      document.getElementById("editTahun").value = d.tahun;
      document.getElementById("editAlamat").value = d.alamat;
      document.getElementById("editKontak").value = d.kontak;

      updateForm.action = `/dashboard/update_data/${d.id}/`;
    });
  });


  // ================= DELETE MODAL =================
  document.querySelectorAll(".btn-delete").forEach(btn => {
    btn.addEventListener("click", function () {
      const id = this.dataset.id;
      const nama = this.dataset.nama;

      // tampilkan modal
      deleteModal.style.display = "flex";

      // isi teks konfirmasi
      modalText.innerText = `Yakin ingin menghapus data ${nama}?`;

      // set action
      deleteForm.action = `dashboard/delete_data/${id}/`;
    });
  });


  // ================= CLOSE BUTTON =================
  if (closeUpdate) {
    closeUpdate.onclick = () => {
      updateModal.style.display = "none";
    };
  }

  if (closeDelete) {
    closeDelete.onclick = () => {
      deleteModal.style.display = "none";
    };
  }


  // ================= CLICK OUTSIDE (GLOBAL CLOSE) =================
  window.onclick = function (e) {
    if (e.target === updateModal) {
      updateModal.style.display = "none";
    }

    if (e.target === deleteModal) {
      deleteModal.style.display = "none";
    }
  };


  // ================= ESC KEY CLOSE =================
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      updateModal.style.display = "none";
      deleteModal.style.display = "none";
    }
  });

});