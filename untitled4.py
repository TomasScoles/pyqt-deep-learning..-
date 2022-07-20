import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QGridLayout, QGroupBox, 
         QPushButton, QRadioButton, QWidget, QLineEdit)
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.createExampleGroupbox1(), 0, 0)
      
     
        grid.addWidget(self.createExampleGroupbox2(), 0, 1)
       
        self.setLayout(grid)

 
   

        self.setWindowTitle("PyQt5 Group Box")
        self.resize(800, 350)
        label = QLabel("Python GUI Development - Geekscoders.com", self)
        label.setText("Enter the number of tickets sold \nfor each class of seats")
       
        label.setFont(QFont("Sanserif", 12))
       
        label.setGeometry(QtCore.QRect(50, 50, 500, 100))
        
        labe11 = QLabel("Python GUI Development - Geekscoders.com", self)
        labe11.setText("Class A:\n\nClass B:\n\nClass C:")
       
        labe11.setFont(QFont("Sanserif", 12))
       
        labe11.setGeometry(QtCore.QRect(100, 50, 500, 300))
        
        class1 = QLineEdit("0",self)
        class1.setGeometry(QtCore.QRect(100,500,100,20))

        class1.move(180, 150)
        
        class2 = QLineEdit("0",self)
        class2.setGeometry(QtCore.QRect(100,500,100,20))

        class2.move(180, 190)
        
        class3 = QLineEdit("0",self)
        class3.setGeometry(QtCore.QRect(100,500,100,20))

        class3.move(180, 230)
        
        
        b1 = QPushButton('Calculate\n Revenue',self)
        b1.setGeometry(QtCore.QRect(100,400,100,40))
        b1.move(250, 280)
        def clicked():
            classa.setText(str(int(class1.text())*15))
            classb.setText(str(int(class2.text())*12))
            classc.setText(str(int(class3.text())*9))
            total.setText(str(int(class1.text())*15+int(class2.text())*12+int(class3.text())*9))
        b1.clicked.connect(clicked)
        def r_clicked():
            class1.setText("0")
            class2.setText("0")
            class3.setText("0")
            clicked()
        
        def exit():
            self.close()
            
        
        b2 = QPushButton('Clear',self)
        b2.setGeometry(QtCore.QRect(100,400,100,40))
        b2.move(400, 280)
        b2.clicked.connect(r_clicked)
        b3 = QPushButton('Exit',self)
        b3.setGeometry(QtCore.QRect(100,400,100,40))
        b3.move(550, 280)
        b3.clicked.connect(exit)
        
        
        
        classa = QLineEdit("0",self)
        classa.setGeometry(QtCore.QRect(100,500,100,20))

        classa.move(580, 110)
        
        classb = QLineEdit("0",self)
        classb.setGeometry(QtCore.QRect(100,500,100,20))

        classb.move(580, 150)
        
        classc = QLineEdit("0",self)
        classc.setGeometry(QtCore.QRect(100,500,100,20))

        classc.move(580, 190)
        
        total = QLineEdit("0",self)
        total.setGeometry(QtCore.QRect(100,500,100,20))

        total.move(580, 230)
        
        label.setGeometry(QtCore.QRect(50, 50, 500, 100))
        
        labe12 = QLabel("Python GUI Development - Geekscoders.com", self)
        labe12.setFont(QFont("Sanserif", 12))
        labe12.setGeometry(QtCore.QRect(150, 150, 100, 150))
        labe12.setText("Class A:\n\nClass B:\n\nClass C:\n\nTotal:")
       # labe12.move(480, 100)

    def createExampleGroupbox1(self):
        groupBox = QGroupBox("Ticket Sold")
        groupBox.setFont(QFont('Arial', 16))
        radio1 = QRadioButton("&Radio pizza")
        radio2 = QRadioButton("R&adio taco")
        radio3 = QRadioButton("Ra&dio burrito")
      
        
 

        
        

        return groupBox
    def createExampleGroupbox2(self):
        groupBox = QGroupBox("Revenue generated")
        groupBox.setFont(QFont('Arial', 16))
        radio1 = QRadioButton("&Radio pizza")
        radio2 = QRadioButton("R&adio taco")
        radio3 = QRadioButton("Ra&dio burrito")

        radio1.setChecked(True)

       

        return groupBox
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())