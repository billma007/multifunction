from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 468)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(160, 140, 261, 141))

        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)

        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 70, 121, 46))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.layoutWidget)

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(157, 314, 271, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(157, 350, 271, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_3.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton.clicked.connect(Form.queryWeather)
        self.pushButton_3.clicked.connect(Form.GoToGitHub)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "马哥天气快速查询(GUI版)-天气情况2.0.0正式版"))
        self.label.setText(_translate("Form", "城市天气查询"))
        self.label_2.setText(_translate("Form", "城市"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.pushButton_3.setText(_translate("Form", "本项目开源，点击前往GitHub及官方网站查看说明"))


