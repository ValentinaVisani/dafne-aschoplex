# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ValidateUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ValidateUI(object):
    def setupUi(self, ValidateUI):
        ValidateUI.setObjectName("ValidateUI")
        ValidateUI.resize(724, 348)
        self.verticalLayout = QtWidgets.QVBoxLayout(ValidateUI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ValidateUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.data_location_Text = QtWidgets.QLineEdit(ValidateUI)
        self.data_location_Text.setEnabled(False)
        self.data_location_Text.setObjectName("data_location_Text")
        self.horizontalLayout.addWidget(self.data_location_Text)
        self.data_choose_Button = QtWidgets.QPushButton(ValidateUI)
        self.data_choose_Button.setObjectName("data_choose_Button")
        self.horizontalLayout.addWidget(self.data_choose_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(ValidateUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mask_location_Text = QtWidgets.QLineEdit(ValidateUI)
        self.mask_location_Text.setEnabled(False)
        self.mask_location_Text.setObjectName("mask_location_Text")
        self.horizontalLayout_2.addWidget(self.mask_location_Text)
        self.mask_choose_Button = QtWidgets.QPushButton(ValidateUI)
        self.mask_choose_Button.setEnabled(False)
        self.mask_choose_Button.setObjectName("mask_choose_Button")
        self.horizontalLayout_2.addWidget(self.mask_choose_Button)
        self.roi_choose_Button = QtWidgets.QPushButton(ValidateUI)
        self.roi_choose_Button.setEnabled(False)
        self.roi_choose_Button.setObjectName("roi_choose_Button")
        self.horizontalLayout_2.addWidget(self.roi_choose_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.currentProgress_Label = QtWidgets.QLabel(ValidateUI)
        self.currentProgress_Label.setObjectName("currentProgress_Label")
        self.horizontalLayout_3.addWidget(self.currentProgress_Label)
        self.slice_progressBar = QtWidgets.QProgressBar(ValidateUI)
        self.slice_progressBar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slice_progressBar.sizePolicy().hasHeightForWidth())
        self.slice_progressBar.setSizePolicy(sizePolicy)
        self.slice_progressBar.setProperty("value", 0)
        self.slice_progressBar.setObjectName("slice_progressBar")
        self.horizontalLayout_3.addWidget(self.slice_progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(ValidateUI)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.overall_progressBar = QtWidgets.QProgressBar(ValidateUI)
        self.overall_progressBar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overall_progressBar.sizePolicy().hasHeightForWidth())
        self.overall_progressBar.setSizePolicy(sizePolicy)
        self.overall_progressBar.setProperty("value", 0)
        self.overall_progressBar.setObjectName("overall_progressBar")
        self.horizontalLayout_4.addWidget(self.overall_progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.status_Label = QtWidgets.QLabel(ValidateUI)
        self.status_Label.setText("")
        self.status_Label.setObjectName("status_Label")
        self.verticalLayout.addWidget(self.status_Label)
        spacerItem = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.evaluate_Button = QtWidgets.QPushButton(ValidateUI)
        self.evaluate_Button.setEnabled(False)
        self.evaluate_Button.setObjectName("evaluate_Button")
        self.verticalLayout.addWidget(self.evaluate_Button)

        self.retranslateUi(ValidateUI)
        QtCore.QMetaObject.connectSlotsByName(ValidateUI)

    def retranslateUi(self, ValidateUI):
        _translate = QtCore.QCoreApplication.translate
        ValidateUI.setWindowTitle(_translate("ValidateUI", "Form"))
        self.label.setText(_translate("ValidateUI", "Data Location:"))
        self.data_choose_Button.setText(_translate("ValidateUI", "Choose..."))
        self.label_2.setText(_translate("ValidateUI", "Masks Location:"))
        self.mask_choose_Button.setText(_translate("ValidateUI", "Choose folder..."))
        self.roi_choose_Button.setText(_translate("ValidateUI", "Choose ROI..."))
        self.currentProgress_Label.setText(_translate("ValidateUI", "Current eval:"))
        self.label_4.setText(_translate("ValidateUI", "Overall progress:"))
        self.evaluate_Button.setText(_translate("ValidateUI", "Evaluate"))
