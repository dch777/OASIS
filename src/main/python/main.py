import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from airfoils import Airfoil
from functools import partial
import math
import optimize

reynolds = 100000000

#CLASS OASYS ADVANCED PANEL
class Ui_OASYSADVANCED(object):

    MAX_CAMBER = 0
    MAX_CAMBER_POSITION = 0
    THICKNESS_PERCENT = 0
    NUMBER_OF_POINTS = 0

    def openBasic(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OASYS()
        self.ui.setupUi(self.window)
        self.window.show()

    def resetValues(self):
        self.MAXCAMBERPOSITIONSLIDER.setValue(0)
        self.NOPOINTSSLIDER.setValue(0)
        self.THICKNESSSLIDER.setValue(0)
        self.MAXCAMBERSLIDER.setValue(0)

    def NACACONVERTER(self, maxcamber, maxcamberpos, thickness):
        m = math.floor(maxcamber/10)
        p = math.floor(maxcamberpos/10)
        xx = f"{thickness:02d}"

        finalNACA = f"{m}{p}{xx}"

        return finalNACA

    def updategraph(self):
        print(self.NACACONVERTER(self.MAXCAMBERSLIDER.value(), self.MAXCAMBERPOSITIONSLIDER.value(), self.THICKNESSSLIDER.value()))
        foil = Airfoil.NACA4(self.NACACONVERTER(self.MAXCAMBERSLIDER.value(), self.MAXCAMBERPOSITIONSLIDER.value(), self.THICKNESSSLIDER.value()))
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

        self.GOBACKBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.GOBACKBUTTON.setGeometry(QtCore.QRect(840, 680, 91, 31))
        self.GOBACKBUTTON.setObjectName("GOBACKBUTTON")

        self.RESETVALUEBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.RESETVALUEBUTTON.setGeometry(QtCore.QRect(710, 680, 91, 31))
        self.RESETVALUEBUTTON.setObjectName("RESETVALUEBUTTON")

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

        self.MAXCAMBERSLIDER.valueChanged.connect(self.MAXCAMBERDISPLAY.display)
        self.MAXCAMBERPOSITIONSLIDER.valueChanged.connect(self.MAXCAMBERPOSITIONDISPLAY.display)
        self.NOPOINTSSLIDER.valueChanged.connect(self.POINTSDISPLAY.display)
        self.THICKNESSSLIDER.valueChanged.connect(self.THICKNESSDISPLAY.display)
        self.RESETVALUEBUTTON.pressed.connect(self.resetValues)
        self.GOBACKBUTTON.pressed.connect(self.openBasic)

        cambersliderval = self.MAXCAMBERSLIDER.value()
        #self.MAXCAMBERDISPLAY.setProperty("intValue", cambersliderval)

        self.UPDATEPLOTBUTTON.clicked.connect(self.updategraph)

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

        """
        self.OPENPLOTBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.OPENPLOTBUTTON.setGeometry(QtCore.QRect(390, 680, 91, 31))
        self.OPENPLOTBUTTON.setObjectName("OPENPLOTBUTTON")
        """

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
        #self.OPENPLOTBUTTON.setText(_translate("OASYS", "Open Plot"))


        self.GOBACKBUTTON.setText(_translate("OASYS", "Return"))
        self.RESETVALUEBUTTON.setText(_translate("OASYS", "Reset values"))


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

#OUTPUTWINDOW
class Ui_OASYSOUTPUT(object):
    def setupUi(self, OASYS):
        naca, ld = optimize.getBestAirfoil(reynolds, iterations=20, angle=10)
        OASYS.setObjectName("OASYS")
        OASYS.resize(844, 591)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OASYS.sizePolicy().hasHeightForWidth())
        OASYS.setSizePolicy(sizePolicy)
        OASYS.setTabletTracking(False)
        OASYS.setStyleSheet("background-color: \"#93e5ff\";")
        self.centralwidget = QtWidgets.QWidget(OASYS)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 200, 831, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(470, 210, 61, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgs/ms.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.ANGLEOFATTACK = QtWidgets.QLabel(self.frame)
        self.ANGLEOFATTACK.setGeometry(QtCore.QRect(10, 80, 471, 41))
        self.ANGLEOFATTACK.setText(str(math.floor(ld[1])))
        self.ANGLEOFATTACK.setPixmap(QtGui.QPixmap("imgs/AOA.png"))
        self.ANGLEOFATTACK.setScaledContents(True)
        self.ANGLEOFATTACK.setObjectName("ANGLEOFATTACK")
        self.OPTIMALNACANUMBER = QtWidgets.QLabel(self.frame)
        self.OPTIMALNACANUMBER.setGeometry(QtCore.QRect(20, 140, 241, 41))
        self.OPTIMALNACANUMBER.setText("")
        self.OPTIMALNACANUMBER.setPixmap(QtGui.QPixmap("imgs/NACA airfoil.png"))
        self.OPTIMALNACANUMBER.setScaledContents(True)
        self.OPTIMALNACANUMBER.setObjectName("OPTIMALNACANUMBER")
        self.LDRLABEL = QtWidgets.QLabel(self.frame)
        self.LDRLABEL.setGeometry(QtCore.QRect(20, 200, 241, 41))
        self.LDRLABEL.setText("")
        self.LDRLABEL.setPixmap(QtGui.QPixmap("imgs/ld_ratio.png"))
        self.LDRLABEL.setScaledContents(True)
        self.LDRLABEL.setObjectName("LDRLABEL")
        self.VIEWGRAPHBUTTON = QtWidgets.QPushButton(self.frame)
        self.VIEWGRAPHBUTTON.setGeometry(QtCore.QRect(690, 130, 111, 51))
        self.VIEWGRAPHBUTTON.setObjectName("VIEWGRAPHBUTTON")
        self.VELOCITYOPTIMAL = QtWidgets.QLCDNumber(self.frame)
        self.VELOCITYOPTIMAL.setGeometry(QtCore.QRect(550, 70, 131, 51))
        self.VELOCITYOPTIMAL.setObjectName("VELOCITYOPTIMAL")
        self.VELOCITYOPTIMAL.display(math.floor(ld[1]))
        self.NACANUMBER = QtWidgets.QLCDNumber(self.frame)
        self.NACANUMBER.setGeometry(QtCore.QRect(550, 130, 131, 51))
        self.NACANUMBER.setObjectName("NACANUMBER")
        self.NACANUMBER.display(f"{naca:04d}")
        self.BESTLDRATIO = QtWidgets.QLCDNumber(self.frame)
        self.BESTLDRATIO.setGeometry(QtCore.QRect(550, 190, 131, 51))
        self.BESTLDRATIO.setObjectName("BESTLDRATIO")
        self.BESTLDRATIO.display(math.floor(ld[0]))
        self.DASHH = QtWidgets.QLabel(self.frame)
        self.DASHH.setGeometry(QtCore.QRect(270, 140, 281, 31))
        self.DASHH.setText("")
        self.DASHH.setPixmap(QtGui.QPixmap("imgs/dash.png"))
        self.DASHH.setScaledContents(False)
        self.DASHH.setObjectName("DASHH")
        self.DASH = QtWidgets.QLabel(self.frame)
        self.DASH.setGeometry(QtCore.QRect(480, 80, 61, 31))
        self.DASH.setText("")
        self.DASH.setPixmap(QtGui.QPixmap("imgs/dash.png"))
        self.DASH.setScaledContents(False)
        self.DASH.setObjectName("DASH")
        self.DASHHH = QtWidgets.QLabel(self.frame)
        self.DASHHH.setGeometry(QtCore.QRect(270, 210, 281, 31))
        self.DASHHH.setText("")
        self.DASHHH.setPixmap(QtGui.QPixmap("imgs/dash.png"))
        self.DASHHH.setScaledContents(False)
        self.DASHHH.setObjectName("DASHHH")
        self.OASYSMAIN = QtWidgets.QLabel(self.centralwidget)
        self.OASYSMAIN.setGeometry(QtCore.QRect(250, 0, 301, 71))
        self.OASYSMAIN.setText("")
        self.OASYSMAIN.setPixmap(QtGui.QPixmap("imgs/OASYS.png"))
        self.OASYSMAIN.setScaledContents(True)
        self.OASYSMAIN.setObjectName("OASYSMAIN")
        self.OASYSFULL = QtWidgets.QLabel(self.centralwidget)
        self.OASYSFULL.setGeometry(QtCore.QRect(40, 70, 741, 41))
        self.OASYSFULL.setText("")
        self.OASYSFULL.setPixmap(QtGui.QPixmap("imgs/Oasys full.png"))
        self.OASYSFULL.setScaledContents(True)
        self.OASYSFULL.setObjectName("OASYSFULL")
        self.OUTPUTWINDOW = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        self.OUTPUTWINDOW.setGeometry(QtCore.QRect(250, 150, 301, 41))
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.OUTPUTWINDOW.setFont(font)
        self.OUTPUTWINDOW.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OUTPUTWINDOW.setStyleSheet("font-color: \"#000000\"")
        self.OUTPUTWINDOW.setText("")
        self.OUTPUTWINDOW.setPixmap(QtGui.QPixmap("imgs/output.png"))
        self.OUTPUTWINDOW.setScaledContents(True)
        self.OUTPUTWINDOW.setObjectName("OUTPUTWINDOW")
        OASYS.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OASYS)
        self.statusbar.setObjectName("statusbar")
        OASYS.setStatusBar(self.statusbar)

        self.retranslateUi(OASYS)
        QtCore.QMetaObject.connectSlotsByName(OASYS)

    def retranslateUi(self, OASYS):
        _translate = QtCore.QCoreApplication.translate
        OASYS.setWindowTitle(_translate("OASYS", "OASYS"))
        self.VIEWGRAPHBUTTON.setText(_translate("OASYS", "View on graph"))

