import sys

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!")

        self.form_layout = qtw.QFormLayout()

        self.setLayout(self.form_layout)

        #Add widgets

        self.label_1 = qtw.QLabel('This is a cool label row!')
        self.label_1.setFont(qtg.QFont('Helvetica', 24))

        self.f_name = qtw.QLineEdit(self)
        self.l_name = qtw.QLineEdit(self)

        # Add rows to app

        self.form_layout.addRow(self.label_1)
        self.form_layout.addRow("First Name:", self.f_name)
        self.form_layout.addRow('Last Name:', self.l_name)

        self.form_layout.addRow(qtw.QPushButton('Press Me!', clicked=lambda: self.press_it()))

        self.show()

    def press_it(self):
        self.label_1.setText(f'You clicked the button {self.f_name.text()}, {self.l_name.text()}!')

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    mv = MainWindow()

    app.exec_()