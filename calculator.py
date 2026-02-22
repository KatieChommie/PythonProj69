import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class MyCalc(QDialog):  # ใช้ QDialog ตามในรูปของคุณ
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("calc.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # เปลี่ยนชื่อเรียกให้ตรงกับรูป (lineEdit, plus, minus, etc.)
        self.ui.plus.clicked.connect(lambda: self.add_op("+"))
        self.ui.minus.clicked.connect(lambda: self.add_op("-"))
        self.ui.multiply.clicked.connect(lambda: self.add_op("*"))
        self.ui.division.clicked.connect(lambda: self.add_op("/"))

        # สมมติว่าคุณมีปุ่มชื่อ equal และ clear ด้วย (ถ้าไม่มีให้ไปตั้งชื่อใน Designer นะครับ)
        if hasattr(self.ui, 'equal'):
            self.ui.equal.clicked.connect(self.calculate)

    def add_op(self, char):
        # ใช้ชื่อ lineEdit ตามรูป
        current = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(current + char)

    def calculate(self):
        try:
            result = eval(self.ui.lineEdit.text())
            self.ui.lineEdit.setText(str(result))
        except:
            self.ui.lineEdit.setText("Error")


app = QApplication(sys.argv)
window = MyCalc()
window.ui.show()  # เรียก show ผ่านตัวแปร ui
sys.exit(app.exec())