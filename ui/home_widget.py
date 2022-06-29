# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home-widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(727, 446)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.itemSearchbar = QtWidgets.QLineEdit(self.frame_5)
        self.itemSearchbar.setObjectName("itemSearchbar")
        self.horizontalLayout_2.addWidget(self.itemSearchbar)
        self.verticalLayout.addWidget(self.frame_5)
        self.itemList = QtWidgets.QListWidget(self.frame)
        self.itemList.setAlternatingRowColors(True)
        self.itemList.setObjectName("itemList")
        self.verticalLayout.addWidget(self.itemList)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 62))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.itemImage = QtWidgets.QLabel(self.frame_7)
        self.itemImage.setText("")
        self.itemImage.setPixmap(QtGui.QPixmap("../images/unknown-item-icon.jpg"))
        self.itemImage.setObjectName("itemImage")
        self.horizontalLayout_4.addWidget(self.itemImage)
        self.itemName = QtWidgets.QTextBrowser(self.frame_7)
        self.itemName.setMaximumSize(QtCore.QSize(16777215, 62))
        self.itemName.setObjectName("itemName")
        self.horizontalLayout_4.addWidget(self.itemName)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.itemOwnedFIR = QtWidgets.QSpinBox(self.frame_3)
        self.itemOwnedFIR.setProperty("showGroupSeparator", True)
        self.itemOwnedFIR.setMaximum(999999999)
        self.itemOwnedFIR.setObjectName("itemOwnedFIR")
        self.gridLayout.addWidget(self.itemOwnedFIR, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.itemNeedNFIR = QtWidgets.QSpinBox(self.frame_3)
        self.itemNeedNFIR.setReadOnly(True)
        self.itemNeedNFIR.setProperty("showGroupSeparator", True)
        self.itemNeedNFIR.setMaximum(999999999)
        self.itemNeedNFIR.setObjectName("itemNeedNFIR")
        self.gridLayout.addWidget(self.itemNeedNFIR, 2, 2, 1, 1)
        self.itemNeedFIR = QtWidgets.QSpinBox(self.frame_3)
        self.itemNeedFIR.setReadOnly(True)
        self.itemNeedFIR.setProperty("showGroupSeparator", True)
        self.itemNeedFIR.setMaximum(999999999)
        self.itemNeedFIR.setObjectName("itemNeedFIR")
        self.gridLayout.addWidget(self.itemNeedFIR, 2, 1, 1, 1)
        self.itemTaskFIR = QtWidgets.QSpinBox(self.frame_3)
        self.itemTaskFIR.setReadOnly(True)
        self.itemTaskFIR.setProperty("showGroupSeparator", True)
        self.itemTaskFIR.setMaximum(999999999)
        self.itemTaskFIR.setObjectName("itemTaskFIR")
        self.gridLayout.addWidget(self.itemTaskFIR, 4, 1, 1, 1)
        self.itemOwnedNFIR = QtWidgets.QSpinBox(self.frame_3)
        self.itemOwnedNFIR.setProperty("showGroupSeparator", True)
        self.itemOwnedNFIR.setMaximum(999999999)
        self.itemOwnedNFIR.setObjectName("itemOwnedNFIR")
        self.gridLayout.addWidget(self.itemOwnedNFIR, 5, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.itemTaskNFIR = QtWidgets.QSpinBox(self.frame_3)
        self.itemTaskNFIR.setReadOnly(True)
        self.itemTaskNFIR.setProperty("showGroupSeparator", True)
        self.itemTaskNFIR.setMaximum(999999999)
        self.itemTaskNFIR.setObjectName("itemTaskNFIR")
        self.gridLayout.addWidget(self.itemTaskNFIR, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.itemSubmitButton = QtWidgets.QPushButton(self.frame)
        self.itemSubmitButton.setObjectName("itemSubmitButton")
        self.verticalLayout.addWidget(self.itemSubmitButton)
        self.horizontalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.taskSearchbar = QtWidgets.QLineEdit(self.frame_6)
        self.taskSearchbar.setObjectName("taskSearchbar")
        self.horizontalLayout_3.addWidget(self.taskSearchbar)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.taskTable = QtWidgets.QTableWidget(self.frame_2)
        self.taskTable.setAlternatingRowColors(True)
        self.taskTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.taskTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.taskTable.setObjectName("taskTable")
        self.taskTable.setColumnCount(4)
        self.taskTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.taskTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.taskTable)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.taskName = QtWidgets.QLineEdit(self.frame_4)
        self.taskName.setReadOnly(True)
        self.taskName.setObjectName("taskName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.taskName)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.taskGiver = QtWidgets.QLineEdit(self.frame_4)
        self.taskGiver.setReadOnly(True)
        self.taskGiver.setObjectName("taskGiver")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.taskGiver)
        self.taskCompleted = QtWidgets.QCheckBox(self.frame_4)
        self.taskCompleted.setText("")
        self.taskCompleted.setObjectName("taskCompleted")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.taskCompleted)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.taskSubmitButton = QtWidgets.QPushButton(self.frame_2)
        self.taskSubmitButton.setObjectName("taskSubmitButton")
        self.verticalLayout_2.addWidget(self.taskSubmitButton)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Item"))
        self.label_12.setText(_translate("Form", "Search"))
        self.label_7.setText(_translate("Form", "Not Found In Raid"))
        self.label_5.setText(_translate("Form", "Task Qty"))
        self.label_4.setText(_translate("Form", "Need Qty"))
        self.label_8.setText(_translate("Form", "Owned Qty"))
        self.label_6.setText(_translate("Form", "Found In Raid"))
        self.itemSubmitButton.setText(_translate("Form", "Submit"))
        self.label_2.setText(_translate("Form", "Task"))
        self.label_13.setText(_translate("Form", "Search"))
        self.taskTable.setSortingEnabled(True)
        item = self.taskTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.taskTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.taskTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Trader"))
        item = self.taskTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Completed?"))
        self.label_9.setText(_translate("Form", "Task Name"))
        self.label_10.setText(_translate("Form", "Task Giver"))
        self.label_11.setText(_translate("Form", "Completed"))
        self.taskSubmitButton.setText(_translate("Form", "Submit"))
