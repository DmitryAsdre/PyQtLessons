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
        self.my_label = qtw.QLabel("Pick something from the list")
        
        self.layout().addWidget(self.my_label)

        #Change font size of label
        self.my_label.setFont(qtg.QFont('Helvetica', 24))

        # Create an combo box
        self.my_combo = qtw.QComboBox(self,
                                      editable=True,
                                      insertPolicy=qtw.QComboBox.InsertAtTop)
        #Add items to combo box
        self.my_combo.addItem('Pepperoni', 'Something') # (text, data, index)
        self.my_combo.addItem('Cheese', 2)
        self.my_combo.addItem('Mushroom', qtw.QWidget)
        self.my_combo.addItem('Peppers')
        
        #Put combo on the screen 
        self.layout().addWidget(self.my_combo)

        #Create a button 
        my_button = qtw.QPushButton('Press me!', 
                                    clicked=lambda:self.press_it())
        self.layout().addWidget(my_button)

        #show the app
        self.show()

    def press_it(self):
        #Add name to text
        #self.my_label.setText(f'You picked {self.my_combo.currentText()}')

        self.my_label.setText(f'You picked <data> : {self.my_combo.currentData()}')
        #self.my_label.setText(f'You picked <index> : {self.my_combo.currentIndex()}')



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()

    app.exec_()