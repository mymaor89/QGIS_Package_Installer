import os
from qgis.core import QgsProject
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QMessageBox, QAction, QFileDialog
from .dialog import Dialog

class MainPlugin:
    def __init__(self, iface):
        """Initialize class"""
        self.canvas = iface.mapCanvas()
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)

    def initGui(self):
        """Initialize graphic user interface"""
        self.action = QAction(
            QIcon("%s/icon.png" % self.plugin_dir),
            "Install python package",
            self.iface.mainWindow()
        )

        # Initialize plugin menu:
        self.iface.addPluginToMenu("Python package installer", self.action)

        # Initialize tool bar:
        self.iface.addToolBarIcon(self.action)
        self.action.triggered.connect(self.run)

        # Initialize dialog:
        self.dialog = Dialog('ui.ui')
        

    def unload(self):
        """Actions to run when the plugin is unloaded"""
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("Python package installer", self.action)


    def run(self):
        """Action to run"""
        self.dialog.lineEdit.clear()
        self.dialog.show()
       
        def install(package):
                os.system('start cmd /D /C "pip install %s"'%package)
                QMessageBox.information(self.canvas, "Success!", "%s is now installed!" %package )
            
        result = self.dialog.exec_()
        if result == 1: # Pressed Ok
            package = self.dialog.lineEdit.text()
            if package:
                install(package)
            else:
                QMessageBox.critical(self.canvas, "Error", "Missing package name")
           
                
