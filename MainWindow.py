from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os


class TabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)


class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.tab = self.parent()

    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = HtmlView(self.tab)
            i = self.tab.addTab(webView, "loading ...")
            self.tab.setCurrentIndex(i)
            webView.urlChanged.connect(lambda url, browser=webView:
                                       self.update_urlbar(url, browser))
            webView.loadFinished.connect(lambda _, i=i, browser=webView:
                                         self.tab.setTabText(i, browser.page().title()))
            return webView
        return QWebEngineView.createWindow(self, windowType)

    def update_urlbar(self, q, browser=None):
        if browser != self.tab.currentWidget():
            return


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.tabs = TabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setObjectName("tabs")
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.init_Ui()

    def init_Ui(self):
        self.statusBar()
        self.showMaximized()
        self.setMinimumSize(1200, 800)
        icon = QIcon()
        icon.addPixmap(QPixmap("assets/ico.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.centralwidget = QWidget(self)
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(320, 80, 1100, 110))
        font = QFont()
        font.setFamily("Noto Serif CJK KR")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(490, 180, 700, 40))
        font = QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(725, 530, 200, 50))
        font = QFont()
        font.setFamily("Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(700, 630, 250, 50))
        font = QFont()
        font.setFamily("Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QRect(675, 680, 300, 50))
        font = QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(QRect(725, 580, 200, 50))
        font = QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setGeometry(QRect(375, 540, 180, 170))
        self.label_7.setText("")
        self.label_7.setPixmap(QPixmap("assets/mcut.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setGeometry(QRect(1050, 550, 350, 140))
        self.label_8.setText("")
        self.label_8.setPixmap(QPixmap("assets/112-removebg.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(725, 275, 250, 150))
        icon_jupy = QIcon()
        icon_jupy.addPixmap(QPixmap("./assets/jupyter.png"),
                            QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon_jupy)
        self.pushButton.setIconSize(QSize(250, 150))
        self.pushButton.setObjectName("pushButton")

        # self.pushButton_2 = QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QRect(840, 250, 100, 50))
        # icon_2 = QIcon()
        # icon_2.addPixmap(QPixmap("./assets/github.png"),
        #                  QIcon.Normal, QIcon.Off)
        # self.pushButton_2.setIcon(icon_2)
        # self.pushButton_2.setIconSize(QSize(100, 50))
        # self.pushButton_2.setObjectName("pushButton_2")
        #
        # self.pushButton_3 = QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QRect(730, 250, 100, 50))
        # icon_3 = QIcon()
        # icon_3.addPixmap(QPixmap("./assets/google.png"),
        #                  QIcon.Normal, QIcon.Off)
        # self.pushButton_3.setIcon(icon_3)
        # self.pushButton_3.setIconSize(QSize(100, 50))
        # self.pushButton_3.setObjectName("pushButton_3")
        #
        # self.pushButton_4 = QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QRect(950, 250, 100, 50))
        # icon_4 = QIcon()
        # icon_4.addPixmap(QPixmap("./assets/github_class.png"),
        #                  QIcon.Normal, QIcon.Off)
        # self.pushButton_4.setIcon(icon_4)
        # self.pushButton_4.setIconSize(QSize(100, 50))
        # self.pushButton_4.setObjectName("pushButton_4")

        self.setCentralWidget(self.centralwidget)

        self.menuBar = QMenuBar(self.centralwidget)
        self.menuBar.setGeometry(QRect(0, 0, 1165, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuAssigment = QMenu(self.menuBar)
        self.menuAssigment.setObjectName("menuAssigment")
        # self.menuTeaching_Material = QMenu(self.menuBar)
        # self.menuTeaching_Material.setObjectName("menuTeaching_Material")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menuBar)

        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QAction(self)
        self.actionClose.setObjectName("actionClose")
        # self.actionCreate = QAction(self)
        # self.actionCreate.setObjectName("actionCreate")
        # self.actionUpdate = QAction(self)
        # self.actionUpdate.setObjectName("actionUpdate")
        self.actionCreate_2 = QAction(self)
        self.actionCreate_2.setObjectName("actionCreate_2")
        self.actionUpdate_2 = QAction(self)
        self.actionUpdate_2.setObjectName("actionUpdate_2")
        self.actionPush = QAction(self)
        self.actionPush.setObjectName("actionPush")
        self.actionPull = QAction(self)
        self.actionPull.setObjectName("actionPull")
        self.actionWeek_3 = QAction(self)
        self.actionWeek_3.setObjectName("actionWeek_3")
        self.actionWeek_4 = QAction(self)
        self.actionWeek_4.setObjectName("actionWeek_4")
        self.actionexit = QAction(self)
        self.actionexit.setObjectName("actionexit")
        self.actionInfo = QAction(self)
        self.actionInfo.setObjectName("actionInfo")
        self.actionNew = QAction(self)
        self.actionNew.setObjectName("actionNew")
        self.actionExport = QAction(self)

        # self.menuNew_File = QMenu(self.menuFile)
        # self.menuNew_File.setObjectName("menuNew_File")

        self.actionExport.setObjectName("actionExport")
        self.actionPush_To_Github = QAction(self)
        self.actionPush_To_Github.setObjectName("actionPush_To_Github")
        self.actionClone_from_Github = QAction(self)
        self.actionClone_from_Github.setObjectName("actionClone_from_Github")
        self.actionHelp = QAction(self)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_Us = QAction(self)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionHelpJup = QAction(self)
        self.actionHelpJup.setObjectName("actionHelpJup")

        # self.actionDirectory = QAction(self)
        # self.actionDirectory.setObjectName("actionDirectory")
        # self.actionHtml_file = QAction(self)
        # self.actionHtml_file.setObjectName("actionHtml_file")
        # self.actionPython_file = QAction(self)
        # self.actionPython_file.setObjectName("actionPython_file")
        # self.actionNotebook = QAction(self)
        # self.actionNotebook.setObjectName("actionNotebook")
        # self.actionTxt_file = QAction(self)
        # self.actionTxt_file.setObjectName("actionTxt_file")

        # self.menuTeaching_Material.addAction(self.actionCreate)
        # self.menuTeaching_Material.addAction(self.actionUpdate)

        self.menuAssigment.addAction(self.actionCreate_2)
        self.menuAssigment.addAction(self.actionUpdate_2)

        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionHelpJup)
        self.menuHelp.addAction(self.actionAbout_Us)

        self.menuFile.addAction(self.actionOpen)
        # self.menuFile.addAction(self.actionNew)

        # self.menuNew_File.addAction(self.actionDirectory)
        # self.menuNew_File.addAction(self.actionNotebook)
        # self.menuNew_File.addAction(self.actionPython_file)
        # self.menuNew_File.addAction(self.actionHtml_file)
        # self.menuNew_File.addAction(self.actionTxt_file)
        # self.menuFile.addAction(self.menuNew_File.menuAction())

        self.menuFile.addAction(self.actionInfo)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionPush_To_Github)
        self.menuFile.addAction(self.actionClone_from_Github)
        self.menuFile.addAction(self.actionexit)

        self.menuBar.addAction(self.menuFile.menuAction())
        # self.menuBar.addAction(self.menuTeaching_Material.menuAction())
        self.menuBar.addAction(self.menuAssigment.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.back = QAction(QIcon("./assets/left.png"), '&Click to go back')
        # self.back.setStatusTip('Click to go back')
        self.forward = QAction(QIcon("./assets/right.png"), '&Click to go forward')
        # self.forward.setStatusTip('Click to go forward')
        self.reload = QAction(QIcon("./assets/reload.png"), '&Reload this page')
        # self.reload.setStatusTip('Reload this page')
        self.home = QAction(QIcon("./assets/home.png"), '&Open the home page')
        # self.home.setStatusTip('Open the home page')
        self.plus = QAction(QIcon("./assets/plus.png"), '&New Tab')
        # self.plus.setStatusTip('Add new browser')
        self.urlbar = QLineEdit()
        # self.urlbar.setMinimumSize(300,30)
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        # self.search = QAction(QIcon("./assets/search.png"), '&search')
        # self.search.setStatusTip('search')
        self.jupyter = QAction(QIcon("./assets/jupyter.png"), '&Open Jupyter Notebook')
        # self.jupyter.setStatusTip('jupyter')
        self.github = QAction(QIcon("./assets/github_2.png"), '&Open GitHub')
        # self.github.setStatusTip('github')
        self.github_class = QAction(QIcon("./assets/github_class_2.png"), '&Open GitHub Classroom')
        # self.github_class.setStatusTip('github_class')

        self.toolBar = QToolBar(self)
        self.toolBar.addAction(self.jupyter)
        self.toolBar.addAction(self.github)
        self.toolBar.addAction(self.github_class)
        self.toolBar.addSeparator()
        self.toolBar.setObjectName("toolBar")
        self.toolBar.addAction(self.back)
        self.toolBar.addAction(self.forward)
        self.toolBar.addAction(self.reload)
        self.toolBar.addAction(self.home)
        self.toolBar.addAction(self.plus)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.urlbar)
        # self.toolBar.addAction(self.search)
        self.toolBar.addSeparator()
        # self.toolBar.setIconSize(  QSize(40, 20))

        self.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def tab_widget(self):
        self.setCentralWidget(self.tabs)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are You Sure to Quit?', QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            os.system("pkill -9 jupyter")
            event.accept()
        else:
            event.ignore()

    def add_new_tab(self, url=None, label="Blank"):
        self.tab_widget()
        if url is None:
            url = QUrl("http://www.google.com")
        browser = HtmlView(self.tabs)
        browser.setUrl(url)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(lambda url, browser=browser:
                                   self.update_urlbar(url, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def current_tab_changed(self, i):
        if i == -1:
            self.urlbar.setText("")
        else:
            qurl = self.tabs.currentWidget().url()
            self.update_urlbar(qurl, self.tabs.currentWidget())

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.tabs.currentWidget().setUrl(q)

    def navigate_home(self):
        if self.tabs.count() < 1:
            pass
        else:
            self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuAssigment.setTitle(_translate("MainWindow", "Assigment"))
        # self.menuTeaching_Material.setTitle(_translate("MainWindow", "Teaching Material"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        # self.actionCreate.setText(_translate("MainWindow", "Create"))
        # self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionCreate_2.setText(_translate("MainWindow", "Clone assignment"))
        self.actionUpdate_2.setText(_translate("MainWindow", "Upload assignment"))
        self.actionPush.setText(_translate("MainWindow", "Push"))
        self.actionPull.setText(_translate("MainWindow", "Pull"))
        self.actionWeek_3.setText(_translate("MainWindow", "Week_1"))
        self.actionWeek_4.setText(_translate("MainWindow", "Week_2"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        # self.menuNew_File.setTitle(_translate("MainWindow", "New ..."))
        # self.actionNew.setText(_translate("MainWindow", "New ..."))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionPush_To_Github.setText(_translate("MainWindow", "Push To Github"))
        self.actionClone_from_Github.setText(_translate("MainWindow", "Clone From Github"))
        self.actionHelp.setText(_translate("MainWindow", "Help ?"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.actionHelpJup.setText(_translate("MainWindow", "Jupyter Notebook"))
        self.label.setText(_translate("WebView", "Welcome To MOIL Portable Teaching Envirnment (PLE)"))
        self.label_2.setText(_translate("WebView", "Press the button to start Jupyter Notebook !!"))
        self.label_3.setText(_translate("MainWindow", "Design by:"))
        self.label_4.setText(_translate("MainWindow", "Under Guidance:"))
        self.label_5.setText(_translate("MainWindow", "Prof. Chuang-Jan Chang"))
        self.label_6.setText(_translate("MainWindow", "Haryanto"))

        # self.actionDirectory.setText(_translate("MainWindow", "Directory"))
        # self.actionHtml_file.setText(_translate("MainWindow", "Html file"))
        # self.actionPython_file.setText(_translate("MainWindow", "Python file"))
        # self.actionNotebook.setText(_translate("MainWindow", "Notebook"))
        # self.actionTxt_file.setText(_translate("MainWindow", "Txt file"))
# if __name__ == "__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#     main = Main()
#     # main.show()
#     sys.exit(app.exec_())
