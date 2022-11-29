####################

# HI!! Its Adrianna!!
# Im just starting by pasting my last assignment and making tweaks

#####################


# import statements
from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.cmds

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
        self.setGeometry(50, 50, 250, 150)
        
        # Create a new button
        self.my_button = QPushButton('Create Simple Rig', self)

        # When the button is clicked, connect a signal to run the function below
        self.my_button.clicked.connect(self.button_onClicked)   
         
    # create a function to define what the button does when clicked
    def button_onClicked(self):
        # WRITE CODE HERE!
        # use locators to create bones
        

# initialize button and make it visible
my_widget = MyMayaWidget()     
my_widget.show()