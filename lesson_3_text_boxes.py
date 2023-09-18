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
        self.my_label = qtw.QLabel("Type something in the box below!")
        
        self.layout().addWidget(self.my_label)

        #Change font size of label
        self.my_label.setFont(qtg.QFont('Helvetica', 24))

        # Create text box
        self.my_text = qtw.QTextEdit(self,
                                     #plainText='Real text ',
                                     #html='<h1>Big header!</b1>', #Html text as plain text
                                     acceptRichText=True, #Colored text or bold or smth
                                     lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                     lineWrapColumnOrWidth=20,
                                     placeholderText='Hello World!',
                                     readOnly=False)
        

        
        #Put combo on the screen 
        self.layout().addWidget(self.my_text)

        #Create a button 
        my_button = qtw.QPushButton('Press me!', 
                                    clicked=lambda:self.press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

    def press_it(self):
        #Add name to text
        #self.my_label.setText(f'You picked {self.my_combo.currentText()}')
        self.my_label.setText(f'You typed {self.my_text.toPlainText()}!')
        self.my_text.setPlainText(f'You pressed button!')

        #self.my_label.setText(f'You picked <data> : {self.my_spin.currentData()}')
        #self.my_label.setText(f'You picked <index> : {self.my_combo.currentIndex()}')



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    app.exec_()