_translate = QCoreApplication.translate
radius = 15
self.textBrowser = QTextBrowser(self.centralwidget)
self.textBrowser.setGeometry(QRect(50, 80, 350, 450))
self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                               "font: 12pt \"Consolas\";\n"
                               "border-top-left-radius:{0}px;\n"
                               "border-bottom-left-radius:{0}px;\n"
                               "border-top-right-radius:{0}px;\n"
                               "border-bottom-right-radius:{0}px;\n"
                               "padding: 10px".format(radius)
                               )
self.textBrowser.setObjectName("textBrowser")
