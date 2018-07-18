# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloaderForRedditGUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/Images/RedditDownloaderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vert_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.vert_splitter.setOrientation(QtCore.Qt.Vertical)
        self.vert_splitter.setHandleWidth(10)
        self.vert_splitter.setObjectName("vert_splitter")
        self.horz_splitter = QtWidgets.QSplitter(self.vert_splitter)
        self.horz_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.horz_splitter.setObjectName("horz_splitter")
        self.user_list_view = QtWidgets.QListView(self.horz_splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_list_view.setFont(font)
        self.user_list_view.setObjectName("user_list_view")
        self.subreddit_list_view = QtWidgets.QListView(self.horz_splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subreddit_list_view.setFont(font)
        self.subreddit_list_view.setObjectName("subreddit_list_view")
        self.layoutWidget = QtWidgets.QWidget(self.vert_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.subreddit_list_combo = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subreddit_list_combo.setFont(font)
        self.subreddit_list_combo.setObjectName("subreddit_list_combo")
        self.gridLayout_2.addWidget(self.subreddit_list_combo, 0, 6, 1, 1)
        self.add_user_button = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_user_button.setFont(font)
        self.add_user_button.setObjectName("add_user_button")
        self.gridLayout_2.addWidget(self.add_user_button, 0, 0, 1, 1)
        self.remove_user_button = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_user_button.setFont(font)
        self.remove_user_button.setObjectName("remove_user_button")
        self.gridLayout_2.addWidget(self.remove_user_button, 0, 1, 1, 1)
        self.remove_subreddit_button = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_subreddit_button.setFont(font)
        self.remove_subreddit_button.setObjectName("remove_subreddit_button")
        self.gridLayout_2.addWidget(self.remove_subreddit_button, 0, 8, 1, 1)
        self.add_subreddit_button = QtWidgets.QToolButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_subreddit_button.setFont(font)
        self.add_subreddit_button.setObjectName("add_subreddit_button")
        self.gridLayout_2.addWidget(self.add_subreddit_button, 0, 7, 1, 1)
        self.download_users_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_users_checkbox.sizePolicy().hasHeightForWidth())
        self.download_users_checkbox.setSizePolicy(sizePolicy)
        self.download_users_checkbox.setMaximumSize(QtCore.QSize(16777201, 16777215))
        self.download_users_checkbox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_users_checkbox.setFont(font)
        self.download_users_checkbox.setObjectName("download_users_checkbox")
        self.gridLayout_2.addWidget(self.download_users_checkbox, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.user_lists_combo = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_lists_combo.setFont(font)
        self.user_lists_combo.setObjectName("user_lists_combo")
        self.gridLayout_2.addWidget(self.user_lists_combo, 0, 2, 1, 1)
        self.download_subreddit_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_subreddit_checkbox.setFont(font)
        self.download_subreddit_checkbox.setObjectName("download_subreddit_checkbox")
        self.gridLayout_2.addWidget(self.download_subreddit_checkbox, 0, 5, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.output_box = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_box.setFont(font)
        self.output_box.setObjectName("output_box")
        self.gridLayout_5.addWidget(self.output_box, 1, 0, 1, 1)
        self.download_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_button.setFont(font)
        self.download_button.setObjectName("download_button")
        self.gridLayout_5.addWidget(self.download_button, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 0, 1, 9)
        self.gridLayout.addWidget(self.vert_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLists = QtWidgets.QMenu(self.menubar)
        self.menuLists.setObjectName("menuLists")
        self.menuUser_Finder = QtWidgets.QMenu(self.menubar)
        self.menuUser_Finder.setObjectName("menuUser_Finder")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.view_sort_lists_by = QtWidgets.QMenu(self.menuView)
        self.view_sort_lists_by.setObjectName("view_sort_lists_by")
        self.view_sort_order = QtWidgets.QMenu(self.menuView)
        self.view_sort_order.setObjectName("view_sort_order")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file_add_user_list = QtWidgets.QAction(MainWindow)
        self.file_add_user_list.setObjectName("file_add_user_list")
        self.file_add_subreddit_list = QtWidgets.QAction(MainWindow)
        self.file_add_subreddit_list.setObjectName("file_add_subreddit_list")
        self.file_save = QtWidgets.QAction(MainWindow)
        self.file_save.setObjectName("file_save")
        self.file_remove_user_list = QtWidgets.QAction(MainWindow)
        self.file_remove_user_list.setObjectName("file_remove_user_list")
        self.file_remove_subreddit_list = QtWidgets.QAction(MainWindow)
        self.file_remove_subreddit_list.setObjectName("file_remove_subreddit_list")
        self.file_open_settings = QtWidgets.QAction(MainWindow)
        self.file_open_settings.setObjectName("file_open_settings")
        self.file_exit = QtWidgets.QAction(MainWindow)
        self.file_exit.setObjectName("file_exit")
        self.file_failed_download_list = QtWidgets.QAction(MainWindow)
        self.file_failed_download_list.setObjectName("file_failed_download_list")
        self.file_open_user_finder = QtWidgets.QAction(MainWindow)
        self.file_open_user_finder.setObjectName("file_open_user_finder")
        self.file_last_downloaded_list = QtWidgets.QAction(MainWindow)
        self.file_last_downloaded_list.setObjectName("file_last_downloaded_list")
        self.file_unfinished_downloads = QtWidgets.QAction(MainWindow)
        self.file_unfinished_downloads.setObjectName("file_unfinished_downloads")
        self.file_imgur_credits = QtWidgets.QAction(MainWindow)
        self.file_imgur_credits.setObjectName("file_imgur_credits")
        self.file_about = QtWidgets.QAction(MainWindow)
        self.file_about.setObjectName("file_about")
        self.file_user_list_count = QtWidgets.QAction(MainWindow)
        self.file_user_list_count.setObjectName("file_user_list_count")
        self.file_subreddit_list_count = QtWidgets.QAction(MainWindow)
        self.file_subreddit_list_count.setObjectName("file_subreddit_list_count")
        self.file_user_manual = QtWidgets.QAction(MainWindow)
        self.file_user_manual.setObjectName("file_user_manual")
        self.file_check_for_updates = QtWidgets.QAction(MainWindow)
        self.file_check_for_updates.setObjectName("file_check_for_updates")
        self.view_sort_list_by_name = QtWidgets.QAction(MainWindow)
        self.view_sort_list_by_name.setCheckable(True)
        self.view_sort_list_by_name.setObjectName("view_sort_list_by_name")
        self.view_sort_list_by_date_added = QtWidgets.QAction(MainWindow)
        self.view_sort_list_by_date_added.setCheckable(True)
        self.view_sort_list_by_date_added.setObjectName("view_sort_list_by_date_added")
        self.view_sort_list_by_number_of_downloads = QtWidgets.QAction(MainWindow)
        self.view_sort_list_by_number_of_downloads.setCheckable(True)
        self.view_sort_list_by_number_of_downloads.setObjectName("view_sort_list_by_number_of_downloads")
        self.view_order_by_ascending = QtWidgets.QAction(MainWindow)
        self.view_order_by_ascending.setCheckable(True)
        self.view_order_by_ascending.setObjectName("view_order_by_ascending")
        self.view_order_by_descending = QtWidgets.QAction(MainWindow)
        self.view_order_by_descending.setCheckable(True)
        self.view_order_by_descending.setObjectName("view_order_by_descending")
        self.file_open_save_file_location = QtWidgets.QAction(MainWindow)
        self.file_open_save_file_location.setObjectName("file_open_save_file_location")
        self.file_import_save_file = QtWidgets.QAction(MainWindow)
        self.file_import_save_file.setObjectName("file_import_save_file")
        self.menuFile.addAction(self.file_open_settings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.file_save)
        self.menuFile.addAction(self.file_import_save_file)
        self.menuFile.addAction(self.file_open_save_file_location)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.file_exit)
        self.menuLists.addAction(self.file_add_user_list)
        self.menuLists.addAction(self.file_add_subreddit_list)
        self.menuLists.addSeparator()
        self.menuLists.addAction(self.file_remove_user_list)
        self.menuLists.addAction(self.file_remove_subreddit_list)
        self.menuLists.addSeparator()
        self.menuLists.addAction(self.file_failed_download_list)
        self.menuLists.addAction(self.file_unfinished_downloads)
        self.menuLists.addAction(self.file_last_downloaded_list)
        self.menuLists.addSeparator()
        self.menuLists.addAction(self.file_user_list_count)
        self.menuLists.addAction(self.file_subreddit_list_count)
        self.menuUser_Finder.addAction(self.file_open_user_finder)
        self.menuHelp.addAction(self.file_imgur_credits)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.file_user_manual)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.file_check_for_updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.file_about)
        self.view_sort_lists_by.addAction(self.view_sort_list_by_name)
        self.view_sort_lists_by.addAction(self.view_sort_list_by_date_added)
        self.view_sort_lists_by.addAction(self.view_sort_list_by_number_of_downloads)
        self.view_sort_order.addAction(self.view_order_by_ascending)
        self.view_sort_order.addAction(self.view_order_by_descending)
        self.menuView.addAction(self.view_sort_lists_by.menuAction())
        self.menuView.addAction(self.view_sort_order.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuLists.menuAction())
        self.menubar.addAction(self.menuUser_Finder.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloader for Reddit"))
        self.subreddit_list_combo.setToolTip(_translate("MainWindow", "Current subreddit list"))
        self.add_user_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add user to selected list</p></body></html>"))
        self.add_user_button.setText(_translate("MainWindow", "+"))
        self.remove_user_button.setToolTip(_translate("MainWindow", "Remove user from selected list"))
        self.remove_user_button.setText(_translate("MainWindow", "-"))
        self.remove_subreddit_button.setToolTip(_translate("MainWindow", "Remove subreddit from selected list"))
        self.remove_subreddit_button.setText(_translate("MainWindow", "-"))
        self.add_subreddit_button.setToolTip(_translate("MainWindow", "Add subreddit to selected list"))
        self.add_subreddit_button.setText(_translate("MainWindow", "+"))
        self.download_users_checkbox.setToolTip(_translate("MainWindow", "Download from User list"))
        self.download_users_checkbox.setText(_translate("MainWindow", "Download Users"))
        self.user_lists_combo.setToolTip(_translate("MainWindow", "Current user list"))
        self.download_subreddit_checkbox.setToolTip(_translate("MainWindow", "Download from Subreddit list"))
        self.download_subreddit_checkbox.setText(_translate("MainWindow", "Download Subreddits"))
        self.download_button.setToolTip(_translate("MainWindow", "Download selected user or subreddit list"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLists.setTitle(_translate("MainWindow", "Lists"))
        self.menuUser_Finder.setTitle(_translate("MainWindow", "User Finder"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.view_sort_lists_by.setTitle(_translate("MainWindow", "Sort Lists By"))
        self.view_sort_order.setTitle(_translate("MainWindow", "Sort Order"))
        self.file_add_user_list.setText(_translate("MainWindow", "Add User List"))
        self.file_add_subreddit_list.setText(_translate("MainWindow", "Add Subreddit List"))
        self.file_save.setText(_translate("MainWindow", "Save"))
        self.file_remove_user_list.setText(_translate("MainWindow", "Remove User List"))
        self.file_remove_subreddit_list.setText(_translate("MainWindow", "Remove Subreddit List"))
        self.file_open_settings.setText(_translate("MainWindow", "Settings"))
        self.file_exit.setText(_translate("MainWindow", "Exit"))
        self.file_failed_download_list.setText(_translate("MainWindow", "Failed Download List"))
        self.file_failed_download_list.setToolTip(_translate("MainWindow", "Display the failed download list for the last download session"))
        self.file_open_user_finder.setText(_translate("MainWindow", "Open User Finder"))
        self.file_last_downloaded_list.setText(_translate("MainWindow", "Last Downloaded List"))
        self.file_unfinished_downloads.setText(_translate("MainWindow", "Unfinished Downloads"))
        self.file_imgur_credits.setText(_translate("MainWindow", "Imgur Credits"))
        self.file_about.setText(_translate("MainWindow", "About"))
        self.file_user_list_count.setText(_translate("MainWindow", "User List Count:"))
        self.file_subreddit_list_count.setText(_translate("MainWindow", "Subreddit List Count:"))
        self.file_user_manual.setText(_translate("MainWindow", "User Manual"))
        self.file_check_for_updates.setText(_translate("MainWindow", "Check For Update"))
        self.view_sort_list_by_name.setText(_translate("MainWindow", "Name"))
        self.view_sort_list_by_date_added.setText(_translate("MainWindow", "Date Added"))
        self.view_sort_list_by_number_of_downloads.setText(_translate("MainWindow", "Number of Downloads"))
        self.view_order_by_ascending.setText(_translate("MainWindow", "Ascending"))
        self.view_order_by_descending.setText(_translate("MainWindow", "Descending"))
        self.file_open_save_file_location.setText(_translate("MainWindow", "Open Save Location"))
        self.file_import_save_file.setText(_translate("MainWindow", "Import Save File"))

