# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RedditObjectSettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RedditObjectSettingsDialog(object):
    def setupUi(self, RedditObjectSettingsDialog):
        RedditObjectSettingsDialog.setObjectName("RedditObjectSettingsDialog")
        RedditObjectSettingsDialog.resize(764, 843)
        font = QtGui.QFont()
        font.setPointSize(10)
        RedditObjectSettingsDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Images/settings_three_gears.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RedditObjectSettingsDialog.setWindowIcon(icon)
        RedditObjectSettingsDialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(RedditObjectSettingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.restore_defaults_button = QtWidgets.QPushButton(RedditObjectSettingsDialog)
        self.restore_defaults_button.setObjectName("restore_defaults_button")
        self.gridLayout.addWidget(self.restore_defaults_button, 1, 0, 1, 1)
        self.view_downloads_button = QtWidgets.QPushButton(RedditObjectSettingsDialog)
        self.view_downloads_button.setObjectName("view_downloads_button")
        self.gridLayout.addWidget(self.view_downloads_button, 1, 1, 1, 1)
        self.save_cancel_buton_box = QtWidgets.QDialogButtonBox(RedditObjectSettingsDialog)
        self.save_cancel_buton_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.save_cancel_buton_box.setObjectName("save_cancel_buton_box")
        self.gridLayout.addWidget(self.save_cancel_buton_box, 1, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(RedditObjectSettingsDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.object_list_widget = QtWidgets.QListWidget(self.splitter)
        self.object_list_widget.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.object_list_widget.setFont(font)
        self.object_list_widget.setObjectName("object_list_widget")
        self.stacked_widget = QtWidgets.QStackedWidget(self.splitter)
        self.stacked_widget.setObjectName("stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.item_added_label = QtWidgets.QLabel(self.page)
        self.item_added_label.setObjectName("item_added_label")
        self.gridLayout_2.addWidget(self.item_added_label, 3, 0, 1, 3)
        self.total_downloads_title_label = QtWidgets.QLabel(self.page)
        self.total_downloads_title_label.setObjectName("total_downloads_title_label")
        self.gridLayout_2.addWidget(self.total_downloads_title_label, 2, 0, 1, 1)
        self.total_downloads_label = QtWidgets.QLabel(self.page)
        self.total_downloads_label.setObjectName("total_downloads_label")
        self.gridLayout_2.addWidget(self.total_downloads_label, 2, 1, 1, 1)
        self.item_display_list_label = QtWidgets.QLabel(self.page)
        self.item_display_list_label.setObjectName("item_display_list_label")
        self.gridLayout_2.addWidget(self.item_display_list_label, 0, 0, 1, 1)
        self.item_display_list_view = QtWidgets.QListView(self.page)
        self.item_display_list_view.setProperty("showDropIndicator", False)
        self.item_display_list_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.item_display_list_view.setObjectName("item_display_list_view")
        self.gridLayout_2.addWidget(self.item_display_list_view, 1, 0, 1, 3)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 2, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.do_not_edit_checkbox = QtWidgets.QCheckBox(self.page)
        self.do_not_edit_checkbox.setObjectName("do_not_edit_checkbox")
        self.gridLayout_3.addWidget(self.do_not_edit_checkbox, 2, 0, 1, 1)
        self.download_object_button = QtWidgets.QPushButton(self.page)
        self.download_object_button.setObjectName("download_object_button")
        self.gridLayout_3.addWidget(self.download_object_button, 1, 0, 1, 1)
        self.editing_disabled_label = QtWidgets.QLabel(self.page)
        self.editing_disabled_label.setEnabled(True)
        self.editing_disabled_label.setObjectName("editing_disabled_label")
        self.gridLayout_3.addWidget(self.editing_disabled_label, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nsfw_filter_label = QtWidgets.QLabel(self.page)
        self.nsfw_filter_label.setObjectName("nsfw_filter_label")
        self.gridLayout_5.addWidget(self.nsfw_filter_label, 9, 0, 1, 1)
        self.sub_sort_label = QtWidgets.QLabel(self.page)
        self.sub_sort_label.setObjectName("sub_sort_label")
        self.gridLayout_5.addWidget(self.sub_sort_label, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 2, 0, 1, 1)
        self.restrict_date_checkbox = QtWidgets.QCheckBox(self.page)
        self.restrict_date_checkbox.setObjectName("restrict_date_checkbox")
        self.gridLayout_5.addWidget(self.restrict_date_checkbox, 1, 0, 1, 1)
        self.save_by_method_label = QtWidgets.QLabel(self.page)
        self.save_by_method_label.setObjectName("save_by_method_label")
        self.gridLayout_5.addWidget(self.save_by_method_label, 4, 0, 1, 1)
        self.custom_save_path_line_edit = QtWidgets.QLineEdit(self.page)
        self.custom_save_path_line_edit.setObjectName("custom_save_path_line_edit")
        self.gridLayout_5.addWidget(self.custom_save_path_line_edit, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 3, 0, 1, 1)
        self.custom_save_path_dialog = QtWidgets.QPushButton(self.page)
        self.custom_save_path_dialog.setObjectName("custom_save_path_dialog")
        self.gridLayout_5.addWidget(self.custom_save_path_dialog, 5, 0, 1, 1)
        self.download_videos_checkbox = QtWidgets.QCheckBox(self.page)
        self.download_videos_checkbox.setObjectName("download_videos_checkbox")
        self.gridLayout_5.addWidget(self.download_videos_checkbox, 7, 0, 1, 1)
        self.save_path_name_label = QtWidgets.QLabel(self.page)
        self.save_path_name_label.setObjectName("save_path_name_label")
        self.gridLayout_5.addWidget(self.save_path_name_label, 5, 2, 1, 1)
        self.save_by_method_combo = QtWidgets.QComboBox(self.page)
        self.save_by_method_combo.setObjectName("save_by_method_combo")
        self.gridLayout_5.addWidget(self.save_by_method_combo, 4, 1, 1, 2)
        self.name_downloads_combo = QtWidgets.QComboBox(self.page)
        self.name_downloads_combo.setObjectName("name_downloads_combo")
        self.gridLayout_5.addWidget(self.name_downloads_combo, 3, 1, 1, 2)
        self.post_limit_spinbox = QtWidgets.QSpinBox(self.page)
        self.post_limit_spinbox.setAccelerated(True)
        self.post_limit_spinbox.setMaximum(1000)
        self.post_limit_spinbox.setObjectName("post_limit_spinbox")
        self.gridLayout_5.addWidget(self.post_limit_spinbox, 2, 1, 1, 2)
        self.date_limit_edit = QtWidgets.QDateTimeEdit(self.page)
        self.date_limit_edit.setCalendarPopup(True)
        self.date_limit_edit.setTimeSpec(QtCore.Qt.LocalTime)
        self.date_limit_edit.setObjectName("date_limit_edit")
        self.gridLayout_5.addWidget(self.date_limit_edit, 1, 1, 1, 2)
        self.sub_sort_combo = QtWidgets.QComboBox(self.page)
        self.sub_sort_combo.setObjectName("sub_sort_combo")
        self.gridLayout_5.addWidget(self.sub_sort_combo, 0, 1, 1, 2)
        self.download_images_checkbox = QtWidgets.QCheckBox(self.page)
        self.download_images_checkbox.setObjectName("download_images_checkbox")
        self.gridLayout_5.addWidget(self.download_images_checkbox, 7, 1, 1, 2)
        self.avoid_duplicates_checkbox = QtWidgets.QCheckBox(self.page)
        self.avoid_duplicates_checkbox.setObjectName("avoid_duplicates_checkbox")
        self.gridLayout_5.addWidget(self.avoid_duplicates_checkbox, 8, 1, 1, 2)
        self.nsfw_filter_combo = QtWidgets.QComboBox(self.page)
        self.nsfw_filter_combo.setObjectName("nsfw_filter_combo")
        self.gridLayout_5.addWidget(self.nsfw_filter_combo, 9, 1, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.content_list = QtWidgets.QListWidget(self.page_2)
        self.content_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.content_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list.setViewMode(QtWidgets.QListView.IconMode)
        self.content_list.setWordWrap(True)
        self.content_list.setObjectName("content_list")
        self.gridLayout_6.addWidget(self.content_list, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.stacked_widget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 3)

        self.retranslateUi(RedditObjectSettingsDialog)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RedditObjectSettingsDialog)

    def retranslateUi(self, RedditObjectSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        RedditObjectSettingsDialog.setWindowTitle(_translate("RedditObjectSettingsDialog", "Settings"))
        self.restore_defaults_button.setToolTip(_translate("RedditObjectSettingsDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Restore settings to the options in the master settings dialog</span></p></body></html>"))
        self.restore_defaults_button.setText(_translate("RedditObjectSettingsDialog", "Restore Defaults"))
        self.view_downloads_button.setToolTip(_translate("RedditObjectSettingsDialog", "View this users downloads (will only display downloads that are in the save path above)"))
        self.view_downloads_button.setText(_translate("RedditObjectSettingsDialog", "View Downloads"))
        self.item_added_label.setText(_translate("RedditObjectSettingsDialog", "User Added On:"))
        self.total_downloads_title_label.setText(_translate("RedditObjectSettingsDialog", "Total User Downloads: "))
        self.total_downloads_label.setText(_translate("RedditObjectSettingsDialog", "0"))
        self.item_display_list_label.setText(_translate("RedditObjectSettingsDialog", "Previous Downloads:"))
        self.do_not_edit_checkbox.setToolTip(_translate("RedditObjectSettingsDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">If checked the changes made in this dialog will not be overwritten by the program when it is run.  The user date limit, avoid duplicates , and download naming method will all remain as they are when this dialog is saved.  The previous downloads will continue to be added to.</span></p></body></html>"))
        self.do_not_edit_checkbox.setText(_translate("RedditObjectSettingsDialog", "Do not overwrite these settings"))
        self.download_object_button.setToolTip(_translate("RedditObjectSettingsDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Download this user only with the settings as they are in this dialog</span></p></body></html>"))
        self.download_object_button.setText(_translate("RedditObjectSettingsDialog", "Download This User"))
        self.editing_disabled_label.setText(_translate("RedditObjectSettingsDialog", "Editing disabled while downloader is running"))
        self.nsfw_filter_label.setText(_translate("RedditObjectSettingsDialog", "NSFW filter:"))
        self.sub_sort_label.setText(_translate("RedditObjectSettingsDialog", "Sort Subreddit By:"))
        self.label.setText(_translate("RedditObjectSettingsDialog", "Post Limit:"))
        self.restrict_date_checkbox.setText(_translate("RedditObjectSettingsDialog", "Restrict by Date:"))
        self.save_by_method_label.setText(_translate("RedditObjectSettingsDialog", "Save By Method:"))
        self.label_2.setText(_translate("RedditObjectSettingsDialog", "Name Downloads By: "))
        self.custom_save_path_dialog.setText(_translate("RedditObjectSettingsDialog", "Custom Save Path"))
        self.download_videos_checkbox.setText(_translate("RedditObjectSettingsDialog", "Download Videos"))
        self.save_path_name_label.setText(_translate("RedditObjectSettingsDialog", "TextLabel"))
        self.date_limit_edit.setToolTip(_translate("RedditObjectSettingsDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">The date and time (time is in 24 hour format) to restrict downloads to</span></p></body></html>"))
        self.date_limit_edit.setDisplayFormat(_translate("RedditObjectSettingsDialog", "M/d/yyyy hh:mm ap"))
        self.sub_sort_combo.setToolTip(_translate("RedditObjectSettingsDialog", "<html><head/><body><p><span style=\" font-size:10pt;\">This combo box is only considered if this subreddit is downloaded as a single download</span></p></body></html>"))
        self.download_images_checkbox.setText(_translate("RedditObjectSettingsDialog", "Download Images"))
        self.avoid_duplicates_checkbox.setText(_translate("RedditObjectSettingsDialog", "Avoid Duplicates"))

