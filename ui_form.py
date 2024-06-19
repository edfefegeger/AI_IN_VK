# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(252, 330)
        Widget.setMinimumSize(QSize(0, 0))
        Widget.setMaximumSize(QSize(252, 330))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 23, -1, 0)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(230, 50))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(230, 50))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(165, 50))
        self.pushButton_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(165, 50))
        self.pushButton_2.setMaximumSize(QSize(250, 0))
        self.pushButton_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">AI IN VK</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u0430\u0443\u0437\u0443", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"\u0421\u043d\u044f\u0442\u044c \u0441 \u043f\u0430\u0443\u0437\u044b", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443", None))
    # retranslateUi

