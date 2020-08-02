# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import qtawesome
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from face_pictures import*
from face_in_camera import *
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960,700)
        self.setWindowTitle("人脸识别系统")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("data/3.jpg")))
        self.setWindowIcon(QIcon('data/logo.jpg'))
        self.setPalette(window_pale)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.photo', color='white'), "图片识别")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.slot_btn_function)
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.camera', color='white'), "相机识别")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(self.slot_btn_function1)
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.close', color='white'), "退出")
        self.left_button_3.clicked.connect(self.close)
        self.left_button_3.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')
    def slot_btn_function(self):
        self.t = two()
        self.t.show()

    def slot_btn_function1(self):
        self.s = face_in_camera()


class two(QMainWindow):

    def __init__(self):
        super(two, self).__init__()
        self.resize(500, 100)
        self.setWindowTitle('图片输入')
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 10, 100, 60))
        self.label.setText('请输入图片路径')
        self.label.setObjectName('label')
        self.label.setToolTip('label提示')
        self.textbox = Qt.QLineEdit(self)
        self.textbox.resize(200, 20)
        self.textbox.move(100, 50)
        self.btn = QtWidgets.QPushButton('确认', self)
        self.btn.resize(50, 20)
        self.btn.move(350, 50)
        self.btn.setStyleSheet("background-color: rgb(255, 255, 255);"

                               "border-color: rgb(170, 150, 163);"

                               "font: 75 12pt \"Arial Narrow\";"

                               "color: rgb(0, 0, 0);")
        self.btn.clicked.connect(self.clickbtn)
        self.show()
    def clickbtn(self):
        textboxValue = self.textbox.text()
        if textboxValue=='':
            self.textbox.setText('')
        else:
            self.s=face_picture(textboxValue)

        self.textbox.setText('')


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()