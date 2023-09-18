import sys

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #Add a title
        self.setWindowTitle('Hello world')

        #set vertical layout 
        self.setLayout(qtw.QVBoxLayout())

        #create a label
        self.my_label = qtw.QLabel("Hello world What's your name?")
        
        self.layout().addWidget(self.my_label)

        #Change font size of label
        self.my_label.setFont(qtg.QFont('Helvetica', 18))

        # Create an entry box
        self.my_entry = qtw.QLineEdit()
        self.my_entry.setObjectName('name_field')
        self.my_entry.setText("")
        self.layout().addWidget(self.my_entry)

        #Create a button 
        my_button = qtw.QPushButton('Press me!', 
                                    clicked=lambda:self.press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

    def press_it(self):
        #Add name to text
        self.my_label.setText(f'Hello {self.my_entry.text()}')
        #Clear the entry box
        self.my_entry.setText('')



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    app.exec_()