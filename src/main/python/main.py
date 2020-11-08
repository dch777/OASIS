import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_MainWindow2()
        self.ui.setupUi(self.window)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 799)
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet("background-color: \"#93e5ff\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(540, 440, 22, 251))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 200, 481, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 10, 291, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout.addWidget(self.horizontalSlider_3)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout.addWidget(self.horizontalSlider_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 141, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Kadhir\\Mystuff\\kadhir\\Coding\\Python\\ucstuff\\imgs/Reynolds Number.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.openbutton = QtWidgets.QPushButton(self.centralwidget)
        self.openbutton.setGeometry(QtCore.QRect(320, 690, 75, 23))
        self.openbutton.setObjectName("openbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 0, 301, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Kadhir\\Mystuff\\kadhir\\Coding\\Python\\ucstuff\\imgs/OASYS.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 741, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Kadhir\\Mystuff\\kadhir\\Coding\\Python\\ucstuff\\imgs/Oasys full.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.OPTTEXT = QtWidgets.QLabel(self.centralwidget)
        self.OPTTEXT.setGeometry(QtCore.QRect(-140, 150, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.OPTTEXT.setFont(font)
        self.OPTTEXT.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OPTTEXT.setStyleSheet("font-color: \"#000000\"")
        self.OPTTEXT.setText("")
        self.OPTTEXT.setPixmap(QtGui.QPixmap("C:\\Kadhir\\Mystuff\\kadhir\\Coding\\Python\\ucstuff\\imgs/optimization system.png"))
        self.OPTTEXT.setScaledContents(True)
        self.OPTTEXT.setObjectName("OPTTEXT")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openbutton.setText(_translate("MainWindow", "UpdatePlot"))


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class UI_MainWindow2(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

    def __init__(self, *args, **kwargs):
        super(UI_MainWindow2, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.setCentralWidget(sc)

        self.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
