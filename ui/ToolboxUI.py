# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolbox.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SegmentationToolbox(object):
    def setupUi(self, SegmentationToolbox):
        SegmentationToolbox.setObjectName("SegmentationToolbox")
        SegmentationToolbox.resize(311, 1048)
        self.centralwidget = QtWidgets.QWidget(SegmentationToolbox)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splashWidget = QtWidgets.QWidget(self.centralwidget)
        self.splashWidget.setObjectName("splashWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.splashWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splash_label = QtWidgets.QLabel(self.splashWidget)
        self.splash_label.setText("")
        self.splash_label.setAlignment(QtCore.Qt.AlignCenter)
        self.splash_label.setObjectName("splash_label")
        self.verticalLayout_8.addWidget(self.splash_label)
        self.splash_progressbar = QtWidgets.QProgressBar(self.splashWidget)
        self.splash_progressbar.setProperty("value", 24)
        self.splash_progressbar.setObjectName("splash_progressbar")
        self.verticalLayout_8.addWidget(self.splash_progressbar)
        self.splash_text_label = QtWidgets.QLabel(self.splashWidget)
        self.splash_text_label.setText("")
        self.splash_text_label.setObjectName("splash_text_label")
        self.verticalLayout_8.addWidget(self.splash_text_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.verticalLayout.addWidget(self.splashWidget)
        self.mainUIWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainUIWidget.setObjectName("mainUIWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainUIWidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.classification_combo = QtWidgets.QComboBox(self.mainUIWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.classification_combo.sizePolicy().hasHeightForWidth())
        self.classification_combo.setSizePolicy(sizePolicy)
        self.classification_combo.setObjectName("classification_combo")
        self.horizontalLayout_11.addWidget(self.classification_combo)
        self.classification_all_button = QtWidgets.QToolButton(self.mainUIWidget)
        self.classification_all_button.setObjectName("classification_all_button")
        self.horizontalLayout_11.addWidget(self.classification_all_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.history_group = QtWidgets.QGroupBox(self.mainUIWidget)
        self.history_group.setObjectName("history_group")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.history_group)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.undoButton = QtWidgets.QPushButton(self.history_group)
        self.undoButton.setEnabled(False)
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout_3.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QPushButton(self.history_group)
        self.redoButton.setEnabled(False)
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout_3.addWidget(self.redoButton)
        self.verticalLayout_9.addWidget(self.history_group)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.mainUIWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.editmode_combo = QtWidgets.QComboBox(self.mainUIWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editmode_combo.sizePolicy().hasHeightForWidth())
        self.editmode_combo.setSizePolicy(sizePolicy)
        self.editmode_combo.setObjectName("editmode_combo")
        self.editmode_combo.addItem("")
        self.editmode_combo.addItem("")
        self.horizontalLayout_6.addWidget(self.editmode_combo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.ROI_group = QtWidgets.QGroupBox(self.mainUIWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROI_group.sizePolicy().hasHeightForWidth())
        self.ROI_group.setSizePolicy(sizePolicy)
        self.ROI_group.setObjectName("ROI_group")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ROI_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.roi_combo = QtWidgets.QComboBox(self.ROI_group)
        self.roi_combo.setObjectName("roi_combo")
        self.horizontalLayout.addWidget(self.roi_combo)
        self.roi_add_button = QtWidgets.QToolButton(self.ROI_group)
        self.roi_add_button.setObjectName("roi_add_button")
        self.horizontalLayout.addWidget(self.roi_add_button)
        self.roi_remove_button = QtWidgets.QToolButton(self.ROI_group)
        self.roi_remove_button.setObjectName("roi_remove_button")
        self.horizontalLayout.addWidget(self.roi_remove_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.subroi_widget = QtWidgets.QWidget(self.ROI_group)
        self.subroi_widget.setObjectName("subroi_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.subroi_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.subroi_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.subroi_combo = QtWidgets.QComboBox(self.subroi_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subroi_combo.sizePolicy().hasHeightForWidth())
        self.subroi_combo.setSizePolicy(sizePolicy)
        self.subroi_combo.setObjectName("subroi_combo")
        self.horizontalLayout_2.addWidget(self.subroi_combo)
        self.subroi_add_button = QtWidgets.QToolButton(self.subroi_widget)
        self.subroi_add_button.setObjectName("subroi_add_button")
        self.horizontalLayout_2.addWidget(self.subroi_add_button)
        self.subroi_remove_button = QtWidgets.QToolButton(self.subroi_widget)
        self.subroi_remove_button.setObjectName("subroi_remove_button")
        self.horizontalLayout_2.addWidget(self.subroi_remove_button)
        self.verticalLayout_2.addWidget(self.subroi_widget)
        self.verticalLayout_9.addWidget(self.ROI_group)
        self.autosegment_button = QtWidgets.QPushButton(self.mainUIWidget)
        self.autosegment_button.setObjectName("autosegment_button")
        self.verticalLayout_9.addWidget(self.autosegment_button)
        self.edit_group = QtWidgets.QGroupBox(self.mainUIWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_group.sizePolicy().hasHeightForWidth())
        self.edit_group.setSizePolicy(sizePolicy)
        self.edit_group.setObjectName("edit_group")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.edit_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.addpaint_button = QtWidgets.QPushButton(self.edit_group)
        self.addpaint_button.setCheckable(True)
        self.addpaint_button.setChecked(False)
        self.addpaint_button.setAutoExclusive(False)
        self.addpaint_button.setObjectName("addpaint_button")
        self.horizontalLayout_8.addWidget(self.addpaint_button)
        self.removeerase_button = QtWidgets.QPushButton(self.edit_group)
        self.removeerase_button.setCheckable(True)
        self.removeerase_button.setAutoExclusive(False)
        self.removeerase_button.setObjectName("removeerase_button")
        self.horizontalLayout_8.addWidget(self.removeerase_button)
        self.removeall_button = QtWidgets.QPushButton(self.edit_group)
        self.removeall_button.setObjectName("removeall_button")
        self.horizontalLayout_8.addWidget(self.removeall_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9.addWidget(self.edit_group)
        self.brush_group = QtWidgets.QGroupBox(self.mainUIWidget)
        self.brush_group.setObjectName("brush_group")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.brush_group)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.circlebrush_button = QtWidgets.QToolButton(self.brush_group)
        self.circlebrush_button.setMinimumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.circlebrush_button.setFont(font)
        self.circlebrush_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/images/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.circlebrush_button.setIcon(icon)
        self.circlebrush_button.setCheckable(True)
        self.circlebrush_button.setChecked(True)
        self.circlebrush_button.setAutoExclusive(True)
        self.circlebrush_button.setObjectName("circlebrush_button")
        self.horizontalLayout_5.addWidget(self.circlebrush_button)
        self.squarebrush_button = QtWidgets.QToolButton(self.brush_group)
        self.squarebrush_button.setMinimumSize(QtCore.QSize(24, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/images/square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.squarebrush_button.setIcon(icon1)
        self.squarebrush_button.setCheckable(True)
        self.squarebrush_button.setAutoExclusive(True)
        self.squarebrush_button.setObjectName("squarebrush_button")
        self.horizontalLayout_5.addWidget(self.squarebrush_button)
        self.brushsize_slider = QtWidgets.QSlider(self.brush_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brushsize_slider.sizePolicy().hasHeightForWidth())
        self.brushsize_slider.setSizePolicy(sizePolicy)
        self.brushsize_slider.setMinimum(0)
        self.brushsize_slider.setMaximum(15)
        self.brushsize_slider.setSingleStep(1)
        self.brushsize_slider.setPageStep(10)
        self.brushsize_slider.setProperty("value", 5)
        self.brushsize_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brushsize_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.brushsize_slider.setObjectName("brushsize_slider")
        self.horizontalLayout_5.addWidget(self.brushsize_slider)
        self.brushsize_label = QtWidgets.QLabel(self.brush_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brushsize_label.sizePolicy().hasHeightForWidth())
        self.brushsize_label.setSizePolicy(sizePolicy)
        self.brushsize_label.setMinimumSize(QtCore.QSize(20, 0))
        self.brushsize_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.brushsize_label.setObjectName("brushsize_label")
        self.horizontalLayout_5.addWidget(self.brushsize_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addWidget(self.brush_group)
        self.maskedit_group = QtWidgets.QGroupBox(self.mainUIWidget)
        self.maskedit_group.setObjectName("maskedit_group")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.maskedit_group)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.grow_button = QtWidgets.QPushButton(self.maskedit_group)
        self.grow_button.setObjectName("grow_button")
        self.horizontalLayout_10.addWidget(self.grow_button)
        self.shrink_button = QtWidgets.QPushButton(self.maskedit_group)
        self.shrink_button.setObjectName("shrink_button")
        self.horizontalLayout_10.addWidget(self.shrink_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9.addWidget(self.maskedit_group)
        self.contouredit_widget = QtWidgets.QGroupBox(self.mainUIWidget)
        self.contouredit_widget.setObjectName("contouredit_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.contouredit_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.translateContour_button = QtWidgets.QPushButton(self.contouredit_widget)
        self.translateContour_button.setCheckable(True)
        self.translateContour_button.setObjectName("translateContour_button")
        self.horizontalLayout_7.addWidget(self.translateContour_button)
        self.rotateContour_button = QtWidgets.QPushButton(self.contouredit_widget)
        self.rotateContour_button.setCheckable(True)
        self.rotateContour_button.setObjectName("rotateContour_button")
        self.horizontalLayout_7.addWidget(self.rotateContour_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.optimizeButton = QtWidgets.QPushButton(self.contouredit_widget)
        self.optimizeButton.setObjectName("optimizeButton")
        self.horizontalLayout_9.addWidget(self.optimizeButton)
        self.simplifyButton = QtWidgets.QPushButton(self.contouredit_widget)
        self.simplifyButton.setObjectName("simplifyButton")
        self.horizontalLayout_9.addWidget(self.simplifyButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addWidget(self.contouredit_widget)
        self.registrationGroup = QtWidgets.QGroupBox(self.mainUIWidget)
        self.registrationGroup.setObjectName("registrationGroup")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.registrationGroup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.propagateBackButton = QtWidgets.QPushButton(self.registrationGroup)
        self.propagateBackButton.setObjectName("propagateBackButton")
        self.horizontalLayout_4.addWidget(self.propagateBackButton)
        self.propagateForwardButton = QtWidgets.QPushButton(self.registrationGroup)
        self.propagateForwardButton.setObjectName("propagateForwardButton")
        self.horizontalLayout_4.addWidget(self.propagateForwardButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.calcTransformsButton = QtWidgets.QPushButton(self.registrationGroup)
        self.calcTransformsButton.setObjectName("calcTransformsButton")
        self.verticalLayout_5.addWidget(self.calcTransformsButton)
        self.verticalLayout_9.addWidget(self.registrationGroup)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.mainUIWidget)
        SegmentationToolbox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SegmentationToolbox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave_masks = QtWidgets.QMenu(self.menuFile)
        self.menuSave_masks.setObjectName("menuSave_masks")
        self.menuSave_as_Numpy = QtWidgets.QMenu(self.menuSave_masks)
        self.menuSave_as_Numpy.setObjectName("menuSave_as_Numpy")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuROI = QtWidgets.QMenu(self.menubar)
        self.menuROI.setObjectName("menuROI")
        SegmentationToolbox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SegmentationToolbox)
        self.statusbar.setObjectName("statusbar")
        SegmentationToolbox.setStatusBar(self.statusbar)
        self.actionImport_ROIs = QtWidgets.QAction(SegmentationToolbox)
        self.actionImport_ROIs.setObjectName("actionImport_ROIs")
        self.actionExport_ROIs = QtWidgets.QAction(SegmentationToolbox)
        self.actionExport_ROIs.setObjectName("actionExport_ROIs")
        self.actionImport_masks = QtWidgets.QAction(SegmentationToolbox)
        self.actionImport_masks.setObjectName("actionImport_masks")
        self.actionSave_as_Dicom = QtWidgets.QAction(SegmentationToolbox)
        self.actionSave_as_Dicom.setObjectName("actionSave_as_Dicom")
        self.actionSave_as_Nifti = QtWidgets.QAction(SegmentationToolbox)
        self.actionSave_as_Nifti.setObjectName("actionSave_as_Nifti")
        self.actionLoad_data = QtWidgets.QAction(SegmentationToolbox)
        self.actionLoad_data.setObjectName("actionLoad_data")
        self.actionSaveNPZ = QtWidgets.QAction(SegmentationToolbox)
        self.actionSaveNPZ.setObjectName("actionSaveNPZ")
        self.actionSaveNPY = QtWidgets.QAction(SegmentationToolbox)
        self.actionSaveNPY.setObjectName("actionSaveNPY")
        self.actionCalculate_statistics = QtWidgets.QAction(SegmentationToolbox)
        self.actionCalculate_statistics.setObjectName("actionCalculate_statistics")
        self.actionAbout = QtWidgets.QAction(SegmentationToolbox)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPyRadiomics = QtWidgets.QAction(SegmentationToolbox)
        self.actionPyRadiomics.setObjectName("actionPyRadiomics")
        self.actionPreferences = QtWidgets.QAction(SegmentationToolbox)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionCopy_roi = QtWidgets.QAction(SegmentationToolbox)
        self.actionCopy_roi.setObjectName("actionCopy_roi")
        self.actionCombine_roi = QtWidgets.QAction(SegmentationToolbox)
        self.actionCombine_roi.setObjectName("actionCombine_roi")
        self.action_Upload_data = QtWidgets.QAction(SegmentationToolbox)
        self.action_Upload_data.setObjectName("action_Upload_data")
        self.actionImport_model = QtWidgets.QAction(SegmentationToolbox)
        self.actionImport_model.setObjectName("actionImport_model")
        self.menuSave_as_Numpy.addAction(self.actionSaveNPZ)
        self.menuSave_as_Numpy.addAction(self.actionSaveNPY)
        self.menuSave_masks.addAction(self.menuSave_as_Numpy.menuAction())
        self.menuSave_masks.addAction(self.actionSave_as_Dicom)
        self.menuSave_masks.addAction(self.actionSave_as_Nifti)
        self.menuFile.addAction(self.actionLoad_data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_ROIs)
        self.menuFile.addAction(self.actionExport_ROIs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_masks)
        self.menuFile.addAction(self.menuSave_masks.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_model)
        self.menuFile.addAction(self.action_Upload_data)
        self.menuTools.addAction(self.actionCalculate_statistics)
        self.menuTools.addAction(self.actionPyRadiomics)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuROI.addAction(self.actionCopy_roi)
        self.menuROI.addAction(self.actionCombine_roi)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuROI.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(SegmentationToolbox)
        QtCore.QMetaObject.connectSlotsByName(SegmentationToolbox)

    def retranslateUi(self, SegmentationToolbox):
        _translate = QtCore.QCoreApplication.translate
        SegmentationToolbox.setWindowTitle(_translate("SegmentationToolbox", "MainWindow"))
        self.classification_all_button.setText(_translate("SegmentationToolbox", "All"))
        self.history_group.setTitle(_translate("SegmentationToolbox", "History"))
        self.undoButton.setText(_translate("SegmentationToolbox", "Undo"))
        self.redoButton.setText(_translate("SegmentationToolbox", "Redo"))
        self.label_2.setText(_translate("SegmentationToolbox", "Edit:"))
        self.editmode_combo.setItemText(0, _translate("SegmentationToolbox", "Mask"))
        self.editmode_combo.setItemText(1, _translate("SegmentationToolbox", "Contour"))
        self.ROI_group.setTitle(_translate("SegmentationToolbox", "ROI"))
        self.roi_add_button.setText(_translate("SegmentationToolbox", "+"))
        self.roi_remove_button.setText(_translate("SegmentationToolbox", "-"))
        self.label.setText(_translate("SegmentationToolbox", " ⮡"))
        self.subroi_add_button.setText(_translate("SegmentationToolbox", "+"))
        self.subroi_remove_button.setText(_translate("SegmentationToolbox", "-"))
        self.autosegment_button.setText(_translate("SegmentationToolbox", "AutoSegment"))
        self.edit_group.setTitle(_translate("SegmentationToolbox", "Edit"))
        self.addpaint_button.setText(_translate("SegmentationToolbox", "Add/Move"))
        self.removeerase_button.setText(_translate("SegmentationToolbox", "Remove"))
        self.removeall_button.setText(_translate("SegmentationToolbox", "Clear"))
        self.brush_group.setTitle(_translate("SegmentationToolbox", "Brush"))
        self.brushsize_label.setText(_translate("SegmentationToolbox", "11"))
        self.maskedit_group.setTitle(_translate("SegmentationToolbox", "Mask"))
        self.grow_button.setText(_translate("SegmentationToolbox", "Grow"))
        self.shrink_button.setText(_translate("SegmentationToolbox", "Shrink"))
        self.contouredit_widget.setTitle(_translate("SegmentationToolbox", "Contour"))
        self.translateContour_button.setText(_translate("SegmentationToolbox", "Translate"))
        self.rotateContour_button.setText(_translate("SegmentationToolbox", "Rotate"))
        self.optimizeButton.setText(_translate("SegmentationToolbox", "Snap to edges"))
        self.simplifyButton.setText(_translate("SegmentationToolbox", "Simplify"))
        self.registrationGroup.setTitle(_translate("SegmentationToolbox", "Registration"))
        self.propagateBackButton.setText(_translate("SegmentationToolbox", "Propagate back"))
        self.propagateForwardButton.setText(_translate("SegmentationToolbox", "Propagate forward"))
        self.calcTransformsButton.setText(_translate("SegmentationToolbox", "Calculate transforms"))
        self.menuFile.setTitle(_translate("SegmentationToolbox", "File"))
        self.menuSave_masks.setTitle(_translate("SegmentationToolbox", "Save masks..."))
        self.menuSave_as_Numpy.setTitle(_translate("SegmentationToolbox", "Save as Numpy..."))
        self.menuTools.setTitle(_translate("SegmentationToolbox", "Tools"))
        self.menuHelp.setTitle(_translate("SegmentationToolbox", "Help"))
        self.menuROI.setTitle(_translate("SegmentationToolbox", "ROI"))
        self.actionImport_ROIs.setText(_translate("SegmentationToolbox", "Import ROI file..."))
        self.actionExport_ROIs.setText(_translate("SegmentationToolbox", "Export ROI file..."))
        self.actionImport_masks.setText(_translate("SegmentationToolbox", "Import masks..."))
        self.actionSave_as_Dicom.setText(_translate("SegmentationToolbox", "Save as Dicom..."))
        self.actionSave_as_Nifti.setText(_translate("SegmentationToolbox", "Save as Nifti..."))
        self.actionLoad_data.setText(_translate("SegmentationToolbox", "Load data..."))
        self.actionSaveNPZ.setText(_translate("SegmentationToolbox", "Single file"))
        self.actionSaveNPY.setText(_translate("SegmentationToolbox", "Multiple files"))
        self.actionCalculate_statistics.setText(_translate("SegmentationToolbox", "Calculate statistics..."))
        self.actionAbout.setText(_translate("SegmentationToolbox", "About..."))
        self.actionPyRadiomics.setText(_translate("SegmentationToolbox", "PyRadiomics..."))
        self.actionPreferences.setText(_translate("SegmentationToolbox", "Preferences..."))
        self.actionCopy_roi.setText(_translate("SegmentationToolbox", "Copy/Rename..."))
        self.actionCombine_roi.setText(_translate("SegmentationToolbox", "Combine..."))
        self.action_Upload_data.setText(_translate("SegmentationToolbox", "! Upload data..."))
        self.actionImport_model.setText(_translate("SegmentationToolbox", "Import model..."))
