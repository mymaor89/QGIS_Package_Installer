import os
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog


def Dialog(uiFileName):
    uiFile, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), uiFileName))
    class DialogClass(QDialog, uiFile):
        def __init__(self, parent = None):
            super(DialogClass, self).__init__(parent)
            self.setupUi(self)
    return DialogClass()
