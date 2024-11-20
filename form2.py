from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QApplication, QMessageBox
from PyQt6.uic import loadUi
import sys

class formDua(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi('form2.ui', self)  # Memuat file .ui
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan saat memuat UI: {e}")
            sys.exit(1)

        # Menghubungkan tombol dengan fungsi masing-masing
        self.submitButton.clicked.connect(self.submit)
        self.ubahButton.clicked.connect(self.ubah)
        self.hapusButton.clicked.connect(self.hapus)

    def submit(self):
        # Mengambil data dari input
        nama = self.editPengguna.text()
        telepon = self.editTelepon.text()
        email = self.editEmail.text()
        alamat = self.editAlamat.text()

        # Validasi data
        if not nama or not telepon or not email or not alamat:
            QMessageBox.critical(self, "Error", "Semua kolom harus diisi!")
            return

        # Menampilkan pesan bahwa data berhasil diinput
        QMessageBox.information(
            self,
            "Berhasil",
            f"Data telah berhasil diinput:\n\n"
            f"Nama: {nama}\nTelepon: {telepon}\nEmail: {email}\nAlamat: {alamat}"
        )

    def ubah(self):
        # Mengambil data baru dari input
        nama = self.editPengguna.text()
        telepon = self.editTelepon.text()
        email = self.editEmail.text()
        alamat = self.editAlamat.text()

        # Validasi data
        if not nama or not telepon or not email or not alamat:
            QMessageBox.critical(self, "Error", "Semua kolom harus diisi untuk mengubah data!")
            return

        # Menampilkan pesan bahwa data berhasil diubah
        QMessageBox.information(
            self,
            "Berhasil",
            f"Data telah berhasil diubah menjadi:\n\n"
            f"Nama: {nama}\nTelepon: {telepon}\nEmail: {email}\nAlamat: {alamat}"
        )

    def hapus(self):
        # Mengosongkan semua kolom input
        self.editPengguna.clear()
        self.editTelepon.clear()
        self.editEmail.clear()
        self.editAlamat.clear()

        # Menampilkan pesan bahwa data telah dihapus
        QMessageBox.information(
            self,
            "Berhasil",
            "Semua data telah berhasil dihapus!"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = formDua()
    window.show()
    sys.exit(app.exec())
