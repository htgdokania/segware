import sys
from PyQt5 import QtWidgets

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, QRect, Qt

App = QApplication(sys.argv)
screen = App.primaryScreen()
size = screen.size()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_widget = window(parent=self)
        self.setGeometry(0,0,size.width(), size.height()/2)#top,left,width,height

        self.setCentralWidget(self.window_widget)
        # filling up a menu bar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        helpMenu = mainMenu.addMenu("Help")
        
        openButton = QAction(QIcon("Images/open.png"), 'Open', self)
        openButton.setShortcut("Ctrl+O")
        openButton.setStatusTip("Open MRI (.nii, .nii.gz, .mha)")
        openButton.triggered.connect(self.OpenMRI)
        fileMenu.addAction(openButton)
        
        openLastButton = QAction(QIcon("Images/open.png"), 'Open last closed', self)
        openLastButton.setShortcut("Ctrl+Shift+T")
        openLastButton.setStatusTip("Open last closed MRI (.nii, .nii.gz, .mha)")
        openLastButton.triggered.connect(self.OpenLastMRI)
        fileMenu.addAction(openLastButton)
        
        openRecentButton = QAction(QIcon("Images/open.png"), 'Open recent', self)
        openRecentButton.setStatusTip("Open recently closed MRI (.nii, .nii.gz, .mha)")
        openRecentButton.triggered.connect(self.OpenRecentMRI)
        fileMenu.addAction(openRecentButton)
        
        saveSegButton = QAction(QIcon("Images/saveSegmentedMRI.png"), 'Save segmented MRI', self)
        saveSegButton.setShortcut('Ctrl+S')
        saveSegButton.setStatusTip('Save segmented MRIs')
        saveSegButton.triggered.connect(self.SaveSegmentedMRI)
        fileMenu.addAction(saveSegButton)
        
        saveMaskButton = QAction(QIcon("Images/saveMask.png"), 'Save mask', self)
        saveMaskButton.setShortcut('Ctrl+Shift+M')
        saveMaskButton.setStatusTip('Save Mask of segmented MRIs')
        saveMaskButton.triggered.connect(self.SaveMask)
        fileMenu.addAction(saveMaskButton)

        exitButton = QAction(QIcon("Images/close.png"), 'Exit',self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip("Exit Application")
        exitButton.triggered.connect(self.CloseApp)
        fileMenu.addAction(exitButton)
        
        aboutButton = QAction(QIcon("Images/about.png"), 'About',self)
        aboutButton.setShortcut("Ctrl+A")
        aboutButton.setStatusTip("About software")
        aboutButton.triggered.connect(self.AboutSoftware)
        helpMenu.addAction(aboutButton)
        
        tutorialButton = QAction(QIcon("Images/tutorial.png"), 'Tutorial',self)
        tutorialButton.setStatusTip("Demo Tutorial")
        tutorialButton.triggered.connect(self.AboutSoftware)
        helpMenu.addAction(tutorialButton)

    def CloseApp(self):
        reply = QMessageBox.question(self, "Close Message", "Are You Sure To Close Window",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            
    def OpenMRI(self):
        print("In open")
        
    def OpenLastMRI(self):
        print("In open last MRI")
        
    def OpenRecentMRI(self):
        print("In open recent MRI")

    def SaveMask(self):
        print("In save mask")
        
    def AboutSoftware(self):
        print("In AboutSoftware")    
        
    def SaveSegmentedMRI(self):
        print("In SaveSegmentedMRI")   

# part for adding buttons in layouts
class window(QScrollArea):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.container = QFrame(self)
        
        self.container.resize(size.width(),size.height()/2)

        self.title="PyQt5 layout"
        self.setWindowTitle(self.title)
        self.setGeometry(0,0,size.width(), size.height()/2)#top,left,width,height

        hBox=QHBoxLayout(self.container)
        self.groupbox1 =QGroupBox("part 1")
        self.groupbox2 =QGroupBox("part 2")
        self.groupbox3 =QGroupBox("part 3")
        self.groupbox4 =QGroupBox("part 4")
        
        self.vBoxLayout =QVBoxLayout(self.container)
        self.vBoxLayout2 =QVBoxLayout(self.container)
        self.vBoxLayout3 =QVBoxLayout(self.container)
        self.vBoxLayout4 =QVBoxLayout(self.container)
        
        hBoxLayout=QHBoxLayout()

        #add buttons for part 1
        button1=QPushButton("T1",self)
        self.vBoxLayout.addWidget(button1)

        button2=QPushButton("T2",self)
        self.vBoxLayout.addWidget(button2)
        
        button3=QPushButton("TC",self)
        self.vBoxLayout.addWidget(button3)

        button4=QPushButton("F",self)
        self.vBoxLayout.addWidget(button4)

        button5=QPushButton("SEGMENT",self)
        self.vBoxLayout.addWidget(button5)
        button5.clicked.connect(self.func)

        button=QPushButton("CLOSE",self)                
        self.vBoxLayout.addWidget(button)
        button.clicked.connect(self.CloseApp)
    
        #add buttonfor part 2        
        button=QPushButton("A",self)
        self.vBoxLayout2.addWidget(button)

        #add for part 3
        button=QPushButton("1",self)
        self.vBoxLayout3.addWidget(button)

        #add for part 4
        
        button=QPushButton("c",self)
        self.vBoxLayout4.addWidget(button)


        #set layout position
        self.groupbox1.setLayout(self.vBoxLayout)
        hBox.addWidget(self.groupbox1)
        self.groupbox2.setLayout(self.vBoxLayout2)
        hBox.addWidget(self.groupbox2)
        self.groupbox3.setLayout(self.vBoxLayout3)
        self.groupbox4.setLayout(self.vBoxLayout4)
                
        self.setWidget(self.container)
        self.show()

    def func(self):
        self.container.resize(size.width(),size.height())
        self.vBoxLayout.addWidget(self.groupbox3)
        self.vBoxLayout2.addWidget(self.groupbox4)
    def CloseApp(self):
        reply = QMessageBox.question(self, "Close Message", "Are You Sure To Close Window",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
    
#"""
    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # creating main window
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())