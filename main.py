import sys
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

        # Top left name
        self.message = QLabel(self.centralwidget)
        self.message.setPixmap(QPixmap("assets/polar_search_v1.png"))
        self.message.setGeometry(60, 10, 381, 50)

        # Exit button
        self.exitButton = PicButton(pixmap=QPixmap("assets/exitbutton.png"), pixmap_hover=QPixmap("assets/exitbutton_hover.png"), pixmap_pressed=QPixmap("assets/exitbutton_hover.png"), parent=self.centralwidget)
        self.exitButton.setGeometry(QRect(870, 10, 20, 20))

        # Close button
        self.closeButton = PicButton(pixmap=QPixmap("assets/closebutton.png"), pixmap_hover=QPixmap("assets/closebutton_hover.png"), pixmap_pressed=QPixmap("assets/closebutton_pressed.png"), parent=self.centralwidget)
        self.closeButton.setGeometry(QRect(845, 10, 20, 20))

        # Search button
        self.searchButton = PicButton(pixmap=QPixmap("assets/search.png"), pixmap_hover=QPixmap("assets/search_hover.png"), pixmap_pressed=QPixmap("assets/search_pressed.png"), parent=self.centralwidget)
        self.searchButton.setGeometry(QRect(10, 540, 50, 50))

        self.uploadButton = PicButton(pixmap=QPixmap("assets/upload.png"), pixmap_hover=QPixmap("assets/upload_hover.png"), pixmap_pressed=QPixmap("assets/upload_pressed.png"), parent=self.centralwidget)
        self.uploadButton.setGeometry(QRect(70, 540, 50, 50))

        self.load_functionality()

    def load_functionality(self):
        self.exitButton.clicked.connect(sys.exit)
        self.closeButton.clicked.connect(self.showMinimized)

    def right_menu(self, pos):
        menu = QMenu()

        # Add menu options
        exit_option = menu.addAction('Exit')

        # Menu option events
        exit_option.triggered.connect(lambda: exit())

        # Position
        menu.exec_(self.mapToGlobal(pos))

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