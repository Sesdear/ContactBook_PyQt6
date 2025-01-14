# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(692, 490)
        Frame.setMinimumSize(QtCore.QSize(692, 490))
        Frame.setMaximumSize(QtCore.QSize(692, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../phone-book.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Frame.setWindowIcon(icon)
        Frame.setStyleSheet("background-color:rgb(61, 61, 61);\n"
"")
        self.frame_show = QtWidgets.QFrame(parent=Frame)
        self.frame_show.setGeometry(QtCore.QRect(9, 219, 391, 261))
        self.frame_show.setStyleSheet("Background-color:rgb(102, 102, 102);\n"
"border-radius:15px")
        self.frame_show.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_show.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_show.setObjectName("frame_show")
        self.widget = QtWidgets.QWidget(parent=self.frame_show)
        self.widget.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.widget.setStyleSheet("background-color:rgb(132, 132, 132);\n"
"border-radius:8px\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 281, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(parent=self.frame_show)
        self.widget_2.setGeometry(QtCore.QRect(9, 59, 371, 191))
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color:rgb(132, 132, 132);\n"
"    border-radius:8px\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(181, 181, 181);\n"
"    border:none;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(191, 191, 191)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(216, 216, 216);\n"
"    color:rgb(57, 57, 57)\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 141, 41))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgb(193, 193, 193);\n"
"color:rgb(0, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:rgb(193, 193, 193);\n"
"color:rgb(0, 0, 0)")
        self.label_6.setObjectName("label_6")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 371, 191))
        self.widget_4.setStyleSheet("QWidget{\n"
"    background-color:rgb(132, 132, 132);\n"
"    border-radius:8px\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(181, 181, 181);\n"
"    border:none;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(191, 191, 191)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(216, 216, 216);\n"
"    color:rgb(57, 57, 57)\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.buttonShow = QtWidgets.QPushButton(parent=self.widget_4)
        self.buttonShow.setGeometry(QtCore.QRect(10, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.buttonShow.setFont(font)
        self.buttonShow.setStyleSheet("")
        self.buttonShow.setObjectName("buttonShow")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.showLabelNumber = QtWidgets.QLabel(parent=self.widget_4)
        self.showLabelNumber.setGeometry(QtCore.QRect(80, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.showLabelNumber.setFont(font)
        self.showLabelNumber.setStyleSheet("background-color:rgb(193, 193, 193);\n"
"color:rgb(0, 0, 0)")
        self.showLabelNumber.setText("")
        self.showLabelNumber.setObjectName("showLabelNumber")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.showLabelName = QtWidgets.QLabel(parent=self.widget_4)
        self.showLabelName.setGeometry(QtCore.QRect(60, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.showLabelName.setFont(font)
        self.showLabelName.setStyleSheet("background-color:rgb(193, 193, 193);\n"
"color:rgb(0, 0, 0)")
        self.showLabelName.setText("")
        self.showLabelName.setObjectName("showLabelName")
        self.buttonDelete = QtWidgets.QPushButton(parent=self.widget_4)
        self.buttonDelete.setGeometry(QtCore.QRect(230, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.buttonDelete.setFont(font)
        self.buttonDelete.setStyleSheet("")
        self.buttonDelete.setObjectName("buttonDelete")
        self.frame_info = QtWidgets.QFrame(parent=Frame)
        self.frame_info.setGeometry(QtCore.QRect(410, 10, 271, 471))
        self.frame_info.setStyleSheet("Background-color:rgb(102, 102, 102);\n"
"border-radius:15px")
        self.frame_info.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_info.setObjectName("frame_info")
        self.contactList = QtWidgets.QListWidget(parent=self.frame_info)
        self.contactList.setGeometry(QtCore.QRect(15, 21, 241, 441))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(10)
        font.setBold(True)
        self.contactList.setFont(font)
        self.contactList.setStyleSheet("background-color:rgb(148, 148, 148);\n"
"border-radius:5px;\n"
"color:rgb(255, 255, 255)\n"
"")
        self.contactList.setObjectName("contactList")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_info)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 121, 20))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.frame_add = QtWidgets.QFrame(parent=Frame)
        self.frame_add.setGeometry(QtCore.QRect(10, 10, 391, 201))
        self.frame_add.setStyleSheet("Background-color:rgb(102, 102, 102);\n"
"border-radius:15px")
        self.frame_add.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_add.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_add.setObjectName("frame_add")
        self.widget_3 = QtWidgets.QWidget(parent=self.frame_add)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.widget_3.setStyleSheet("background-color:rgb(132, 132, 132);\n"
"border-radius:8px\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.widget_5 = QtWidgets.QWidget(parent=self.frame_add)
        self.widget_5.setGeometry(QtCore.QRect(10, 50, 371, 141))
        self.widget_5.setStyleSheet("QWidget{\n"
"    background-color:rgb(132, 132, 132);\n"
"    border-radius:8px\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(181, 181, 181);\n"
"    border:none;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(191, 191, 191)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(216, 216, 216);\n"
"    color:rgb(57, 57, 57)\n"
"}\n"
"QLineEdit{\n"
"    background-color:rgb(193, 193, 193);\n"
"    color:rgb(0, 0, 0)\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.label_12 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_12.setGeometry(QtCore.QRect(10, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_14.setObjectName("label_14")
        self.buttonAdd = QtWidgets.QPushButton(parent=self.widget_5)
        self.buttonAdd.setGeometry(QtCore.QRect(10, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        font.setBold(False)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")
        self.NameEntry = QtWidgets.QLineEdit(parent=self.widget_5)
        self.NameEntry.setGeometry(QtCore.QRect(60, 11, 301, 41))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.NameEntry.setFont(font)
        self.NameEntry.setObjectName("NameEntry")
        self.NumberEntry = QtWidgets.QLineEdit(parent=self.widget_5)
        self.NumberEntry.setGeometry(QtCore.QRect(80, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("SF Pro Text")
        font.setPointSize(12)
        self.NumberEntry.setFont(font)
        self.NumberEntry.setObjectName("NumberEntry")
        self.label_9 = QtWidgets.QLabel(parent=Frame)
        self.label_9.setGeometry(QtCore.QRect(0, 470, 81, 31))
        self.label_9.setStyleSheet("Background:none")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Записная Книга"))
        self.label.setText(_translate("Frame", "Информация о выбраном контакте"))
        self.pushButton.setText(_translate("Frame", "Показать"))
        self.label_2.setText(_translate("Frame", "Номер:"))
        self.label_4.setText(_translate("Frame", "+70000000000"))
        self.label_5.setText(_translate("Frame", "Имя:"))
        self.label_6.setText(_translate("Frame", "Сергей Орехов Алексеевич"))
        self.buttonShow.setText(_translate("Frame", "Показать"))
        self.label_7.setText(_translate("Frame", "Номер:"))
        self.label_10.setText(_translate("Frame", "Имя:"))
        self.buttonDelete.setText(_translate("Frame", "Удалить"))
        self.label_3.setText(_translate("Frame", "Список номеров"))
        self.label_8.setText(_translate("Frame", "Добавить новый контакт"))
        self.label_12.setText(_translate("Frame", "Номер:"))
        self.label_14.setText(_translate("Frame", "Имя:"))
        self.buttonAdd.setText(_translate("Frame", "Добавить"))
        self.label_9.setText(_translate("Frame", "Pre_Build: 0.0.1"))
