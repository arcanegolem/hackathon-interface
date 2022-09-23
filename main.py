import sys
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from datetime import datetime

from picbutton import PicButton


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Window size
        self.WIDTH = 900
        self.HEIGHT = 600
        self.resize(self.WIDTH, self.HEIGHT)

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(self.WIDTH, self.HEIGHT)
        self.setCentralWidget(self.centralwidget)
        
        radius = 15
        self.centralwidget.setStyleSheet(
            """
            background: white;
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )

        # Initial
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(1)

        # Top left icon
        self.iconMascot = QLabel(self.centralwidget)
        self.iconMascot.setPixmap(QPixmap("assets/icon_xs.png"))
        self.iconMascot.resize(50, 50)
        self.iconMascot.setGeometry(QRect(10, 10, 50, 50))

        _translate = QCoreApplication.translate
        radius = 15
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QRect(50, 80, 400, 400))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                       "font: 12pt \"Consolas\";\n"
                                       "border-top-left-radius:{0}px;\n"
                                       "border-bottom-left-radius:{0}px;\n"
                                       "border-top-right-radius:{0}px;\n"
                                       "border-bottom-right-radius:{0}px;\n"
                                       "padding: 10px".format(radius)
                                       )
        self.textBrowser.setObjectName("textBrowser")

        # # Top left name
        # self.message = QLabel(self.centralwidget)
        # self.message.setPixmap(QPixmap("assets/polar_search_v1.png"))
        # self.message.setGeometry(60, 10, 381, 50)

        # Exit button
        self.exitButton = PicButton(pixmap=QPixmap("assets/exitbutton.png"), pixmap_hover=QPixmap("assets/exitbutton_hover.png"), pixmap_pressed=QPixmap("assets/exitbutton_hover.png"), parent=self.centralwidget)
        self.exitButton.setGeometry(QRect(870, 10, 20, 20))

        # Close button
        self.closeButton = PicButton(pixmap=QPixmap("assets/closebutton.png"), pixmap_hover=QPixmap("assets/closebutton_hover.png"), pixmap_pressed=QPixmap("assets/closebutton_pressed.png"), parent=self.centralwidget)
        self.closeButton.setGeometry(QRect(845, 10, 20, 20))

        # Add file button
        self.addFileButton = QPushButton(self.centralwidget)
        self.addFileButton.setText("Добавить")
        self.addFileButton.setFont(QFont("Arial"))
        self.addFileButton.setGeometry(500, 500, 80, 20)
        self.addFileButton.setStyleSheet('''
            QPushButton {background: rgb(204, 204, 204);
            border-radius: 10px;}
            QPushButton:hover {background: grey;}
            QPushButton:pressed {color: white;}
        ''')

        self.removeFileButton = QPushButton(self.centralwidget)
        self.removeFileButton.setText("Удалить")
        self.removeFileButton.setFont(QFont("Arial"))
        self.removeFileButton.setGeometry(590, 500, 80, 20)
        self.removeFileButton.setStyleSheet('''
            QPushButton {background: rgb(204, 204, 204);
            border-radius: 10px;}
            QPushButton:hover {background: grey;}
            QPushButton:pressed {color: white;}
        ''')

        # File list view
        self.fileList = QListWidget(self.centralwidget)
        self.fileList.setGeometry(QRect(500, 80, 350, 400))
        self.fileList.setStyleSheet('''
            background: rgb(204, 204, 204);
            padding: 10px;
            font: 15px;
        ''')

        '''Test items'''
        # self.testItem = QListWidgetItem()
        # self.testItem.setIcon(QIcon("assets/folder.png"))
        # self.testItem.setText("Batch folder")
        # self.testItem.setFont(QFont("Arial"))
        # self.fileList.addItem(self.testItem)
        #
        # self.testItem2 = QListWidgetItem()
        # self.testItem2.setIcon(QIcon("assets/picture.png"))
        # self.testItem2.setText("Batch folder")
        # self.testItem2.setFont(QFont("Arial"))
        # self.fileList.addItem(self.testItem2)


        # # Search button
        # self.searchButton = PicButton(pixmap=QPixmap("assets/search.png"), pixmap_hover=QPixmap("assets/search_hover.png"), pixmap_pressed=QPixmap("assets/search_pressed.png"), parent=self.centralwidget)
        # self.searchButton.setGeometry(QRect(10, 540, 50, 50))
        #
        # self.uploadButton = PicButton(pixmap=QPixmap("assets/upload.png"), pixmap_hover=QPixmap("assets/upload_hover.png"), pixmap_pressed=QPixmap("assets/upload_pressed.png"), parent=self.centralwidget)
        # self.uploadButton.setGeometry(QRect(70, 540, 50, 50))

        self.folderPaths = {}

        self.load_functionality()

    def load_functionality(self):
        self.exitButton.clicked.connect(sys.exit)
        self.closeButton.clicked.connect(self.showMinimized)
        self.addFileButton.clicked.connect(self.addFolder)
        self.removeFileButton.clicked.connect(self.removeFolder)

    def addFolder(self):
        text = str(QFileDialog.getExistingDirectory(self, 'Select Folder'))
        item = QListWidgetItem()
        item.setText(text.split("/")[-1])
        item.setIcon(QIcon("assets/folder.png"))
        self.fileList.addItem(item)
        self.folderPaths[text.split("/")[-1]] = text

    def removeFolder(self):
        selected = self.fileList.selectedItems()

        if not selected:
            return

        for item in selected:
            self.fileList.takeItem(self.fileList.row(item))
            del self.folderPaths[item.text()]

    def show_start_in_status_menu(self, file_name):
        current_time = str(datetime.now().time())
        current_time = current_time[:current_time.find('.')]
        answer = """< body style = " font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;" >
        < p style = " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;" >
        < span style = " color:#ffffff;" >[{}]Детекция медведей в папке - {}...< / span >< / p >< / body >""".format(
            current_time, file_name)
        self.textBrowser.append(answer)

    def show_data_in_status_menu(self, counter):
        current_time = str(datetime.now().time())
        current_time = current_time[:current_time.find('.')]
        answer = """< body style = " font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;" >
        < p style = " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;" >
        < span style = " color:#ffffff;" >[{}]Найдено: {} < / span >< / p >< / body >""".format(current_time, counter)
        self.textBrowser.append(answer)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if Qt.LeftButton and self.moveFlag:
                self.move(event.globalPos() - self.movePosition)
                self.setCursor(QCursor(Qt.ClosedHandCursor))
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, QMouseEvent):
        self.moveFlag = False
        self.setCursor(Qt.ArrowCursor)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())