from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt6.uic import loadUi
from form2 import formDua
from form3 import formTiga
from form4 import formEmpat  # Pastikan form4 memiliki kelas formEmpat
import sys


class formSatu(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            loadUi('form1.ui', self)  # Memuat file .ui untuk form1
        except Exception as e:
            print(f"Error saat memuat form1.ui: {e}")
            sys.exit(1)

        # Menghubungkan tombol tampil form2
        self.button_tampil_form2 = self.findChild(QPushButton, "button_tampil_form2")
        if not self.button_tampil_form2:
            print("Error: Button 'button_tampil_form2' tidak ditemukan di form1.ui")
            sys.exit(1)

        self.button_tampil_form2.clicked.connect(self.tampil_form2)

        # Menghubungkan tombol tampil form3
        self.button_tampil_form3 = self.findChild(QPushButton, "button_tampil_form3")
        if not self.button_tampil_form3:
            print("Error: Button 'button_tampil_form3' tidak ditemukan di form1.ui")
            sys.exit(1)

        self.button_tampil_form3.clicked.connect(self.tampil_form3)

        # Menghubungkan tombol tampil form4
        self.button_tampil_form4 = self.findChild(QPushButton, "button_tampil_form4")
        if not self.button_tampil_form4:
            print("Error: Button 'button_tampil_form4' tidak ditemukan di form1.ui")
            sys.exit(1)

        self.button_tampil_form4.clicked.connect(self.tampil_form4)

    def tampil_form2(self):
        try:
            self.form2 = formDua()  # Membuat instance form2
            self.form2.show()  # Menampilkan form2
        except Exception as e:
            print(f"Error saat membuka form2: {e}")

    def tampil_form3(self):
        try:
            self.form3 = formTiga()  # Membuat instance form3
            self.form3.show()  # Menampilkan form3
        except Exception as e:
            print(f"Error saat membuka form3: {e}")

    def tampil_form4(self):
        try:
            self.form4 = formEmpat()  # Membuat instance form4
            self.form4.show()  # Menampilkan form4
        except Exception as e:
            print(f"Error saat membuka form4: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = formSatu()
    window.show()
    sys.exit(app.exec())
