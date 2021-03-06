# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'python/plugins/processing/algs/ui/DlgFieldsCalculator.ui'
#
# Created: Thu Oct 24 16:06:48 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FieldsCalculator(object):
    def setupUi(self, FieldsCalculator):
        FieldsCalculator.setObjectName(_fromUtf8("FieldsCalculator"))
        FieldsCalculator.resize(681, 681)
        self.gridLayout = QtGui.QGridLayout(FieldsCalculator)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mNewFieldGroupBox = QtGui.QGroupBox(FieldsCalculator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mNewFieldGroupBox.sizePolicy().hasHeightForWidth())
        self.mNewFieldGroupBox.setSizePolicy(sizePolicy)
        self.mNewFieldGroupBox.setFlat(True)
        self.mNewFieldGroupBox.setCheckable(True)
        self.mNewFieldGroupBox.setChecked(True)
        self.mNewFieldGroupBox.setObjectName(_fromUtf8("mNewFieldGroupBox"))
        self.gridlayout = QtGui.QGridLayout(self.mNewFieldGroupBox)
        self.gridlayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridlayout.setContentsMargins(3, 3, 3, 0)
        self.gridlayout.setVerticalSpacing(3)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.mFieldNameLabel = QtGui.QLabel(self.mNewFieldGroupBox)
        self.mFieldNameLabel.setObjectName(_fromUtf8("mFieldNameLabel"))
        self.gridlayout.addWidget(self.mFieldNameLabel, 0, 0, 1, 1)
        self.mOutputFieldNameLineEdit = QtGui.QLineEdit(self.mNewFieldGroupBox)
        self.mOutputFieldNameLineEdit.setObjectName(_fromUtf8("mOutputFieldNameLineEdit"))
        self.gridlayout.addWidget(self.mOutputFieldNameLineEdit, 0, 1, 1, 3)
        self.mOutputFieldTypeLabel = QtGui.QLabel(self.mNewFieldGroupBox)
        self.mOutputFieldTypeLabel.setObjectName(_fromUtf8("mOutputFieldTypeLabel"))
        self.gridlayout.addWidget(self.mOutputFieldTypeLabel, 1, 0, 1, 1)
        self.mOutputFieldTypeComboBox = QtGui.QComboBox(self.mNewFieldGroupBox)
        self.mOutputFieldTypeComboBox.setObjectName(_fromUtf8("mOutputFieldTypeComboBox"))
        self.gridlayout.addWidget(self.mOutputFieldTypeComboBox, 1, 1, 1, 3)
        self.mOutputFieldWidthLabel = QtGui.QLabel(self.mNewFieldGroupBox)
        self.mOutputFieldWidthLabel.setObjectName(_fromUtf8("mOutputFieldWidthLabel"))
        self.gridlayout.addWidget(self.mOutputFieldWidthLabel, 2, 0, 1, 1)
        self.mOutputFieldWidthSpinBox = QtGui.QSpinBox(self.mNewFieldGroupBox)
        self.mOutputFieldWidthSpinBox.setMinimum(0)
        self.mOutputFieldWidthSpinBox.setProperty("value", 15)
        self.mOutputFieldWidthSpinBox.setObjectName(_fromUtf8("mOutputFieldWidthSpinBox"))
        self.gridlayout.addWidget(self.mOutputFieldWidthSpinBox, 2, 1, 1, 1)
        self.mOutputFieldPrecisionLabel = QtGui.QLabel(self.mNewFieldGroupBox)
        self.mOutputFieldPrecisionLabel.setObjectName(_fromUtf8("mOutputFieldPrecisionLabel"))
        self.gridlayout.addWidget(self.mOutputFieldPrecisionLabel, 2, 2, 1, 1)
        self.mOutputFieldPrecisionSpinBox = QtGui.QSpinBox(self.mNewFieldGroupBox)
        self.mOutputFieldPrecisionSpinBox.setProperty("value", 2)
        self.mOutputFieldPrecisionSpinBox.setObjectName(_fromUtf8("mOutputFieldPrecisionSpinBox"))
        self.gridlayout.addWidget(self.mOutputFieldPrecisionSpinBox, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.mNewFieldGroupBox, 2, 0, 1, 1)
        self.mButtonBox = QtGui.QDialogButtonBox(FieldsCalculator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mButtonBox.sizePolicy().hasHeightForWidth())
        self.mButtonBox.setSizePolicy(sizePolicy)
        self.mButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.mButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.mButtonBox.setObjectName(_fromUtf8("mButtonBox"))
        self.gridLayout.addWidget(self.mButtonBox, 5, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(FieldsCalculator)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cmbInputLayer = QtGui.QComboBox(FieldsCalculator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbInputLayer.sizePolicy().hasHeightForWidth())
        self.cmbInputLayer.setSizePolicy(sizePolicy)
        self.cmbInputLayer.setObjectName(_fromUtf8("cmbInputLayer"))
        self.horizontalLayout.addWidget(self.cmbInputLayer)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.mUpdateExistingGroupBox = QtGui.QGroupBox(FieldsCalculator)
        self.mUpdateExistingGroupBox.setFlat(True)
        self.mUpdateExistingGroupBox.setCheckable(True)
        self.mUpdateExistingGroupBox.setChecked(False)
        self.mUpdateExistingGroupBox.setObjectName(_fromUtf8("mUpdateExistingGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mUpdateExistingGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mExistingFieldComboBox = QtGui.QComboBox(self.mUpdateExistingGroupBox)
        self.mExistingFieldComboBox.setObjectName(_fromUtf8("mExistingFieldComboBox"))
        self.verticalLayout.addWidget(self.mExistingFieldComboBox)
        self.gridLayout.addWidget(self.mUpdateExistingGroupBox, 2, 1, 1, 1)
        self.builder = QgsExpressionBuilderWidget(FieldsCalculator)
        self.builder.setAutoFillBackground(False)
        self.builder.setObjectName(_fromUtf8("builder"))
        self.gridLayout.addWidget(self.builder, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(FieldsCalculator)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.leOutputFile = QtGui.QLineEdit(FieldsCalculator)
        self.leOutputFile.setObjectName(_fromUtf8("leOutputFile"))
        self.horizontalLayout_2.addWidget(self.leOutputFile)
        self.btnBrowse = QtGui.QToolButton(FieldsCalculator)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout_2.addWidget(self.btnBrowse)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.progressBar = QtGui.QProgressBar(FieldsCalculator)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 2)
        self.mFieldNameLabel.setBuddy(self.mOutputFieldNameLineEdit)
        self.mOutputFieldTypeLabel.setBuddy(self.mOutputFieldTypeComboBox)
        self.mOutputFieldWidthLabel.setBuddy(self.mOutputFieldWidthSpinBox)
        self.mOutputFieldPrecisionLabel.setBuddy(self.mOutputFieldPrecisionSpinBox)

        self.retranslateUi(FieldsCalculator)
        QtCore.QObject.connect(self.mButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FieldsCalculator.accept)
        QtCore.QObject.connect(self.mButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FieldsCalculator.reject)
        QtCore.QMetaObject.connectSlotsByName(FieldsCalculator)
        FieldsCalculator.setTabOrder(self.mOutputFieldNameLineEdit, self.mOutputFieldTypeComboBox)
        FieldsCalculator.setTabOrder(self.mOutputFieldTypeComboBox, self.mOutputFieldWidthSpinBox)
        FieldsCalculator.setTabOrder(self.mOutputFieldWidthSpinBox, self.mOutputFieldPrecisionSpinBox)
        FieldsCalculator.setTabOrder(self.mOutputFieldPrecisionSpinBox, self.mButtonBox)

    def retranslateUi(self, FieldsCalculator):
        FieldsCalculator.setWindowTitle(QtGui.QApplication.translate("FieldsCalculator", "Field calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.mNewFieldGroupBox.setTitle(QtGui.QApplication.translate("FieldsCalculator", "Create a new field", None, QtGui.QApplication.UnicodeUTF8))
        self.mFieldNameLabel.setText(QtGui.QApplication.translate("FieldsCalculator", "Output field name", None, QtGui.QApplication.UnicodeUTF8))
        self.mOutputFieldTypeLabel.setText(QtGui.QApplication.translate("FieldsCalculator", "Output field type", None, QtGui.QApplication.UnicodeUTF8))
        self.mOutputFieldWidthLabel.setText(QtGui.QApplication.translate("FieldsCalculator", "Output field width", None, QtGui.QApplication.UnicodeUTF8))
        self.mOutputFieldWidthSpinBox.setToolTip(QtGui.QApplication.translate("FieldsCalculator", "Width of complete output. For example 123,456 means 6 as field width.", None, QtGui.QApplication.UnicodeUTF8))
        self.mOutputFieldPrecisionLabel.setText(QtGui.QApplication.translate("FieldsCalculator", "Precision", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FieldsCalculator", "Input layer", None, QtGui.QApplication.UnicodeUTF8))
        self.mUpdateExistingGroupBox.setTitle(QtGui.QApplication.translate("FieldsCalculator", "Update existing field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FieldsCalculator", "Output file", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse.setText(QtGui.QApplication.translate("FieldsCalculator", "...", None, QtGui.QApplication.UnicodeUTF8))

from qgis.gui import QgsExpressionBuilderWidget
