from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QPixmap, QColor
import sys
import os
import subprocess
class tool_ex(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('外部工具')
        self.diskgenius= QPushButton('DiskGenius', self)
        self.diskgenius.clicked.connect(self.dg)
        self.diskgenius.setGeometry(QtCore.QRect(0,0,200,40))

        self.dism_64 = QPushButton('Dism++64位', self)
        self.dism_64.clicked.connect(self.dism64)
        self.dism_64.setGeometry(QtCore.QRect(0,50,200,40))

        self.dism_32 = QPushButton('Dism++32位', self)
        self.dism_32.clicked.connect(self.dism32)
        self.dism_32.setGeometry(QtCore.QRect(0,100,200,40))

        self.dism_arm64 = QPushButton('Dism++Arm架构64位', self)
        self.dism_arm64.clicked.connect(self.dismarm64)
        self.dism_arm64.setGeometry(QtCore.QRect(0,150,200,40))

        self.detect = QPushButton('硬件检测工具', self)
        self.detect.clicked.connect(self.det)
        self.detect.setGeometry(QtCore.QRect(0,200,200,40))
    def dism64(self):
        os.system("tools\Dism++\Dism++x64")
    def dism32(self):
        os.system("tools\Dism++\Dism++x86")
    def dismarm64(self):
        os.system("tools\Dism++\Dism++ARM64")
    def dg(self):
        os.system("tools\dg")
    def det(self):
        os.system("tools\图拉丁硬件检测\图拉丁硬件检测.exe")

class caidan(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('彩蛋')
        text_edit = QTextEdit(self)
        text_edit.setPlainText('''
只要功夫深，bug如井喷。
一测三千年，测完成荒坟。
熟识与非门，交谈非真人。
谁解其中味，颈雄已沉沉!
    ——致敬程序开发者
    ——GXBF
    ——shengrui11
我们准备了很多屎山代码，快去看看吧！''')
        text_edit.setReadOnly(True)
        self.setCentralWidget(text_edit)
        button = QPushButton('关闭❎', self)
        button.move(100, 220)
        button.clicked.connect(self.close)

        self.setFixedSize(200, 250)

class shutwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('关机命令集')
        self.shutdown_i = QPushButton('有注释的关机', self)
        self.shutdown_i.clicked.connect(self.shutdowni)
        self.shutdown_i.setGeometry(QtCore.QRect(0, 0, 200, 41))
        #self.webbutton.setGeometry(QtCore.QRect(0, 50, 200, 41))

    def shutdowni(self):
        subprocess.call(["shutdown","-i"])

class shit(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('探索系统屎山')
        self.shutbutton = QPushButton('关机命令集', self)
        self.webbutton = QPushButton('简易官网', self)
        self.webbutton.clicked.connect(self.webwindow)
        self.shutbutton.clicked.connect(self.shutwindow)
        self.shutbutton.setGeometry(QtCore.QRect(0,0,200,41))
        self.webbutton.setGeometry(QtCore.QRect(0,50,200,41))
    def shutwindow(self):
        self.open = shutwindow()
        self.open.show()
    def webwindow(self):
        self.open = WebWindow()
        self.open.show()


'''class ticket(object):

    # 设置UI的方法
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # 设置窗体对象名称
        MainWindow.resize(960, 786)  # 设置窗体大小
        MainWindow.setMinimumSize(QtCore.QSize(960, 786))  # 主窗体最小值
        MainWindow.setMaximumSize(QtCore.QSize(960, 786))  # 主窗体最大值
        self.centralwidget = QtWidgets.QWidget(MainWindow)  # 主窗体的widget控件
        self.centralwidget.setObjectName("centralwidget")  # 设置对象名称

        # 通过label控件显示顶部图片
        self.label_title_img = QtWidgets.QLabel(self.centralwidget)
        self.label_title_img.setGeometry(QtCore.QRect(0, 0, 960, 141))
        self.label_title_img.setObjectName("label_title_img")
        title_img = QPixmap('img/bg1.png')  # 打开顶部位图
        self.label_title_img.setPixmap(title_img)  # 设置调色板

        # 查询部分的widget
        self.widget_query = QtWidgets.QWidget(self.centralwidget)
        self.widget_query.setGeometry(QtCore.QRect(0, 141, 960, 80))
        self.widget_query.setObjectName("widget_query")
        # 开启自动填充背景
        self.widget_query.setAutoFillBackground(True)
        palette = QPalette()  # 调色板类
        palette.setBrush(QPalette.Background, QtGui.QBrush(QtGui.QPixmap('img/bg2.png')))  # 设置背景图片
        self.widget_query.setPalette(palette)  # 为控件设置对应的调色板即可

        # 出发地与对应的编辑框控件
        self.label = QtWidgets.QLabel(self.widget_query)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label.setObjectName("label")
        font = QtGui.QFont()  # 创建QFont()对象
        font.setPointSize(8)  # 设置编辑框字体大小的值
        self.label.setFont(font)  # 设置编辑框字体

        self.textEdit = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit.setGeometry(QtCore.QRect(80, 20, 104, 31))
        font = QtGui.QFont()  # 创建QFont()对象
        font.setPointSize(11)  # 设置编辑框字体大小的值
        self.textEdit.setFont(font)  # 设置编辑框字体
        self.textEdit.setObjectName("textEdit")  # 出发地对应编辑框对象名称

        # 目的地与对应的编辑框
        self.label_2 = QtWidgets.QLabel(self.widget_query)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 54, 12))
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()  # 创建QFont()对象
        font.setPointSize(8)  # 设置编辑框字体大小的值
        self.label_2.setFont(font)  # 设置编辑框字体
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 20, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        # 出发日与有对应的编辑框
        self.label_3 = QtWidgets.QLabel(self.widget_query)
        self.label_3.setGeometry(QtCore.QRect(410, 30, 54, 12))
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()  # 创建QFont()对象
        font.setPointSize(8)  # 设置编辑框字体大小的值
        self.label_3.setFont(font)  # 设置编辑框字体
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget_query)
        self.textEdit_3.setGeometry(QtCore.QRect(460, 20, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")

        # 查询按钮
        self.pushButton = QtWidgets.QPushButton(self.widget_query)
        self.pushButton.setGeometry(QtCore.QRect(610, 20, 91, 31))
        self.pushButton.setObjectName("pushButton")

        # 选择车次类型的widget
        self.widget_checkBox = QtWidgets.QWidget(self.centralwidget)
        self.widget_checkBox.setGeometry(QtCore.QRect(0, 220, 961, 35))
        self.widget_checkBox.setAutoFillBackground(False)
        self.widget_checkBox.setObjectName("widget_checkBox")
        # 开启自动填充背景
        self.widget_checkBox.setAutoFillBackground(True)
        palette = QPalette()  # 调色板类
        palette.setBrush(QPalette.Background, QtGui.QBrush(QtGui.QPixmap('img/bg3.png')))  # 设置背景图片
        self.widget_checkBox.setPalette(palette)  # 设置调色板控件对应的方法即可

        # 显示车次类型文字
        self.label_type = QtWidgets.QLabel(self.widget_checkBox)
        self.label_type.setGeometry(QtCore.QRect(30, 9, 65, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")

        # 选择高铁
        self.checkBox_G = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_G.setGeometry(QtCore.QRect(100, 9, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_G.setFont(font)
        self.checkBox_G.setObjectName("checkBox_GC")

        # 选择动车
        self.checkBox_D = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_D.setGeometry(QtCore.QRect(258, 9, 63, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_D.setFont(font)
        self.checkBox_D.setObjectName("checkBox_D")
        # 选择直达
        self.checkBox_Z = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_Z.setGeometry(QtCore.QRect(415, 9, 63, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_Z.setFont(font)
        self.checkBox_Z.setObjectName("checkBox_Z")
        # 选择特快
        self.checkBox_T = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_T.setGeometry(QtCore.QRect(572, 9, 63, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_T.setFont(font)
        self.checkBox_T.setObjectName("checkBox_T")
        # 选择快速
        self.checkBox_K = QtWidgets.QCheckBox(self.widget_checkBox)
        self.checkBox_K.setGeometry(QtCore.QRect(730, 9, 63, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_K.setFont(font)
        self.checkBox_K.setObjectName("checkBox_K")

        # 通过label控件显示火车信息图片
        self.label_train_img = QtWidgets.QLabel(self.centralwidget)
        self.label_train_img.setGeometry(QtCore.QRect(0, 256, 960, 62))
        self.label_train_img.setObjectName("label_train_img")
        train_img = QPixmap('img/bg4.png')  # 打开火车信息位图
        self.label_train_img.setPixmap(train_img)  # 设置调色板
        # 显示车次信息的列表
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 320, 960, 440))
        self.tableView.setObjectName("tableView")
        self.model = QStandardItemModel();  # 创建存储数据的模式
        # 根据空间自动改变列宽度并且不可修改列宽度
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表头不可见
        self.tableView.horizontalHeader().setVisible(False)
        # 纵向表头不可见
        self.tableView.verticalHeader().setVisible(False)
        # 设置表格内容文字大小
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView.setFont(font)
        # 设置表格内容不可编辑
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 垂直滚动条始终开启
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # 主窗体设置主Widget
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)  # 调用retranslateUi方法显示窗体文字
        QtCore.QMetaObject.connectSlotsByName(MainWindow)  # 关联信号槽

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快手查票"))
        self.checkBox_T.setText(_translate("MainWindow", "T-特快"))
        self.checkBox_K.setText(_translate("MainWindow", "K-快速"))
        self.checkBox_Z.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox_D.setText(_translate("MainWindow", "D-动车"))
        self.checkBox_G.setText(_translate("MainWindow", "GC-高铁"))
        self.label_type.setText(_translate("MainWindow", "车次类型："))
        self.label.setText(_translate("MainWindow", "出发地："))
        self.label_2.setText(_translate("MainWindow", "目的地："))
        self.label_3.setText(_translate("MainWindow", "出发日："))
        self.pushButton.setText(_translate("MainWindow", "查询"))

        self.textEdit_3.setText(get_time())  # 出发日显示当天日期
        self.pushButton.clicked.connect(self.on_click)  # 查询按钮指定单击事件的方法
        self.checkBox_G.stateChanged.connect(self.change_G)  # 高铁选中与取消事件
        self.checkBox_D.stateChanged.connect(self.change_D)  # 动车选中与取消事件
        self.checkBox_Z.stateChanged.connect(self.change_Z)  # 直达车选中与取消事件
        self.checkBox_T.stateChanged.connect(self.change_T)  # 特快车选中与取消事件
        self.checkBox_K.stateChanged.connect(self.change_K)  # 快车选中与取消事件

    # 查询按钮的单击事件
    def on_click(self):
        get_from = self.textEdit.toPlainText()  # 获取出发地
        get_to = self.textEdit_2.toPlainText()  # 获取到达地
        get_date = self.textEdit_3.toPlainText()  # 获取出发时间
        # 判断车站文件是否存在
        if isStations() == True:
            stations = eval(read())  # 读取所有车站并转换为dic类型
            # 判断所有参数是否为空，出发地、目的地、出发日期
            if get_from != "" and get_to != "" and get_date != "":
                # 判断输入的车站名称是否存在，以及时间格式是否正确
                if get_from in stations and get_to in stations and is_valid_date(get_date):
                    # 获取输入的日期是当前年初到现在一共过了多少天
                    inputYearDay = time.strptime(get_date, "%Y-%m-%d").tm_yday
                    # 获取系统当前日期是当前年初到现在一共过了多少天
                    yearToday = time.localtime(time.time()).tm_yday
                    # 计算时间差，也就是输入的日期减掉系统当前的日期
                    timeDifference = inputYearDay - yearToday
                    # 判断时间差为0时证明是查询当前的查票，
                    # 以及29天以后的车票。12306官方要求只能查询30天以内的车票
                    if timeDifference >= 0 and timeDifference <= 28:
                        from_station = stations[get_from]  # 在所有车站文件中找到对应的参数，出发地
                        to_station = stations[get_to]  # 目的地
                        data = query(get_date, from_station, to_station)  # 发送查询请求,并获取返回的信息
                        self.checkBox_default()
                        if len(data) != 0:  # 判断返回的数据是否为空
                            # 如果不是空的数据就将车票信息显示在表格中
                            self.displayTable(len(data), 16, data)
                        else:
                            self.messageDialog('警告', '没有返回的网络数据！')
                    else:
                        self.messageDialog('警告', '超出查询日期的范围内,'
                                                 '不可查询昨天的车票信息,以及29天以后的车票信息！')
                else:
                    self.messageDialog('警告', '输入的站名不存在,或日期格式不正确！')
            else:
                self.messageDialog('警告', '请填写车站名称！')
        else:
            self.messageDialog('警告', '未下载车站查询文件！')

    # 将所有车次分类复选框取消勾选
    def checkBox_default(self):
        self.checkBox_G.setChecked(False)
        self.checkBox_D.setChecked(False)
        self.checkBox_Z.setChecked(False)
        self.checkBox_T.setChecked(False)
        self.checkBox_K.setChecked(False)


    # 高铁复选框事件处理
    def change_G(self, state):
        # 选中将高铁信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            g_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data), 16, type_data)
        else:
            # 取消选中状态将移除该数据
            r_g_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 动车复选框事件处理
    def change_D(self, state):
        # 选中将动车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取动车信息
            d_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data), 16, type_data)

        else:
            # 取消选中状态将移除该数据
            r_d_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 直达复选框事件处理
    def change_Z(self, state):
        # 选中将直达车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取直达车信息
            z_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            # 取消选中状态将移除该数据
            r_z_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 特快复选框事件处理
    def change_T(self, state):
        # 选中将特快车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取特快车信息
            t_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            # 取消选中状态将移除该数据
            r_t_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 快速复选框事件处理
    def change_K(self, state):
        # 选中将快车信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取快速车信息
            k_vehicle()
            self.displayTable(len(type_data), 16, type_data)

        else:
            # 取消选中状态将移除该数据
            r_k_vehicle()
            self.displayTable(len(type_data), 16, type_data)

    # 显示消息提示框，参数title为提示框标题文字，message为提示信息
    def messageDialog(self, title, message):
        msg_box = QMessageBox(QMessageBox.Warning, title, message)
        msg_box.exec_()

    # 显示车次信息的表格
    # train参数为共有多少趟列车，该参数作为表格的行。
    # info参数为每趟列车的具体信息，例如有座、无座卧铺等。该参数作为表格的列
    def displayTable(self, train, info, data):
        self.model.clear()
        for row in range(train):
            for column in range(info):
                # 添加表格内容
                item = QStandardItem(data[row][column])
                # 向表格存储模式中添加表格具体信息
                self.model.setItem(row, column, item)
        # 设置表格存储数据的模式
        self.tableView.setModel(self.model)


# 获取系统当前时间并转换请求数据所需要的格式
def get_time():
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其它日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeStruct = time.localtime(now)
    strTime = time.strftime("%Y-%m-%d", timeStruct)
    return strTime


def is_valid_date(str):
    ''''判断是否是一个有效的日期字符串'''''
    try:
        time.strptime(str, "%Y-%m-%d")
        return True
    except:
        return False






openai.api_key = "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"
MODEL = "gpt-3.5-turbo-0301"
class ChatGPT(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ChatGPT")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.chat_history = QTextEdit()
        self.layout.addWidget(self.chat_history)

        self.input_layout = QHBoxLayout()
        self.input_text = QTextEdit()
        self.input_layout.addWidget(self.input_text)
        self.send_button = QPushButton("发送")
        self.send_button.clicked.connect(self.send_message)
        self.input_layout.addWidget(self.send_button)
        self.layout.addLayout(self.input_layout)

        self.central_widget.setLayout(self.layout)

        self.chatgpt = ChatGPT()  # 创建 ChatGPT 实例

    def send_message(self):
        user_message = self.input_text.toPlainText()
        self.input_text.clear()

        # 向 ChatGPT 发送用户消息并获取回复
        response = self.chatgpt.generate_response(user_message)

        # 显示用户消息和 ChatGPT 的回复
        self.chat_history.append("You: " + user_message)
        self.chat_history.append("ChatGPT: " + response)'''


# setGeometry(X,Y,宽,高)

class Calculator(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("计算器")

        # 创建界面组件
        self.input_line = QLineEdit()
        self.result_line = QLineEdit()
        self.result_line.setReadOnly(True)

        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        # 创建布局和组件添加
        layout = QGridLayout(self)
        layout.addWidget(self.input_line, 0, 0, 1, 4)
        layout.addWidget(self.result_line, 1, 0, 1, 4)

        row = 2
        col = 0
        for button_row in self.buttons:
            for label in button_row:
                button = QPushButton(label)
                button.clicked.connect(self.on_button_click)
                layout.addWidget(button, row, col)
                col += 1
            row += 1
            col = 0

    def on_button_click(self):
        button = self.sender()
        label = button.text()

        if label == "=":
            # 执行计算
            try:
                result = eval(self.input_line.text())
                self.result_line.setText(str(result))
            except Exception as e:
                self.result_line.setText("Error")
        elif label == "C":
            # 清除输入和结果
            self.input_line.clear()
            self.result_line.clear()
        else:
            # 向输入行添加按钮标签
            self.input_line.insert(label)

class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("官网")
        self.setGeometry(100, 100, 800, 600)
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("http://www.hopestu.mysxl.cn"))
        self.setCentralWidget(self.web_view)

    def show_image(self):
        pixmap = QPixmap(self.images[self.current_index])
        self.image_label.setPixmap(pixmap.scaled(self.image_label.width(), self.image_label.height()))

    def next_image(self):
        self.current_index += 1
        if self.current_index >= len(self.images):
            self.current_index = 0
        self.show_image()


class OtherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('其他')
        self.logbutton = QPushButton('开发日志', self)
        self.webbutton = QPushButton('简易官网', self)
        self.webbutton.clicked.connect(self.webwindow)
        self.logbutton.clicked.connect(self.logwindow)
        self.logbutton.setGeometry(QtCore.QRect(0,0,200,41))
        self.webbutton.setGeometry(QtCore.QRect(0,50,200,41))
    def logwindow(self):
        self.open = LogWindow()
        self.open.show()
    def webwindow(self):
        self.open = WebWindow()
        self.open.show()
# 页面实例



class LogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('开发日志')
        text_edit = QTextEdit(self)
        text_edit.setPlainText('''
                                尼玛反编译者死光光
                              Hope-Chat Teams定制版
一个一个的聊天室，用PyQt5制作。

Hope-Chat-Teams定制版只在Hope-Teams系列产品中附加，不和Hope-Chat走同一个发展路线。


''')
        text_edit.setReadOnly(True)
        self.setCentralWidget(text_edit)
        button = QPushButton('关闭❎', self)
        button.move(375, 465)
        button.clicked.connect(self.close)

        self.setFixedSize(500, 500)
        self.show()



class CopyRightWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('版权声明')
        text_edit = QTextEdit(self)
        text_edit.setPlainText('''
                               
                                    版权声明
 感谢您对希望工作室的关注和支持。在使用我们的产品、服务和内容之前，请务必仔细阅读并理解本版权声明。本版权声明将明确说明您与希望工作室之间的版权关系以及相关的权益和责任。



    1.版权所有：除非另有明确说明，希望工作室拥有所有产品、服务和内容（包括但不限于文字、图像、音频、视频、软件、标志、商标等）的版权。

    2.保护知识产权：希望工作室非常重视知识产权保护。未经希望工作室明确授权，禁止任何人使用、复制、修改、发布、传播、展示或运用希望工作室的知识产权内容。希望工作室保留依法追究侵权者法律责任的权利。

    3.授权使用：若您希望使用希望工作室的产品、服务或内容，请您与我们联系，获取书面授权。任何未经授权的使用行为将被视为侵权行为，希望工作室将采取相应的法律措施维护权益。

    4.用户提交内容：对于您在希望工作室的产品、服务或平台上提交的内容，您同意授予希望工作室非独占的、永久的、全球范围内的、免费的使用权许可。希望工作室有权在产品、服务或平台内使用、复制、展示、修改或传播您的提交内容，但不会非法使用您的个人信息。

    5.第三方内容和链接：希望工作室的产品、服务和内容可能包含第三方的知识产权内容或链接。对于这些内容和链接，希望工作室不能保证其准确性、合法性、安全性或完整性。用户在使用这些内容和链接时应自行判断，并承担相应的风险和责任。

    6免责声明：在法律允许的范围内，希望工作室不对因使用其产品、服务和内容而导致的任何直接或间接损失承担责任，包括但不限于利润损失、数据损失、业务中断等。用户在使用希望工作室的产品、服务和内容时应自行承担风险。

    7.法律适用和争议解决：本版权声明受中华人民共和国法律的约束。任何因使用希望工作室的产品、服务或内容而产生的争议，均应通过友好协商解决。协商不成的，您同意将争议提交至希望工作室所在地有管辖权的人民法院解决。



    本版权声明的解释权归希望工作室所有。希望工作室保留随时更新或修改本版权声明的权利。请您定期查阅本版权声明以了解任何修改。如您对本版权声明或希望工作室的版权问题有任何疑问或意见，请联系我们。

                                                                                                                                                                                                                                                                                                          希望工作室 版权所有
''')
        text_edit.setReadOnly(True)
        self.setCentralWidget(text_edit)
        button = QPushButton('关闭❎', self)
        button.move(375, 465)
        button.clicked.connect(self.close)

        self.setFixedSize(500, 500)
        self.show()

#聊天室
class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        self.pc = None  # 预设这个变量

        self.MainSet()
        self.createWidget()
        self.componentWidgets()

    # 设定Main窗口属性的函数

    def MainSet(self):
        self.setWindowTitle("Hope-Chat Teams定制版")

        # self.setFixedSize(730,400)

    def createWidget(self):
        self.centerWidget = QWidget()  # 中心窗口控件
        self.mainLayout = QGridLayout()
        self.rightBottomLayout = QVBoxLayout()
        self.rightTopLayout = QGridLayout()
        self.ControlBox = QGroupBox("控制面板")
        self.ConfigBox = QGroupBox("连接信息")
        self.chatEdit = QTextEdit()  # 聊天对话框
        self.chatEdit.setReadOnly(True)
        self.inputLine = QLineEdit()  # 输入框

        self.sendBtn = QPushButton("发送")
        self.sendBtn.clicked.connect(self.sendInfo)  # 向服务器发送信息(如果是服务器本身则广播)
        self.ipEdit = QLineEdit()  # IP输入栏
        self.ipEdit.setInputMask('000.000.000.000; ')  # 设定为IP输入格式
        self.hostIPbtn = QPushButton("获取本机IP")
        self.hostIPbtn.clicked.connect(self.getHostIP)
        self.portEdit = QLineEdit()  # 端口输入栏
        self.portEdit.setPlaceholderText("1145")  # 默认端口为9999
        self.hostEdit = QLineEdit()  # 主机名输入栏
        self.hostEdit.setPlaceholderText(socket.gethostname())  # 默认为本地主机
        self.serverRbtn = QRadioButton("创建服务器")
        self.serverRbtn.setChecked(True)
        self.serverRbtn.toggled.connect(self.radiobtnChange)
        self.clientRbtn = QRadioButton("加入服务器")
        self.connectBtn = QPushButton("连接")
        self.connectBtn.clicked.connect(self.setClient)
        self.connectBtn.setEnabled(False)
        self.buildServerBtn = QPushButton("创建")  # 建立服务器按钮
        self.buildServerBtn.clicked.connect(self.setServer)
        self.quitBtn = QPushButton("退出")  # 退出按钮
        self.quitBtn.clicked.connect(self.quit)
        self.otherBtn = QPushButton("其他")  # 退出按钮
        self.otherBtn.clicked.connect(self.otherwindow)
        # ---------------------------------------------------------
        self.statusBar = QStatusBar()  # 状态栏
    def otherwindow(self):
        self.open = OtherWindow()
        self.open.show()
    def componentWidgets(self):
        self.setCentralWidget(self.centerWidget)
        self.setStatusBar(self.statusBar)
        self.centerWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.chatEdit, 0, 0, 9, 2)
        self.mainLayout.addWidget(self.inputLine, 9, 0, 1, 1)
        self.mainLayout.addWidget(self.sendBtn, 9, 1, 1, 1)
        self.mainLayout.addWidget(self.ConfigBox, 0, 2, 5, 10)
        self.mainLayout.addWidget(self.ControlBox, 5, 2, 5, 10)
        self.ConfigBox.setLayout(self.rightTopLayout)
        self.rightTopLayout.addWidget(QLabel("服务器IP地址"), 0, 0, 1, 0)
        self.rightTopLayout.addWidget(self.ipEdit, 1, 0, 1, 3)
        self.rightTopLayout.addWidget(self.hostIPbtn, 1, 3, 1, 1)
        self.rightTopLayout.addWidget(QLabel("服务器端口"), 2, 0, 1, 1)
        self.rightTopLayout.addWidget(self.portEdit, 2, 1, 1, 3)
        self.rightTopLayout.addWidget(QLabel("昵称"), 3, 0, 1, 1)
        self.rightTopLayout.addWidget(self.hostEdit, 3, 1, 1, 3)
        self.rightTopLayout.addWidget(self.serverRbtn, 4, 0, 1, 2)
        self.rightTopLayout.addWidget(self.clientRbtn, 4, 2, 1, 2)
        self.ControlBox.setLayout(self.rightBottomLayout)
        self.rightBottomLayout.addWidget(self.connectBtn)
        self.rightBottomLayout.addWidget(self.buildServerBtn)
        self.rightBottomLayout.addWidget(self.quitBtn)
        self.rightBottomLayout.addWidget(self.otherBtn)

    def radiobtnChange(self, status):
        if status:
            self.connectBtn.setEnabled(False)
            self.buildServerBtn.setEnabled(True)
        else:
            self.connectBtn.setEnabled(True)
            self.buildServerBtn.setEnabled(False)

    def getHostIP(self):
        hostip = socket.gethostbyname_ex(socket.gethostname())
        self.ipEdit.setText(hostip[-1][-1])

    # 状态栏情况发送函数
    def sendInfo(self):
        if self.pc == None:
            self.statusBar.showMessage("发送失败！（连接走丢了）")
        else:
            info = self.inputLine.text()
            if info != "":
                info = self.pc.hostName + ":\n" + info
                self.pc.btnsend(info)
            else:
                self.statusBar.showMessage("不能发送空信息！")

    # 设定本主机为服务器
    def setServer(self):
        host = self.hostEdit.text()
        port = self.portEdit.text()
        ip = self.ipEdit.text()
        print(ip)
        if host == "": host = "服务器管理员"  # 服务主机
        if port == "": port = 1145  # 默认端口
        if ip == "...": ip = "127.0.0.1"  # 默认IP
        self.pc = Server(self, ip, host, int(port))

    # 设定本主机为客户端
    def setClient(self):
        host = self.hostEdit.text()
        port = self.portEdit.text()
        ip = self.ipEdit.text()
        if host == "": host = "匿名用户"  # 匿名用户
        if port == "": port = 1145  # 默认端口
        if ip == "...": ip = "127.0.0.1"  # 默认IP
        self.pc = Client(self, ip, host, int(port))

    def quit(self):
        if self.pc != None:
            self.pc.closeThread()
        self.close()


# 服务端
class Server():
    def __init__(self, widget, ip, host, port):
        # 设定本主机的一些基本信息 ---------------------------------------
        self.widget = widget
        self.ip = ip  # 获得该主机ip
        self.hostName = host  # 获得该主机名
        self.port = port  # 设定默认端口号(服务器端口号和客户端接入端口号都是这个默认端口)
        self.serverDict = {}  # 服务线程字典
        self.serverID = 0  # 初始的服务线程id
        self.buildSocket()

    # 创建网络连接实例
    def buildSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.AF_INET(!!INET - IPv4  INET6 - IPv6)
        # socket.SOCK_STREAM - 传输控制协议(TCP)
        self.initialServer()

    # 初始化服务(仅限服务器)
    def initialServer(self):
        # 首先绑定服务端口号
        self.socket.bind((self.ip, self.port))  # 绑定端口与主机名
        self.socket.listen(5)  # 设定最大连接数
        self.buildServer()  # 初始化一个服务线程

    # 创建服务线程
    def buildServer(self):
        server = ServerThread(str(self.serverID), self.socket)
        self.serverDict[str(self.serverID)] = server
        self.serverID += 1
        server._flag.connect(self.getFlag)
        server._signal.connect(self.getMessage)
        server._text.connect(self.getText)
        server.start()

    # 广播所有消息
    def bordCastInfo(self, info):
        print(len(self.serverDict))
        for client in self.serverDict:
            try:
                if self.serverDict[client].clientsocket != None:
                    print("尝试将信息广播出去")
                    self.serverDict[client].sendToClient(info)  # 将消息传入指定的客户端
                    print("广播成功")
            except Exception as reason:
                self.getFlag("@@@".join([client, "disconnect"]))  # 运行函数,停止某个客户端的监听(相当于关闭)
                print("服务端", reason)

    def btnsend(self, text):
        self.widget.chatEdit.append(text)
        self.bordCastInfo(text)

    # 关闭所有的服务
    def closeThread(self):
        for server in self.serverDict:
            self.serverDict[server].runflag = False

    def getFlag(self, flag):
        flag = flag.split("@@@")
        if flag[1] == "connect":  # 如果传来连接成功,则新开一个线程监听
            self.buildServer()
        elif flag[1] == "disconnect":  # 如果连接出现问题
            self.serverDict[flag[0]].runflag = False

    def getMessage(self, signal):
        signal = signal.split("@@@")
        self.widget.statusBar.showMessage("serverID为" + signal[0] + " 状态：" + signal[1])

    def getText(self, text):
        self.widget.chatEdit.append(text)
        self.bordCastInfo(text)  # 广播出去


# 客户端
class Client:  # 主机默认为本地主机,
    def __init__(self, widget, ip, hostName, port):
        self.widget = widget
        self.ip = ip
        self.hostName = hostName  # 获得该主机名
        self.port = port  # 设定默认端口号(服务器端口号和客户端接入端口号都是这个默认端口)
        self.buildSocket()

    def buildSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buildClient()

    def buildClient(self):
        self.client = ClientThread(self.socket)  # 获取连接
        self.client._flag.connect(self.getFlag)
        self.client._signal.connect(self.getMessage)
        self.client._text.connect(self.getText)
        if self.client.connectServer(self.ip, self.port):
            self.client.start()

    def sendToServer(self, text):  # 向服务器发送消息
        try:
            self.socket.send(text.encode('utf-8'))
        except Exception as reason:
            self.getMessage(reason)
            self.getFlag("disconnect")  # 发送连接失败标志

    def btnsend(self, text):
        self.sendToServer(text)

    def closeThread(self):
        self.runflag = False

    def getFlag(self, flag):
        if flag == "connect":
            self.widget.statusBar.showMessage("成功连接！")
        elif flag == "disconnect":
            self.client.runflag = False

    def getMessage(self, signal):
        self.widget.statusBar.showMessage(signal)

    def getText(self, text):
        self.widget.chatEdit.append(text)


# 监听连接线程,负责构成会话(服务端线程)
class ServerThread(QThread):
    _signal = pyqtSignal(str)  # 设定信号,主要向主线程发送信号
    _text = pyqtSignal(str)  # 设定信号,向主线程发送接收到的信息
    _flag = pyqtSignal(str)  # 设定信号,向主线程发送连接状态标志

    def __init__(self, serverID, serverSocket):
        super(ServerThread, self).__init__()
        self.serverID = serverID  # 获得主机实例
        self.serverSocket = serverSocket
        self.clientsocket = None
        self.addr = None
        self.runflag = True

        self.connectList = ["connect", "disconnect"]  # 连接成功与连接失败

    # 自动进行该函数
    def run(self):
        self.sendMessage("等待用户加入……")
        self.clientsocket, self.addr = self.serverSocket.accept()  # 收到客户端的连接后返回 连接控件,地址(持续监听,直到接收到执行下一个操作)
        print(self.clientsocket)
        self.sendText("正在连接IP为 %s" % str(self.addr) + "的服务器！")
        self.sendFlag(0)  # 发送连接成功标志
        self.getMessage()

    # 持续接受消息
    def getMessage(self):
        while self.runflag:
            try:
                data = self.clientsocket.recv(1024).decode('utf-8')  # 接受到字符串并按照utf-8编译
                self.sendText(data)
            except Exception as reason:
                self.sendMessage(str(reason))
                self.sendText(str(self.addr) + " 退出了服务器...")
                self.sendFlag(1)  # 发送断开连接标志
                break
        self.clientsocket.close()
        print("线程关闭成功")

    def sendToClient(self, info):
        print(self.clientsocket)
        try:
            self.clientsocket.send(info.encode("utf-8"))
            print("广播成功")
        except Exception as reason:
            print("广播失败原因", reason)
            self.sendMessage(self.addr + " 退出了服务器...")
            self.sendFlag(1)

    # 发送状态信号函数
    def sendMessage(self, message):
        self._signal.emit("@@@".join([self.serverID, message]))

    # 发送接收到的消息信号
    def sendText(self, text):
        self._text.emit(text)

    # 发送连接状态标志
    def sendFlag(self, flagIndex):
        self._flag.emit("@@@".join([self.serverID, self.connectList[flagIndex]]))


class ClientThread(QThread):
    _signal = pyqtSignal(str)
    _text = pyqtSignal(str)
    _flag = pyqtSignal(str)

    def __init__(self, serverSocket):
        super(ClientThread, self).__init__()
        self.serverSocket = serverSocket
        self.runflag = True
        self.connectList = ["connect", "disconnect"]  # 连接成功与连接失败

    def connectServer(self, ip, port):
        try:
            self.serverSocket.connect((ip, port))
            self.sendFlag(0)  # 发送连接成功标志
            return True
        except Exception as reason:
            self.sendMessage(reason)
            self.sendFlag(1)  # 发送链接失败标志
            return reason

    def run(self):
        while self.runflag:
            try:
                msg = self.serverSocket.recv(1024).decode("utf-8")  # 接受服务端消息
                self.sendText(msg)
            except Exception as reason:
                self.sendMessage(reason)
                self.sendFlag(1)  # 发送连接失败标志
                break

    def sendMessage(self, message):
        self._signal.emit(str(message))

    def sendText(self, text):
        self._text.emit(str(text))

    def sendFlag(self, flagIndex):
        self._flag.emit(str(self.connectList[flagIndex]))



















#MainUi类
class mainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainUi(self)
        self.pc = None  # 预设这个变量
        self.setFixedSize(1200, 665)


        #定义mainUi
    def mainUi(self,main):
        self.resize(1200, 665)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(920, 110, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1352, 23))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)
        self.news = QtWidgets.QGroupBox(self.centralwidget)
        self.news.setGeometry(QtCore.QRect(620, 100, 271, 481))
        self.news.setObjectName("news")
        self.newtitle_1 = QtWidgets.QLabel(self.news)
        self.newtitle_1.setGeometry(QtCore.QRect(20, 40, 300, 41))
        self.newtitle_1.setObjectName("newtitle_1")
        self.newtitle_2 = QtWidgets.QLabel(self.news)
        self.newtitle_2.setGeometry(QtCore.QRect(20, 130, 300, 41))
        self.newtitle_2.setObjectName("newtitle_2")

        self.newtitle_3 = QtWidgets.QLabel(self.news)
        self.newtitle_3.setGeometry(QtCore.QRect(20, 220, 300, 41))
        self.newtitle_3.setObjectName("newtitle_3")

        self.newtitle_4 = QtWidgets.QLabel(self.news)
        self.newtitle_4.setGeometry(QtCore.QRect(20, 310, 300, 41))
        self.newtitle_4.setObjectName("newtitle_3")

        self.read_1 = QtWidgets.QPushButton(self.news)
        self.read_1.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.read_1.setObjectName("read_1")
        self.read_1.clicked.connect(self.open_webpage)

        self.read_2 = QtWidgets.QPushButton(self.news)
        self.read_2.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.read_2.setObjectName("read_2")
        self.read_2.clicked.connect(self.open_CopyRightWindow)

        self.read_3 = QtWidgets.QPushButton(self.news)
        self.read_3.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.read_3.setObjectName("read_3")
        self.read_3.clicked.connect(self.open_join)

        self.read_4 = QtWidgets.QPushButton(self.news)
        self.read_4.setGeometry(QtCore.QRect(170, 360, 75, 23))
        self.read_4.setObjectName("read_4")
        self.read_4.clicked.connect(self.open_asia_games)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(150,0,501, 111))
        self.title.setMinimumSize(QtCore.QSize(501, 111))
        self.title.setMaximumSize(QtCore.QSize(501, 111))
        self.title.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.title.setObjectName("title")

        self.chat_andXXX = QtWidgets.QGroupBox(self.centralwidget)
        self.chat_andXXX.setGeometry(QtCore.QRect(10, 160, 601, 481))
        self.chat_andXXX.setObjectName("chat_andXXX")

        self.chat_2 = QtWidgets.QPushButton(self.chat_andXXX)
        self.chat_2.setGeometry(QtCore.QRect(20, 20, 171, 51))
        self.chat_2.setObjectName("chat_2")
        self.chat_2.clicked.connect(self.open_ChatRoom)

        self.calc = QtWidgets.QPushButton(self.chat_andXXX)
        self.calc.setGeometry(QtCore.QRect(20, 80, 171, 51))
        self.calc.setObjectName("calculator")
        self.calc.clicked.connect(self.open_calculator)

        self.tic = QtWidgets.QPushButton(self.chat_andXXX)
        self.tic.setGeometry(QtCore.QRect(200,80,171,51))
        self.tic.setObjectName("ticket")
        #self.tic.clicked.connect(self.open_tic)

        self.shit = QtWidgets.QPushButton(self.chat_andXXX)
        self.shit.setGeometry(QtCore.QRect(200,80,171,51))
        self.shit.setObjectName("shit")
        self.shit.clicked.connect(self.open_shit)

        self.tools = QPushButton(self.chat_andXXX)
        self.tools.clicked.connect(self.open_tools_ex)
        self.tools.setGeometry(QtCore.QRect(380, 80, 171, 51))
        self.tools.setObjectName("tools")

        self.caidan = QPushButton(self.chat_andXXX)
        self.caidan.clicked.connect(self.open_caidan)
        self.caidan.setGeometry(QtCore.QRect(370, 20, 171, 51))
        self.caidan.setObjectName("caidan")

        self.shutdown_button = QPushButton(self.chat_andXXX)
        self.shutdown_button.clicked.connect(self.shutdown)
        self.shutdown_button.setGeometry(QtCore.QRect(380, 20, 171, 51))
        self.shutdown_button.setObjectName("shutdown")

        self.AI_Robot = QtWidgets.QPushButton(self.chat_andXXX)
        self.AI_Robot.setGeometry(QtCore.QRect(200, 20, 171, 51))
        self.AI_Robot.setObjectName("AI_Robot")
        #self.AI_Robot.clicked.connect(self.open_GPT)

        self.youaresmart = QtWidgets.QLabel(self.centralwidget)
        self.youaresmart.setGeometry(QtCore.QRect(10, 120, 411, 31))
        self.youaresmart.setObjectName("youaresmart")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(620, 590, 271, 51))
        self.exit.setObjectName("exit")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(10, 0, 121, 121))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.icon.setObjectName("icon")
        self.setCentralWidget(self.centralwidget)
        self.icon.setBuddy(self.icon)
        self.mainretranslateUi(main)
        self.exit.clicked.connect(main.close) # type: ignore
        self.mainretranslateUi(main)
    def open_asia_games(self):
        url = QUrl("https://sports.cctv.com/")  # 替换为你要打开的网页地址
        QDesktopServices.openUrl(url)
    def open_join(self):
        url = QUrl("http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=ZWK9Hjr85usU530C3rt0X_3a3ELG0o9e&authKey=g5Q5ELTce3ChemOo76dqWRxgCbJOHRJ6cRWiEJGFL95vR+JE4tyB2yqgTj5V22xf&noverify=0&group_code=876244203")  # 替换为你要打开的网页地址
        QDesktopServices.openUrl(url)
    def open_tools_ex(self):
        self.open = tool_ex()
        self.open.show()
    def open_caidan(self):
        self.open = caidan()
        self.open.show()
    def open_shit(self):
        self.open = shit()
        self.open.show()
    def open_GPT(self):
        '''self. open = ChatGPT()'''
        #self.open.show()
    def open_CopyRightWindow(self):
        self.open = CopyRightWindow()
        self.show()
    def open_webpage(self):
        url = QUrl("https://hopestu.mysxl.cn/")  # 替换为你要打开的网页地址
        QDesktopServices.openUrl(url)
    def open_calculator(self):
        self.open = Calculator()
        self.open.show()
    def shutdown(self):
        subprocess.call(["shutdown","-s", "-t","0"])
    #打开聊天室
    def open_ChatRoom(self):
        self.open = MainWin()
        self.open.show()
        #弄了会死
        #self.window_b.exit(app.exec_())

    #加载UI
    def mainretranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate


        main.setWindowTitle(_translate("main", "Hope-Teams 1.4.7"))
        self.read_4.setText(_translate("main","查看"))
        self.tools.setText(_translate("main","牛逼の外部工具"))
        self.caidan.setText(_translate("main", "1145141919810"))
        self.shit.setText(_translate("main", "探索系统屎山"))
        self.tic.setText(_translate("main","查火车票 （暂未开放）"))
        self.news.setTitle(_translate("main", "开发者新闻"))
        self.newtitle_1.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">我们的网站</span></p></body></html>"))
        self.newtitle_2.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">版权声明</span></p></body></html>"))
        self.newtitle_3.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">加入QQ交流群</span></p></body></html>"))
        self.newtitle_4.setText(_translate("main","<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">在线看亚运</span></p></body></html>"))
        self.read_1.setText(_translate("main", "查看"))
        self.read_2.setText(_translate("main", "查看"))
        self.read_3.setText(_translate("main", "查看"))
        self.title.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:72pt;\">Hope-Teams</span></p></body></html>"))
        self.chat_andXXX.setTitle(_translate("main", "工具"))
        self.chat_2.setText(_translate("main", "聊天室"))
        self.AI_Robot.setText(_translate("main", "AI机器人（余额用尽）"))
        self.shutdown_button.setText(_translate("main", "一键关机（慎用）"))
        self.calc.setText(_translate("main", "简易计算器"))
        self.youaresmart.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">你今天看起来很聪明！</span></p></body></html>"))
        self.exit.setText(_translate("main", "退出..."))





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainwindow = mainUi()
    mainwindow.show()
    sys.exit(app.exec_())