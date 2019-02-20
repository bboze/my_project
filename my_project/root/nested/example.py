import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#from root.nested.wst import Wst

from wst import Wst

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import traceback
import time


 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'WEB SERVICES TEST TOOL'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 400
        
        #create GUI
        self.initUI()        
        
 
    def initUI(self):
        #window setting
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        #file menu
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
 
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        
        browseButton = QAction(QIcon('exit24.png'), 'Browser', self)
        browseButton.setShortcut('Ctrl+B')
        browseButton.setStatusTip('Open browser')
        browseButton.triggered.connect(self.test_browser)
        toolsMenu.addAction(browseButton)        
        
        #main window components
        centralWidget = MainWindow()          
        self.setCentralWidget(centralWidget) 
        
        self.statusBar()
 
        self.show()
        
    def test_browser(self):
        try:           
            wst = Wst()
            wst.popuniKladionicu()
        except:
            print("Unexpected error:", sys.exc_info()[0])     
            
            
class MainWindow(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initUI()
        
 
    def initUI(self):
        self.createGridLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        
    def createGridLayout(self):      
        self.horizontalGroupBox = QGroupBox("")
        
        self.title = QLabel('Title')
        self.urlLabel = QLabel('URL')
        self.resLabel = QLabel('Response')
        self.titleEdit = QLineEdit()
        self.urlEdit = QLineEdit()
        self.urlEdit.setText("http://api.football-data.org/v1/competitions/467/teams") 
        self.responseEdit = QTextEdit()  
        self.getButton = QPushButton("GET") 
        self.getButton.clicked.connect(self.get_clicked)
        self.cancelButton = QPushButton("Cancel")         
                
        
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)

        grid.addWidget(self.urlLabel, 2, 0)
        grid.addWidget(self.urlEdit, 2, 1)

        grid.addWidget(self.resLabel, 3, 0)
        grid.addWidget(self.responseEdit, 3, 1, 5, 1)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.getButton)
        hbox.addWidget(self.cancelButton)
        
        grid.addLayout(hbox, 9, 1) 

        self.horizontalGroupBox.setLayout(grid)
        
        self.show()
    
    #call and get response from web service    
    def get_clicked(self):
        try:           
            self.responseEdit.setText("")
            wst = Wst()
            response = wst.call_ws(self.urlEdit.text())
            self.responseEdit.append(response)
        except:
            print("Unexpected error:", sys.exc_info()[0])
                     
       
        
#application entry point 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())