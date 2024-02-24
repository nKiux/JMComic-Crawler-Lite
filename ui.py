import os
import time

try:
    import jmcomic
    from PyQt5 import QtCore, QtGui, QtWidgets
    import JMCCL
except:
    os.system('python -m pip install pyqt5')
os.system('python -m pip install jmcomic -i https://pypi.org/project --upgrade')
global _translate
_translate = QtCore.QCoreApplication.translate

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 123)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Dialog.setMouseTracking(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 75, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 371, 41))
        self.lineEdit.setObjectName("input")
        #self.lineEdit.textChanged.connect(self.setnum)
        self.retranslateUi(Dialog)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 80, 211, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.buttonBox.accepted.connect(self.ok_clicked) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        
        Dialog.setWindowTitle(_translate("Dialog", "JMCCL"))
        self.lineEdit.setText(_translate("Dialog", "請輸入本子號碼 (數字)"))
    
    def ok_clicked(self):
        try:
            num = self.lineEdit.text()
            self.lineEdit.setText(_translate("Dialog", "正在等待回傳並下載..."))
            self.progressBar.setProperty("value", 60)
            JMCCL.dld(number = num)
            self.progressBar.setProperty("value", 100)
            self.lineEdit.setText(_translate("Dialog", f"{JMCCL.status}"))
        except:
            print(f'ran into failure, num = {num}')

while True:
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        #Ui_Dialog.buttonBox.Cancel.connect()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
