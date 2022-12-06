# Main Script for Final

# import statements
import json
import os
from maya import OpenMayaUI as omui
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.cmds

# import rig.py script
import rig

# Get a reference to the main Maya application window
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget) 

class MyMayaWidget(QWidget):    
    def __init__(self, *args, **kwargs):        
        super(MyMayaWidget, self).__init__(*args, **kwargs)
        
        # Parent widget under Maya main window        
        self.setParent(mayaMainWindow)        
        self.setWindowFlags(Qt.Window)   
        
        # Set the UI display title and size    
        self.setWindowTitle('Procedural Rig Creation Tool')        
        self.setGeometry(50, 50, 750, 150)

        # set up a horizontal layout for the buttons
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Create button1 and add to the layout
        self.button1 = QPushButton('Create Simple Rig', self)
        layout.addWidget(self.button1)

        # When button1 is clicked, connect a signal to run the proper function 
        self.button1.clicked.connect(self.button1_onClicked)   

        # Create button2 and add to the layout
        self.button2 = QPushButton('Reference Model Version', self)
        layout.addWidget(self.button2)

        # When the button is clicked, connect a signal to run the proper function
        self.button2.clicked.connect(self.button2_onClicked)  

        # Create text editors and add to the layout
        self.artistName = QLineEdit('Artist Name', self)
        self.versionNumber = QLineEdit('Version Number', self)
        layout.addWidget(self.artistName)
        layout.addWidget(self.versionNumber)

        # Create drop box and add to the layout
        self.fileExt = QComboBox()
        self.fileExt.addItems(['fbx','obj','mb','ma'])
        layout.addWidget(self.fileExt)
     
    # create a function to define what button1 does when clicked
    def button1_onClicked(self):
        modelPath = maya.cmds.ls(sl=True,l=True)
        rig.createJoints(modelPath)

    # create a function to define what button2 does when clicked
    def button2_onClicked(self):
        asset_info = {"project": os.getenv('project'),
                      "asset": os.getenv('asset'),
                      "task": os.getenv('task'),
                      "artist": self.artistName.toPlainText(),  # usually built-in
                      "version": self.versionNumber.toPlainText(),
                      "ext": self.fileExt.currentText()
                      }

        naming = rig.getNamingFile()['namingConvention']
        fileName = naming.format(**asset_info)
        filePath = maya.cmds.file(q=True, sn=True)
        assetFile = os.path.join(os.path.dirname(filePath), fileName)
        files = maya.cmds.getFileList(folder=os.path.dirname(filePath), filespec=fileName)
        if len(files) == 0:
            maya.cmds.warning("No file found")
        maya.cmds.file(os.path.dirname(filePath)+fileName, i=True)

# initialize button and make it visible
my_widget = MyMayaWidget()     
my_widget.show()