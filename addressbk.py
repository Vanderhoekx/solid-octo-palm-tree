# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addressbook.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
path = os.getcwd()

class Ui_addr_widget(object):
    def setupUi(self, addr_widget):
        addr_widget.setObjectName("addr_widget")
        addr_widget.resize(748, 431)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addr_widget.sizePolicy().hasHeightForWidth())
        addr_widget.setSizePolicy(sizePolicy)
        addr_widget.setMinimumSize(QtCore.QSize(748, 431))
        addr_widget.setAutoFillBackground(False)
        addr_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.631, y1:0.846182, x2:1, y2:0, stop:0.142045 rgba(0, 54, 81, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.add_disp = QtWidgets.QTabWidget(addr_widget)
        self.add_disp.setGeometry(QtCore.QRect(400, 10, 331, 401))
        self.add_disp.setMinimumSize(QtCore.QSize(305, 375))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add_disp.setFont(font)
        self.add_disp.setStyleSheet("")
        self.add_disp.setDocumentMode(True)
        self.add_disp.setObjectName("add_disp")
        self.tab_af = QtWidgets.QWidget()
        self.tab_af.setObjectName("tab_af")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_af)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.add_disp_af = QtWidgets.QTextBrowser(self.tab_af)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_disp_af.setFont(font)
        self.add_disp_af.setAcceptRichText(False)
        self.add_disp_af.setSource(QtCore.QUrl("file:///" + path + "/Address_af.txt"))
        self.add_disp_af.setObjectName("add_disp_af")
        self.gridLayout_7.addWidget(self.add_disp_af, 0, 0, 1, 1)
        self.add_disp.addTab(self.tab_af, "")
        self.tab_gl = QtWidgets.QWidget()
        self.tab_gl.setObjectName("tab_gl")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_gl)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.add_disp_gl = QtWidgets.QTextBrowser(self.tab_gl)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_disp_gl.setFont(font)
        self.add_disp_gl.setSource(QtCore.QUrl("file:///" + path + "/Address_gl.txt"))
        self.add_disp_gl.setObjectName("add_disp_gl")
        self.gridLayout_6.addWidget(self.add_disp_gl, 0, 0, 1, 1)
        self.add_disp.addTab(self.tab_gl, "")
        self.tab_mr = QtWidgets.QWidget()
        self.tab_mr.setObjectName("tab_mr")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_mr)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.add_disp_mr = QtWidgets.QTextBrowser(self.tab_mr)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_disp_mr.setFont(font)
        self.add_disp_mr.setSource(QtCore.QUrl("file:///" + path + "/Address_mr.txt"))
        self.add_disp_mr.setObjectName("add_disp_mr")
        self.gridLayout_5.addWidget(self.add_disp_mr, 0, 0, 1, 1)
        self.add_disp.addTab(self.tab_mr, "")
        self.tab_sw = QtWidgets.QWidget()
        self.tab_sw.setObjectName("tab_sw")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_sw)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.add_disp_sw = QtWidgets.QTextBrowser(self.tab_sw)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_disp_sw.setFont(font)
        self.add_disp_sw.setSource(QtCore.QUrl("file:///" + path + "/Address_sw.txt"))
        self.add_disp_sw.setObjectName("add_disp_sw")
        self.gridLayout_4.addWidget(self.add_disp_sw, 0, 0, 1, 1)
        self.add_disp.addTab(self.tab_sw, "")
        self.tab_xz = QtWidgets.QWidget()
        self.tab_xz.setObjectName("tab_xz")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_xz)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.add_disp_xz = QtWidgets.QTextBrowser(self.tab_xz)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_disp_xz.setFont(font)
        self.add_disp_xz.setSource(QtCore.QUrl("file:///" + path + "/Address_xz.txt"))
        self.add_disp_xz.setObjectName("add_disp_xz")
        self.gridLayout_3.addWidget(self.add_disp_xz, 0, 0, 1, 1)
        self.add_disp.addTab(self.tab_xz, "")
        self.widget = QtWidgets.QWidget(addr_widget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 381, 337))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.fname_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.fname_lbl.setFont(font)
        self.fname_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.fname_lbl.setObjectName("fname_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.fname_lbl)
        self.fname_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.fname_ent.setFont(font)
        self.fname_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.fname_ent.setClearButtonEnabled(True)
        self.fname_ent.setObjectName("fname_ent")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fname_ent)
        self.lname_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.lname_lbl.setFont(font)
        self.lname_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.lname_lbl.setObjectName("lname_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lname_lbl)
        self.lname_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.lname_ent.setFont(font)
        self.lname_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.lname_ent.setClearButtonEnabled(True)
        self.lname_ent.setObjectName("lname_ent")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lname_ent)
        self.add1_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.add1_lbl.setFont(font)
        self.add1_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.add1_lbl.setObjectName("add1_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.add1_lbl)
        self.add1_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.add1_ent.setFont(font)
        self.add1_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.add1_ent.setClearButtonEnabled(True)
        self.add1_ent.setObjectName("add1_ent")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.add1_ent)
        self.add2_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.add2_lbl.setFont(font)
        self.add2_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.add2_lbl.setObjectName("add2_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.add2_lbl)
        self.add2_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.add2_ent.setFont(font)
        self.add2_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.add2_ent.setClearButtonEnabled(True)
        self.add2_ent.setObjectName("add2_ent")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.add2_ent)
        self.city_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.city_lbl.setFont(font)
        self.city_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.city_lbl.setObjectName("city_lbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.city_lbl)
        self.city_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.city_ent.setFont(font)
        self.city_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.city_ent.setClearButtonEnabled(True)
        self.city_ent.setObjectName("city_ent")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.city_ent)
        self.prov_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.prov_lbl.setFont(font)
        self.prov_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.prov_lbl.setObjectName("prov_lbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.prov_lbl)
        self.prov_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.prov_ent.setFont(font)
        self.prov_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.prov_ent.setClearButtonEnabled(True)
        self.prov_ent.setObjectName("prov_ent")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.prov_ent)
        self.country_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.country_lbl.setFont(font)
        self.country_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.country_lbl.setObjectName("country_lbl")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.country_lbl)
        self.country_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.country_ent.setFont(font)
        self.country_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.country_ent.setClearButtonEnabled(True)
        self.country_ent.setObjectName("country_ent")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.country_ent)
        self.postal_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.postal_lbl.setFont(font)
        self.postal_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.postal_lbl.setObjectName("postal_lbl")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.postal_lbl)
        self.postal_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.postal_ent.setFont(font)
        self.postal_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.postal_ent.setClearButtonEnabled(True)
        self.postal_ent.setObjectName("postal_ent")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.postal_ent)
        self.email_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.email_lbl.setFont(font)
        self.email_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.email_lbl.setObjectName("email_lbl")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.email_lbl)
        self.email_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.email_ent.setFont(font)
        self.email_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.email_ent.setClearButtonEnabled(True)
        self.email_ent.setObjectName("email_ent")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.email_ent)
        self.ph1_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.ph1_lbl.setFont(font)
        self.ph1_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.ph1_lbl.setObjectName("ph1_lbl")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.ph1_lbl)
        self.ph1_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.ph1_ent.setFont(font)
        self.ph1_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.ph1_ent.setClearButtonEnabled(True)
        self.ph1_ent.setObjectName("ph1_ent")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.ph1_ent)
        self.ph2_lbl = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        self.ph2_lbl.setFont(font)
        self.ph2_lbl.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.ph2_lbl.setObjectName("ph2_lbl")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.ph2_lbl)
        self.ph2_ent = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.ph2_ent.setFont(font)
        self.ph2_ent.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.ph2_ent.setClearButtonEnabled(True)
        self.ph2_ent.setObjectName("ph2_ent")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.ph2_ent)
        self.splitter = QtWidgets.QSplitter(addr_widget)
        self.splitter.setGeometry(QtCore.QRect(10, 380, 381, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.clr_btn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.clr_btn.setFont(font)
        self.clr_btn.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.clr_btn.setObjectName("clr_btn")
        self.sub_btn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(11)
        self.sub_btn.setFont(font)
        self.sub_btn.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0.051, angle:112.1, stop:0 rgba(255, 255, 0, 69), stop:0.318182 rgba(255, 255, 0, 69), stop:0.380682 rgba(255, 255, 0, 69), stop:0.397727 rgba(255, 244, 71, 130), stop:0.539773 rgba(255, 255, 0, 255), stop:0.556818 rgba(251, 255, 0, 145), stop:0.607955 rgba(247, 255, 0, 208), stop:1 rgba(255, 255, 0, 69));")
        self.sub_btn.setObjectName("sub_btn")

        self.retranslateUi(addr_widget)
        self.add_disp.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(addr_widget)

    def retranslateUi(self, addr_widget):
        _translate = QtCore.QCoreApplication.translate
        addr_widget.setWindowTitle(_translate("addr_widget", "Address Book"))
        self.add_disp.setTabText(self.add_disp.indexOf(self.tab_af), _translate("addr_widget", "A-F"))
        self.add_disp.setTabText(self.add_disp.indexOf(self.tab_gl), _translate("addr_widget", "G-L"))
        self.add_disp.setTabText(self.add_disp.indexOf(self.tab_mr), _translate("addr_widget", "M-R"))
        self.add_disp.setTabText(self.add_disp.indexOf(self.tab_sw), _translate("addr_widget", "S-W"))
        self.add_disp.setTabText(self.add_disp.indexOf(self.tab_xz), _translate("addr_widget", "X-Z"))
        self.fname_lbl.setText(_translate("addr_widget", "First Name:"))
        self.lname_lbl.setText(_translate("addr_widget", "Last Name:"))
        self.add1_lbl.setText(_translate("addr_widget", "Address Line 1:"))
        self.add2_lbl.setText(_translate("addr_widget", "Address Line 2:"))
        self.city_lbl.setText(_translate("addr_widget", "City:"))
        self.prov_lbl.setText(_translate("addr_widget", "Province/State:"))
        self.country_lbl.setText(_translate("addr_widget", "Country:"))
        self.postal_lbl.setText(_translate("addr_widget", "Postal Code:"))
        self.email_lbl.setText(_translate("addr_widget", "Email Address:"))
        self.ph1_lbl.setText(_translate("addr_widget", "Phone Number:"))
        self.ph2_lbl.setText(_translate("addr_widget", "Phone Number:"))
        self.clr_btn.setText(_translate("addr_widget", "Clear Form"))
        self.sub_btn.setText(_translate("addr_widget", "Submit"))