#basic optimization 
class Ui_OASYS(object):
    def openOutput(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OASYSOUTPUT()
        self.ui.setupUi(self.window)
        self.window.show()
        reynolds = self.REYNOLDSSLIDER.value()

    def openAdvanced(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OASYSADVANCED()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, OASYS):
        OASYS.setObjectName("OASYS")
        OASYS.resize(844, 591)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OASYS.sizePolicy().hasHeightForWidth())
        OASYS.setSizePolicy(sizePolicy)
        OASYS.setTabletTracking(False)
        OASYS.setStyleSheet("background-color: \"#93e5ff\";")
        self.centralwidget = QtWidgets.QWidget(OASYS)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 200, 831, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imgs/Reynolds Number.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.REYNOLDSDISPLAY = QtWidgets.QLCDNumber(self.frame)
        self.REYNOLDSDISPLAY.setGeometry(QtCore.QRect(580, 30, 211, 51))
        self.REYNOLDSDISPLAY.setObjectName("REYNOLDSDISPLAY")
        self.REYNOLDSSLIDER = QtWidgets.QSlider(self.frame)
        self.REYNOLDSSLIDER.setGeometry(QtCore.QRect(170, 50, 289, 22))
        self.REYNOLDSSLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.REYNOLDSSLIDER.setObjectName("REYNOLDSSLIDER")
        self.REYNOLDSSLIDER.setMinimum(100)
        self.REYNOLDSSLIDER.setMaximum(100000000)
        self.DENSITYSLIDER = QtWidgets.QSlider(self.frame)
        self.DENSITYSLIDER.setGeometry(QtCore.QRect(170, 130, 289, 22))
        self.DENSITYSLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.DENSITYSLIDER.setObjectName("DENSITYSLIDER")
        self.VELOCITYSLIDER = QtWidgets.QSlider(self.frame)
        self.VELOCITYSLIDER.setGeometry(QtCore.QRect(170, 220, 289, 22))
        self.VELOCITYSLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.VELOCITYSLIDER.setObjectName("VELOCITYSLIDER")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imgs/density.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 121, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imgs/velocity.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(470, 130, 81, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imgs/kgm3.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(470, 210, 61, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgs/ms.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.DENSITYDISPLAY = QtWidgets.QLCDNumber(self.frame)
        self.DENSITYDISPLAY.setGeometry(QtCore.QRect(580, 120, 211, 51))
        self.DENSITYDISPLAY.setObjectName("DENSITYDISPLAY")
        self.VELOCITYDISPLAY = QtWidgets.QLCDNumber(self.frame)
        self.VELOCITYDISPLAY.setGeometry(QtCore.QRect(580, 210, 211, 51))
        self.VELOCITYDISPLAY.setObjectName("VELOCITYDISPLAY")
        self.OUTPUTBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.OUTPUTBUTTON.setGeometry(QtCore.QRect(420, 520, 131, 41))
        self.OUTPUTBUTTON.setObjectName("OUTPUTBUTTON")
        self.OASYSHEAD = QtWidgets.QLabel(self.centralwidget)
        self.OASYSHEAD.setGeometry(QtCore.QRect(250, 0, 301, 71))
        self.OASYSHEAD.setText("")
        self.OASYSHEAD.setPixmap(QtGui.QPixmap("imgs/OASYS.png"))
        self.OASYSHEAD.setScaledContents(True)
        self.OASYSHEAD.setObjectName("OASYSHEAD")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 741, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgs/Oasys full.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.OPTTEXT = QtWidgets.QLabel(self.centralwidget)
        self.OPTTEXT.setGeometry(QtCore.QRect(70, 150, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.OPTTEXT.setFont(font)
        self.OPTTEXT.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OPTTEXT.setStyleSheet("font-color: \"#000000\"")
        self.OPTTEXT.setText("")
        self.OPTTEXT.setPixmap(QtGui.QPixmap("imgs/optimization system.png"))
        self.OPTTEXT.setScaledContents(True)
        self.OPTTEXT.setObjectName("OPTTEXT")
        self.ADVANCEDOPTIONS = QtWidgets.QPushButton(self.centralwidget)
        self.ADVANCEDOPTIONS.setGeometry(QtCore.QRect(260, 520, 131, 41))
        self.ADVANCEDOPTIONS.setObjectName("ADVANCEDOPTIONS")
        OASYS.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OASYS)
        self.statusbar.setObjectName("statusbar")
        OASYS.setStatusBar(self.statusbar)

        self.REYNOLDSSLIDER.valueChanged.connect(self.REYNOLDSDISPLAY.display)
        self.VELOCITYSLIDER.valueChanged.connect(self.VELOCITYDISPLAY.display)
        self.DENSITYSLIDER.valueChanged.connect(self.DENSITYDISPLAY.display)
        self.OUTPUTBUTTON.pressed.connect(self.openOutput)
        self.ADVANCEDOPTIONS.pressed.connect(self.openAdvanced)
        self.retranslateUi(OASYS)
        QtCore.QMetaObject.connectSlotsByName(OASYS)

    def retranslateUi(self, OASYS):
        _translate = QtCore.QCoreApplication.translate
        OASYS.setWindowTitle(_translate("OASYS", "OASYS"))
        self.OUTPUTBUTTON.setText(_translate("OASYS", "Show Output"))
        self.ADVANCEDOPTIONS.setText(_translate("OASYS", "Advanced options"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OASYS()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
