from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QApplication, QMessageBox
from PyQt6.uic import loadUi
import sys


class formEmpat(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi('form4.ui', self)  # Memuat file .ui
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan saat memuat UI: {e}")
            sys.exit(1)

        # Menghubungkan tombol dan input dari file .ui ke variabel Python
        self.tambahButton = self.findChild(QPushButton, "tambahButton")
        self.ubahButton = self.findChild(QPushButton, "ubahButton")
        self.hapusButton = self.findChild(QPushButton, "hapusButton")

        self.editNama = self.findChild(QLineEdit, "editNama")
        self.editDeskripsi = self.findChild(QLineEdit, "editDeskripsi")
        self.editHarga = self.findChild(QLineEdit, "editHarga")
        self.editKategori = self.findChild(QLineEdit, "editKategori")

        # Validasi apakah semua widget ditemukan
        if not all([self.tambahButton, self.ubahButton, self.hapusButton,
                    self.editNama, self.editDeskripsi, self.editHarga, self.editKategori]):
            QMessageBox.critical(self, "Error", "Beberapa komponen tidak ditemukan di form4.ui!")
            sys.exit(1)

        # Menghubungkan tombol dengan fungsi masing-masing
        self.tambahButton.clicked.connect(self.tambah)
        self.ubahButton.clicked.connect(self.ubah)
        self.hapusButton.clicked.connect(self.hapus)

    def tambah(self):
        # Mengambil data dari input
        nama = self.editNama.text()
        deskripsi = self.editDeskripsi.text()
        harga = self.editHarga.text()
        kategori = self.editKategori.text()

        # Validasi data
        if not nama or not deskripsi or not harga or not kategori:
            QMessageBox.critical(self, "Error", "Semua kolom harus diisi!")
            return

        # Menampilkan pesan bahwa data berhasil diinput
        QMessageBox.information(
            self,
            "Berhasil",
            f"Data telah berhasil diinput:\n\n"
            f"Nama: {nama}\nDeskripsi: {deskripsi}\nHarga: {harga}\nKategori: {kategori}"
        )

    def ubah(self):
        # Mengambil data baru dari input
        nama = self.editNama.text()
        deskripsi = self.editDeskripsi.text()
        harga = self.editHarga.text()
        kategori = self.editKategori.text()

        # Validasi data
        if not nama or not deskripsi or not harga or not kategori:
            QMessageBox.critical(self, "Error", "Semua kolom harus diisi untuk mengubah data!")
            return

        # Menampilkan pesan bahwa data berhasil diubah
        QMessageBox.information(
            self,
            "Berhasil",
            f"Data telah berhasil diubah menjadi:\n\n"
            f"Nama: {nama}\nDeskripsi: {deskripsi}\nHarga: {harga}\nKategori: {kategori}"
        )

    def hapus(self):
        # Mengosongkan semua kolom input
        self.editNama.clear()
        self.editDeskripsi.clear()
        self.editHarga.clear()
        self.editKategori.clear()

        # Menampilkan pesan bahwa data telah dihapus
        QMessageBox.information(
            self,
            "Berhasil",
            "Semua data telah berhasil dihapus!"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = formEmpat()
    window.show()
    sys.exit(app.exec())
