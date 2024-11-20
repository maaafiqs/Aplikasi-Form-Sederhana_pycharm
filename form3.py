from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QApplication, QMessageBox
from PyQt6.uic import loadUi
import sys


class formTiga(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi('form3.ui', self)  # Memuat file .ui
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan saat memuat UI: {e}")
            sys.exit(1)

        # Menghubungkan tombol dan input dari file .ui ke variabel Python
        self.tambahButton = self.findChild(QPushButton, "tambahButton")
        self.ubahButton = self.findChild(QPushButton, "ubahButton")
        self.hapusButton = self.findChild(QPushButton, "hapusButton")

        self.editTanggal = self.findChild(QLineEdit, "editTanggal")
        self.editId = self.findChild(QLineEdit, "editId")
        self.editAlamat = self.findChild(QLineEdit, "editAlamat")
        self.editOngkir = self.findChild(QLineEdit, "editOngkir")
        self.editKota = self.findChild(QLineEdit, "editKota")
        self.editTelepon = self.findChild(QLineEdit, "editTelepon")

        # Validasi apakah semua widget ditemukan
        if not all([self.tambahButton, self.ubahButton, self.hapusButton,
                    self.editTanggal, self.editId, self.editAlamat, self.editOngkir, self.editKota, self.editTelepon]):
            QMessageBox.critical(self, "Error", "Beberapa komponen tidak ditemukan di form3.ui!")
            sys.exit(1)

        # Menghubungkan tombol dengan fungsi masing-masing
        self.tambahButton.clicked.connect(self.tambah)
        self.ubahButton.clicked.connect(self.ubah)
        self.hapusButton.clicked.connect(self.hapus)

    def tambah(self):
        # Mengambil data dari input
        tanggal = self.editTanggal.text()
        id = self.editId.text()
        alamat = self.editAlamat.text()
        ongkir = self.editOngkir.text()
        kota = self.editKota.text()
        telepon = self.editTelepon.text()

        # Validasi data
        if not tanggal or not id or not alamat or not ongkir or not kota or not telepon:
            QMessageBox.critical(self, "Error", "Semua kolom harus diisi!")
            return

        # Menampilkan pesan bahwa data berhasil diinput
        QMessageBox.information(
            self,
            "Berhasil",
            f"Data telah berhasil diinput:\n\n"
            f"Tanggal: {tanggal}\nId: {id}\nAlamat: {alamat}\nOngkir: {ongkir}\nKota: {kota}\nTelepon: {telepon}"
        )

    def ubah(self):
        # Mengambil data baru dari input
        tanggal = self.editTanggal.text()
        id = self.editId.text()
        alamat = self.editAlamat.text()
        ongkir = self.editOngkir.text()
        kota = self.editKota.text()
        telepon = self.editTelepon.text()

        # Validasi data
        if not tanggal or not id or not alamat or not ongkir or not kota or not telepon:
            QMessageBox.critical(self, "Error", "Semua kolom harus diisi untuk mengubah data!")
            return

        # Menampilkan pesan bahwa data berhasil diubah
        QMessageBox.information(
            self,
            "Berhasil",
            f"Data telah berhasil diubah menjadi:\n\n"
            f"Tanggal: {tanggal}\nId: {id}\nAlamat: {alamat}\nOngkir: {ongkir}\nKota: {kota}\nTelepon: {telepon}"
        )

    def hapus(self):
        # Mengosongkan semua kolom input
        self.editTanggal.clear()
        self.editId.clear()
        self.editAlamat.clear()
        self.editOngkir.clear()
        self.editKota.clear()
        self.editTelepon.clear()

        # Menampilkan pesan bahwa data telah dihapus
        QMessageBox.information(
            self,
            "Berhasil",
            "Semua data telah berhasil dihapus!"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = formTiga()
    window.show()
    sys.exit(app.exec())
