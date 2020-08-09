import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import webbrowser
import os
import secrets
from github import Github
from github import InputGitTreeElement
import glob


class Controller:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.main = Main()
        self.connect_event()
        os.system("jupyter notebook --notebook-dir= /home/$USER/ &")
        self.repo_url = None
        self.dirName = None
        sys.exit(app.exec_())

    def connect_event(self):
        self.main.reload.triggered.connect(self.reload)
        self.main.back.triggered.connect(self.back)
        self.main.forward.triggered.connect(self.forward)
        self.main.plus.triggered.connect(self.plus_home)
        self.main.home.triggered.connect(self.main.navigate_home)
        self.main.pushButton.clicked.connect(self.open_jupyter)
        self.main.actionOpen.triggered.connect(self.open_file)
        self.main.actionexit.triggered.connect(self.exit)
        self.main.actionHelp.triggered.connect(self.open_help)
        self.main.actionAbout_Us.triggered.connect(self.about_us)
        self.main.actionHelpJup.triggered.connect(self.jupyter_help)
        self.main.actionPush_To_Github.triggered.connect(self.push_to_github)
        self.main.actionClone_from_Github.triggered.connect(self.clone_from_github)

        # self.main.pushButton_2.clicked.connect(self.open_github)
        # self.main.pushButton_3.clicked.connect(self.plus_home)
        # self.main.pushButton_4.clicked.connect(self.open_github_classroom)
        self.main.jupyter.triggered.connect(self.open_jupyter)
        self.main.github.triggered.connect(self.open_github)
        self.main.github_class.triggered.connect(self.open_github_classroom)
        self.main.actionCreate_2.triggered.connect(self.clone_from_github)
        self.main.actionUpdate_2.triggered.connect(self.push_to_github)
        self.main.actionInfo.triggered.connect(self.info)
        self.main.actionExport.triggered.connect(self.export)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path = str(os.environ['HOME'])
        fileName, _ = QFileDialog.getOpenFileName(self.main, "All files", path,
                                                  "All Files (*);;Python Files (*.py);;Notebook Files (*.ipynb)",
                                                  options=options)
        if fileName:
            self.main.add_new_tab(QUrl("file://" + "/" + str(fileName)))

    def info(self):
        QMessageBox.warning(self.main, 'Warning !!', "\nUnder Development !!")

    def export(self):
        QMessageBox.warning(self.main, 'Warning !!', "\nUnder Development !!")

    def open_folder(self):
        path = str(os.environ['HOME'])
        self.dirName = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select project folder:', path,
                                                                  QtWidgets.QFileDialog.ShowDirsOnly)
        if self.dirName:
            self.dir_select.setText(self.dirName)

    def push_to_github(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.setWindowTitle("Upload repository to GitHub")
        self.dialog.setMinimumWidth(500)
        self.dialog.setFixedHeight(150)

        VLayout = QtWidgets.QVBoxLayout()
        Hlayout1 = QtWidgets.QHBoxLayout()
        Hlayout3 = QtWidgets.QHBoxLayout()

        label = QtWidgets.QLabel(self.dialog)
        label.setText(" WorkDir      : ")

        button = QtWidgets.QPushButton()
        button.setText("Open")
        button.setObjectName("button")
        button.clicked.connect(self.open_folder)

        self.dir_select = QtWidgets.QLineEdit()
        self.dir_select.setObjectName("dir_select")
        path = str(os.environ['HOME'])
        self.dir_select.setText(path)

        add = QtWidgets.QPushButton()
        add.setObjectName("add_link")
        add.setText('Push')
        add.clicked.connect(self.push_submit)

        cancel = QtWidgets.QPushButton()
        cancel.setObjectName("cancel_link")
        cancel.setText('Cancel')
        cancel.clicked.connect(self.dialog.reject)

        Hlayout1.addWidget(label)
        Hlayout1.addWidget(self.dir_select)
        Hlayout1.addWidget(button)

        Hlayout3.addStretch()
        Hlayout3.addWidget(add, 0, QtCore.Qt.AlignRight)
        Hlayout3.addWidget(cancel, 0, QtCore.Qt.AlignRight)

        VLayout.addLayout(Hlayout1, 1)
        VLayout.addLayout(Hlayout3, 2)
        self.dialog.setLayout(VLayout)
        self.dialog.exec()

    def push_submit(self):
        self.dirName = self.dir_select.text()
        if self.dirName is None:
            QMessageBox.warning(self.main, 'Warning !!', "\nSelect folder you want to push to github repository !!")
        else:
            path = self.dirName

            dialog = QtWidgets.QDialog()
            dialog.setWindowTitle("Setup Github Account")
            dialog.setMinimumWidth(250)
            dialog.setFixedHeight(120)

            VLayout = QtWidgets.QVBoxLayout()
            Hlayout1 = QtWidgets.QHBoxLayout()
            Hlayout2 = QtWidgets.QHBoxLayout()
            Hlayout3 = QtWidgets.QHBoxLayout()

            label = QtWidgets.QLabel(dialog)
            label.setText("User Name : ")
            label_1 = QtWidgets.QLabel(dialog)
            label_1.setText("   Password : ")

            username = QtWidgets.QLineEdit()
            password = QtWidgets.QLineEdit()

            Ok = QtWidgets.QPushButton()
            Ok.setObjectName("Ok")
            Ok.setText('Ok')
            Ok.clicked.connect(dialog.accept)

            cancel = QtWidgets.QPushButton()
            cancel.setObjectName("cancel")
            cancel.setText('Cancel')
            cancel.clicked.connect(dialog.reject)

            Hlayout1.addWidget(label)
            Hlayout1.addWidget(username)

            Hlayout2.addWidget(label_1)
            Hlayout2.addWidget(password)

            Hlayout3.addStretch()
            Hlayout3.addWidget(Ok, 0, QtCore.Qt.AlignRight)
            Hlayout3.addWidget(cancel, 0, QtCore.Qt.AlignRight)

            VLayout.addLayout(Hlayout1, 1)
            VLayout.addLayout(Hlayout2, 2)
            VLayout.addLayout(Hlayout3, 3)
            dialog.setLayout(VLayout)
            dialog.exec()
            token = secrets.token_hex(5)
            user = str(username.text())
            passwd = str(password.text())
            if user and passwd != "":
                os.chdir(path)
                pwd = str(os.getcwd())
                repo_name = path.rstrip(os.sep)
                repo_name = os.path.basename(repo_name)
                try:
                    g = Github(user, passwd)
                    repo = g.get_user().get_repo(repo_name)
                    file = glob.glob(pwd + '/*')
                    commit_message = str(token)
                    file_name = [os.path.basename(x) for x in glob.glob(path + '/*')]
                    master_ref = repo.get_git_ref('heads/master')
                    master_sha = master_ref.object.sha
                    base_tree = repo.get_git_tree(master_sha)
                    element_list = list()
                    for i, entry in enumerate(file):
                        with open(entry) as input_file:
                            data = input_file.read()
                        if entry.endswith('.png'):
                            data = base64.b64encode(data)
                        element = InputGitTreeElement(file_name[i], '100644', 'blob', data)
                        element_list.append(element)
                    tree = repo.create_git_tree(element_list, base_tree)
                    print(tree)
                    if tree.sha != base_tree.sha:
                        parent = repo.get_git_commit(master_sha)
                        commit = repo.create_git_commit(commit_message, tree, [parent])
                        master_ref.edit(commit.sha)
                    self.dialog.close()
                    buttonReply = QMessageBox.information(self.main, 'Information !!', "Uploaded to github repository "
                                                                                       "\n\nis succeed !!",
                                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if buttonReply == QMessageBox.Yes:
                        self.main.add_new_tab(QtCore.QUrl("https://github.com/" + user + "/" + repo_name))

                except:
                    QMessageBox.warning(self.main, 'Warning !!', "Error git authentication !!!! \n\n"
                                                                 " 1. Make sure you typing correct username and password \n"
                                                                 " 2. Make sure You're repository already connect to github.\n"
                                                                 " plese ref:https://docs.github.com/en/github/using-git/adding-a-remote ")

    def clone(self):
        self.repo_url = self.repo_link.text()
        self.dirName = self.dir_select.text()
        if self.dirName is None:
            QMessageBox.warning(self.main, 'Warning !!', "\nSelect folder you want to push to github repository !!")
        elif self.repo_url is "":
            QMessageBox.warning(self.main, 'Warning !!', "\nPlease write Github Repository Url !!")
        else:
            os.chdir(self.dirName)
            self.dialog_2.accept()
            path = self.repo_url
            path = path.rstrip(os.sep)
            path = os.path.basename(path)
            pwd = os.getcwd()
            if os.path.isdir(path):
                buttonReply = QMessageBox.question(self.main, 'File exist !!', "File already exist !!!",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.main.add_new_tab(QtCore.QUrl("http://localhost:8888/tree/" + str(pwd) + '/' + str(path)))

            elif os.path.isdir(path[:-4]):
                buttonReply = QMessageBox.question(self.main, 'File exist !!', "File already exist !!!",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.main.add_new_tab(QtCore.QUrl("http://localhost:8888/tree/" + str(pwd) + '/' + str(path[:-4])))

            else:
                os.system("git clone " + str(self.repo_url))
                if os.path.isdir(path):
                    buttonReply = QMessageBox.question(self.main, 'Clone success !!', "cloning repository is finish !!!"
                                                                                      "\n you want to open the file ?",
                                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if buttonReply == QMessageBox.Yes:
                        self.main.add_new_tab(QtCore.QUrl("http://localhost:8888/tree/" + str(path)))

                elif os.path.isdir(path[:-4]):
                    buttonReply = QMessageBox.question(self.main, 'Clone success !!', "cloning repository is finish !!!"
                                                                                      "\n you want to open the file ?",
                                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if buttonReply == QMessageBox.Yes:
                        self.main.add_new_tab(QtCore.QUrl("http://localhost:8888/tree/" + str(path[:-4])))

    def clone_from_github(self):
        self.dialog_2 = QtWidgets.QDialog()
        self.dialog_2.setWindowTitle("Clone Repository From Github")
        self.dialog_2.setMinimumWidth(550)
        self.dialog_2.setFixedHeight(180)

        VLayout = QtWidgets.QVBoxLayout()
        Hlayout1 = QtWidgets.QHBoxLayout()
        Hlayout2 = QtWidgets.QHBoxLayout()
        Hlayout3 = QtWidgets.QHBoxLayout()

        label = QtWidgets.QLabel(self.dialog_2)
        label.setText(" WorkDir      : ")
        label_1 = QtWidgets.QLabel(self.dialog_2)
        label_1.setText("Github URL : ")

        button = QtWidgets.QPushButton()
        button.setText("Open")
        button.setObjectName("button")
        button.clicked.connect(self.open_folder)

        self.dir_select = QtWidgets.QLineEdit()
        self.dir_select.setObjectName("dir_select")
        path = str(os.environ['HOME'])
        self.dir_select.setText(path)

        self.repo_link = QtWidgets.QLineEdit()

        add = QtWidgets.QPushButton()
        add.setObjectName("add_link")
        add.setText('clone')
        add.clicked.connect(self.clone)

        cancel = QtWidgets.QPushButton()
        cancel.setObjectName("cancel_link")
        cancel.setText('Cancel')
        cancel.clicked.connect(self.dialog_2.reject)

        Hlayout1.addWidget(label)
        Hlayout1.addWidget(self.dir_select)
        Hlayout1.addWidget(button)

        Hlayout2.addWidget(label_1)
        Hlayout2.addWidget(self.repo_link)

        Hlayout3.addStretch()
        # Hlayout3.addWidget(Change_url, 0, QtCore.Qt.AlignRight)
        Hlayout3.addWidget(add, 0, QtCore.Qt.AlignRight)
        Hlayout3.addWidget(cancel, 0, QtCore.Qt.AlignRight)

        VLayout.addLayout(Hlayout1, 1)
        VLayout.addLayout(Hlayout2, 2)
        VLayout.addLayout(Hlayout3, 3)
        self.dialog_2.setLayout(VLayout)
        self.dialog_2.exec()

    def open_jupyter(self):
        self.main.add_new_tab(QtCore.QUrl('http://localhost:8888/tree?'), 'Loading ...')
        self.main.urlbar.setText('http://localhost:8888/tree?')

    def plus_home(self):
        if self.main.tabs.count() < 1:
            pass
        else:
            self.main.add_new_tab(QtCore.QUrl('http://www.google.com.tw'), 'Homepage')

    def jupyter_help(self):
        self.main.add_new_tab(QtCore.QUrl("https://jupyter-notebook.readthedocs.io/en/stable/notebook.html"))

    def reload(self):
        if self.main.tabs.count() < 1:
            pass
        else:
            self.main.tabs.currentWidget().reload()

    def back(self):
        if self.main.tabs.count() < 1:
            pass
        else:
            self.main.tabs.currentWidget().back()

    def forward(self):
        if self.main.tabs.count() < 1:
            pass
        else:
            self.main.tabs.currentWidget().forward()

    def open_github(self):
        self.main.add_new_tab(QtCore.QUrl("https://github.com/"), 'Loading ...')

    def open_github_classroom(self):
        self.main.add_new_tab(QtCore.QUrl("https://classroom.github.com/"), 'Loading ...')

    def about_us(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText("MOIL \n\n\nOmnidirectional Imaging & Surveillance Lab\n\n"
                       "Ming Chi University of Technology\n\n"
                       "Contact: M07158031@o365.mcut.edu.tw")
        msgbox.setIconPixmap(QtGui.QPixmap('./assets/chess.jpg'))
        msgbox.exec()

    def open_help(self):
        url = "/assets/help.html"
        source = os.getcwd()
        self.main.add_new_tab(QUrl("file://" + str(source) + url))

    def exit(self):
        os.system("pkill -9 jupyter")
        self.main.close()


# if __name__ == '__main__':
#     window = Controller()
#     sys.exit(window.exec_())
