import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from airfoils import Airfoil
from functools import partial

#CLASS OASYS ADVANCED PANEL
class Ui_OASYSADVANCED(object):

    MAX_CAMBER = 0
    MAX_CAMBER_POSITION = 0
    THICKNESS_PERCENT = 0
    NUMBER_OF_POINTS = 0

    def NACACONVERTER(self, maxcamber, maxcamberpos, thickness):
        m = maxcamber/10
        p = maxcamberpos/10
        xx = thickness

        finalNACA = f"{m}{p}{xx}"

        return finalNACA


    def updategraph(self, maxcamber, maxcamberpos, thickness, points):
        foil = Airfoil.NACA4(self.NACACONVERTER(maxcamber, maxcamberpos, thickness), points)
        print(maxcamber)
        foil.plot()




    #Setup for all UI elements
    def setupUi(self, OASYS):

        #Main window
        OASYS.setObjectName("OASYSADVANCED")
        OASYS.resize(1061, 799)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OASYS.sizePolicy().hasHeightForWidth())
        OASYS.setSizePolicy(sizePolicy)
        OASYS.setTabletTracking(False)
        OASYS.setStyleSheet("background-color: \"#93e5ff\";")

        #Alignment widget
        self.centralwidget = QtWidgets.QWidget(OASYS)
        self.centralwidget.setObjectName("centralwidget")

        #Container to hold all sliders/ data input
        self.CONTAINER = QtWidgets.QFrame(self.centralwidget)
        self.CONTAINER.setGeometry(QtCore.QRect(130, 200, 801, 461))
        self.CONTAINER.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CONTAINER.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CONTAINER.setObjectName("CONTAINER")

        self.MAXCAMBERSLIDER = QtWidgets.QSlider(self.CONTAINER)
        self.MAXCAMBERSLIDER.setGeometry(QtCore.QRect(310, 50, 289, 22))
        self.MAXCAMBERSLIDER.setMaximum(90)
        self.MAXCAMBERSLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.MAXCAMBERSLIDER.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.MAXCAMBERSLIDER.setTickInterval(10)
        self.MAXCAMBERSLIDER.setObjectName("MAXCAMBERSLIDER")

        cambersliderval = 0
        self.MAXCAMBERSLIDER.setValue(cambersliderval)

        #max camber display
        self.MAXCAMBERDISPLAY = QtWidgets.QLCDNumber(self.CONTAINER)
        self.MAXCAMBERDISPLAY.setGeometry(QtCore.QRect(650, 10, 131, 51))
        self.MAXCAMBERDISPLAY.setObjectName("MAXCAMBERDISPLAY")




        #thickness slider
        self.THICKNESSSLIDER = QtWidgets.QSlider(self.CONTAINER)
        self.THICKNESSSLIDER.setGeometry(QtCore.QRect(310, 230, 289, 22))
        self.THICKNESSSLIDER.setAutoFillBackground(False)
        self.THICKNESSSLIDER.setMaximum(40)
        self.THICKNESSSLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.THICKNESSSLIDER.setInvertedAppearance(False)
        self.THICKNESSSLIDER.setInvertedControls(False)
        self.THICKNESSSLIDER.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.THICKNESSSLIDER.setTickInterval(1)
        self.THICKNESSSLIDER.setObjectName("THICKNESSSLIDER")

        #max camber position display
        self.MAXCAMBERPOSITIONDISPLAY = QtWidgets.QLCDNumber(self.CONTAINER)
        self.MAXCAMBERPOSITIONDISPLAY.setGeometry(QtCore.QRect(650, 100, 131, 51))
        self.MAXCAMBERPOSITIONDISPLAY.setObjectName("MAXCAMBERPOSITIONDISPLAY")

        #thickness display
        self.THICKNESSDISPLAY = QtWidgets.QLCDNumber(self.CONTAINER)
        self.THICKNESSDISPLAY.setGeometry(QtCore.QRect(650, 190, 131, 51))
        self.THICKNESSDISPLAY.setObjectName("THICKNESSDISPLAY")

        #point # slider
        self.NOPOINTSSLIDER = QtWidgets.QSlider(self.CONTAINER)
        self.NOPOINTSSLIDER.setGeometry(QtCore.QRect(310, 330, 289, 22))
        self.NOPOINTSSLIDER.setMaximum(200)
        self.NOPOINTSSLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.NOPOINTSSLIDER.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.NOPOINTSSLIDER.setTickInterval(5)
        self.NOPOINTSSLIDER.setObjectName("NOPOINTSSLIDER")


        self.MAXCAMBERPERCENTLABEL = QtWidgets.QLabel(self.CONTAINER)
        self.MAXCAMBERPERCENTLABEL.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.MAXCAMBERPERCENTLABEL.setText("")
        self.MAXCAMBERPERCENTLABEL.setPixmap(QtGui.QPixmap("imgs/max camber.png"))
        self.MAXCAMBERPERCENTLABEL.setScaledContents(True)
        self.MAXCAMBERPERCENTLABEL.setObjectName("MAXCAMBERPERCENTLABEL")


        self.MAXCAMBERPOSITIONPERCENTLABLE = QtWidgets.QLabel(self.CONTAINER)
        self.MAXCAMBERPOSITIONPERCENTLABLE.setGeometry(QtCore.QRect(10, 130, 281, 31))
        self.MAXCAMBERPOSITIONPERCENTLABLE.setText("")
        self.MAXCAMBERPOSITIONPERCENTLABLE.setPixmap(QtGui.QPixmap("imgs/max camberpos.png"))
        self.MAXCAMBERPOSITIONPERCENTLABLE.setScaledContents(True)
        self.MAXCAMBERPOSITIONPERCENTLABLE.setObjectName("MAXCAMBERPOSITIONPERCENTLABLE")


        self.THICKNESSPERCENTLABEL = QtWidgets.QLabel(self.CONTAINER)
        self.THICKNESSPERCENTLABEL.setGeometry(QtCore.QRect(10, 220, 151, 31))
        self.THICKNESSPERCENTLABEL.setText("")
        self.THICKNESSPERCENTLABEL.setPixmap(QtGui.QPixmap("imgs/Thickness.png"))
        self.THICKNESSPERCENTLABEL.setScaledContents(True)
        self.THICKNESSPERCENTLABEL.setObjectName("THICKNESSPERCENTLABEL")


        self.POINTSDISPLAY = QtWidgets.QLCDNumber(self.CONTAINER)
        self.POINTSDISPLAY.setGeometry(QtCore.QRect(650, 290, 131, 51))
        self.POINTSDISPLAY.setObjectName("POINTSDISPLAY")


        self.ZERONINTEYLABEL = QtWidgets.QLabel(self.CONTAINER)
        self.ZERONINTEYLABEL.setGeometry(QtCore.QRect(300, 10, 321, 31))
        self.ZERONINTEYLABEL.setText("")
        self.ZERONINTEYLABEL.setPixmap(QtGui.QPixmap("imgs/0-.png"))
        self.ZERONINTEYLABEL.setScaledContents(True)
        self.ZERONINTEYLABEL.setObjectName("ZERONINTEYLABEL")


        self.MAXCAMBERPOSITIONSLIDER = QtWidgets.QSlider(self.CONTAINER)
        self.MAXCAMBERPOSITIONSLIDER.setGeometry(QtCore.QRect(310, 140, 289, 22))
        self.MAXCAMBERPOSITIONSLIDER.setMaximum(90)
        self.MAXCAMBERPOSITIONSLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.MAXCAMBERPOSITIONSLIDER.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.MAXCAMBERPOSITIONSLIDER.setTickInterval(10)
        self.MAXCAMBERPOSITIONSLIDER.setObjectName("MAXCAMBERPOSITIONSLIDER")


        self.ZERONINTEYLABEL_2 = QtWidgets.QLabel(self.CONTAINER)
        self.ZERONINTEYLABEL_2.setGeometry(QtCore.QRect(300, 100, 321, 31))
        self.ZERONINTEYLABEL_2.setText("")
        self.ZERONINTEYLABEL_2.setPixmap(QtGui.QPixmap("imgs/0-.png"))
        self.ZERONINTEYLABEL_2.setScaledContents(True)
        self.ZERONINTEYLABEL_2.setObjectName("ZERONINTEYLABEL_2")


        self.ZEROFORTYLABEL = QtWidgets.QLabel(self.CONTAINER)
        self.ZEROFORTYLABEL.setGeometry(QtCore.QRect(300, 200, 321, 31))
        self.ZEROFORTYLABEL.setText("")
        self.ZEROFORTYLABEL.setPixmap(QtGui.QPixmap("imgs/0-40.png"))
        self.ZEROFORTYLABEL.setScaledContents(True)
        self.ZEROFORTYLABEL.setObjectName("ZEROFORTYLABEL")


        self.NUMBEROFPOINTSLABEL = QtWidgets.QLabel(self.CONTAINER)
        self.NUMBEROFPOINTSLABEL.setGeometry(QtCore.QRect(10, 320, 141, 31))
        self.NUMBEROFPOINTSLABEL.setText("")
        self.NUMBEROFPOINTSLABEL.setPixmap(QtGui.QPixmap("imgs/pointnumber.png"))
        self.NUMBEROFPOINTSLABEL.setScaledContents(True)
        self.NUMBEROFPOINTSLABEL.setObjectName("NUMBEROFPOINTSLABEL")

        self.ZEROTEWOHUNDREDLABEL = QtWidgets.QLabel(self.CONTAINER)
        self.ZEROTEWOHUNDREDLABEL.setGeometry(QtCore.QRect(300, 300, 321, 31))
        self.ZEROTEWOHUNDREDLABEL.setText("")
        self.ZEROTEWOHUNDREDLABEL.setPixmap(QtGui.QPixmap("imgs/0-200.png"))
        self.ZEROTEWOHUNDREDLABEL.setScaledContents(True)
        self.ZEROTEWOHUNDREDLABEL.setObjectName("ZEROTEWOHUNDREDLABEL")

        self.UPDATEPLOTBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.UPDATEPLOTBUTTON.setGeometry(QtCore.QRect(130, 680, 91, 31))
        self.UPDATEPLOTBUTTON.setObjectName("UPDATEPLOTBUTTON")


        #print(cambersliderval)

        self.MAXCAMBERSLIDER.valueChanged.connect(self.MAXCAMBERDISPLAY.display)

        cambersliderval = self.MAXCAMBERSLIDER.value()
        #self.MAXCAMBERDISPLAY.setProperty("intValue", cambersliderval)

        foil = Airfoil.NACA4("2454")

        #x = partial()

        self.UPDATEPLOTBUTTON.clicked.connect(foil.plot)

        self.TITLEOASISLABEL = QtWidgets.QLabel(self.centralwidget)
        self.TITLEOASISLABEL.setGeometry(QtCore.QRect(370, 0, 301, 71))
        self.TITLEOASISLABEL.setText("")
        self.TITLEOASISLABEL.setPixmap(QtGui.QPixmap("imgs/OASYS.png"))
        self.TITLEOASISLABEL.setScaledContents(True)
        self.TITLEOASISLABEL.setObjectName("TITLEOASISLABEL")

        self.OASYSFULLLABEL = QtWidgets.QLabel(self.centralwidget)
        self.OASYSFULLLABEL.setGeometry(QtCore.QRect(150, 70, 741, 41))
        self.OASYSFULLLABEL.setText("")
        self.OASYSFULLLABEL.setPixmap(QtGui.QPixmap("imgs/Oasys full.png"))
        self.OASYSFULLLABEL.setScaledContents(True)
        self.OASYSFULLLABEL.setObjectName("OASYSFULLLABEL")

        self.ADVANCEDCONTROLLABEL = QtWidgets.QLabel(self.centralwidget)
        self.ADVANCEDCONTROLLABEL.setGeometry(QtCore.QRect(250, 150, 521, 41))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)

        self.ADVANCEDCONTROLLABEL.setFont(font)
        self.ADVANCEDCONTROLLABEL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ADVANCEDCONTROLLABEL.setStyleSheet("font-color: \"#000000\"")
        self.ADVANCEDCONTROLLABEL.setText("")
        self.ADVANCEDCONTROLLABEL.setPixmap(QtGui.QPixmap("imgs/advanced text.png"))
        self.ADVANCEDCONTROLLABEL.setScaledContents(True)
        self.ADVANCEDCONTROLLABEL.setObjectName("ADVANCEDCONTROLLABEL")

        self.VISUALIZE = QtWidgets.QPushButton(self.centralwidget)
        self.VISUALIZE.setGeometry(QtCore.QRect(260, 680, 182, 31))
        self.VISUALIZE.setObjectName("VISUALIZEBUTTON")

        """
        self.OPENPLOTBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.OPENPLOTBUTTON.setGeometry(QtCore.QRect(390, 680, 91, 31))
        self.OPENPLOTBUTTON.setObjectName("OPENPLOTBUTTON")
        """
        self.GOBACKBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.GOBACKBUTTON.setGeometry(QtCore.QRect(840, 680, 91, 31))
        self.GOBACKBUTTON.setObjectName("GOBACKBUTTON")

        self.RESETVALUEBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.RESETVALUEBUTTON.setGeometry(QtCore.QRect(710, 680, 91, 31))
        self.RESETVALUEBUTTON.setObjectName("RESETVALUEBUTTON")

        OASYS.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(OASYS)

        self.statusbar.setObjectName("statusbar")

        OASYS.setStatusBar(self.statusbar)

        self.retranslateUi(OASYS)
        QtCore.QMetaObject.connectSlotsByName(OASYS)

    def retranslateUi(self, OASYS):
        _translate = QtCore.QCoreApplication.translate
        OASYS.setWindowTitle(_translate("OASYS", "OASYS"))
        self.UPDATEPLOTBUTTON.setText(_translate("OASYS", "Update Plot"))
        self.VISUALIZE.setText(_translate("OASYS", "Visualize lift drag relationship"))
        #self.OPENPLOTBUTTON.setText(_translate("OASYS", "Open Plot"))


        self.GOBACKBUTTON.setText(_translate("OASYS", "Return"))
        self.RESETVALUEBUTTON.setText(_translate("OASYS", "Reset values"))


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
    ui = Ui_OASYSADVANCED()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
