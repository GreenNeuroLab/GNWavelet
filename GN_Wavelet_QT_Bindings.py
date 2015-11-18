# -*- coding: utf-8 -*-
"""
Wavelet QT Bindings

Created on Thu May 28 13:01:22 2015
Updated on Mon Jun 1 08:15 2015 

@author: Green Neuroscience Laboratory
         Linh Pham
         Elan Ohayon     
"""

#!/usr/bin/env python

# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

# Matplotlib Figure object
#from matplotlib.Figure import Figure
import matplotlib.pyplot as plt

class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        """ The following is created in 2015_05_May27a"""
        #self.fig = Figure() 
        #self.ax = self.fig.add_subplot(211) 
        
        """ The following is created in 2015_ 05_May28a""" 
        #self.fig = Figure()
        self.fig=plt.figure()
        self.fig.subplots_adjust(bottom=0.1) 
        self.fig.subplots_adjust(hspace=0) 
        #axarr = plt.subplots(2, 4)
        #self.fig.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
        # self.fig.subplots_adjust(bottom=0.06) 

        self.ax1 = self.fig.add_subplot(511)
        # self.ax2 = self.fig.add_subplot(312)
        # self.ax3 = self.fig.add_subplot(313)
#        self.ax2 = self.fig.add_subplot(412, sharex=self.ax1, sharey=self.ax1)
#        self.ax3 = self.fig.add_subplot(413, sharex=self.ax1, sharey=self.ax1)
#        self.ax4 = self.fig.add_subplot(414, sharex=self.ax1, sharey=self.ax1)
#        self.ax1.set_title('Test Signal')        
#        self.ax1.set_yticks([0, 6])
#        self.ax1.set_ylim([-30, 10])
        self.ax2 = self.fig.add_subplot(512)
        self.ax3 = self.fig.add_subplot(513)
        self.ax4 = self.fig.add_subplot(514)
        self.ax5 = self.fig.add_subplot(515)
 #       self.ax1.yticks([])
        
        #axarr = fig.subplots(1, 4)
        #self.fig.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)


        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        """FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)"""
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)

#---------------------
#ax.set_xticks([0, 1])
#ax.set_xlim([-0.5, 1.5])
# ax.set_ylim([0, 110])
#ax.set_ylim([0, 120])
#ax.set_xticklabels(['CONFIRMED BY\nEXPERIMENT', 'REFUTED BY\nEXPERIMENT'])
#plt.yticks([])
#---------------------


#---------------------
#
# Three subplots sharing both x/y axes
#f, axarr = plt.subplots(2, 2)

#f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
#ax1.plot(x, y)
#ax1.set_title('Sharing both axes')
#ax2.scatter(x, y)
#ax3.scatter(x, 2 * y ** 2 - 1, color='r')
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
#f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
#
#-------------------

class WgtPlot_Sig1(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        # set the layout to the vertical box
        self.setLayout(self.vbl)

class MplCanvas1(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        
        """ The following is created in 2015_ 05_May28a"""
        #self.fig = Figure()
        self.fig = plt.figure()
        self.fig.subplots_adjust(bottom=0.2)
        self.ax = self.fig.add_subplot(111)
        #self.ax = self.fig.add_subplot(122)

        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        """FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)"""
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)

#class MplCanvas2(FigureCanvas):
#    """Class to represent the FigureCanvas widget"""
#    def __init__(self):
#        # setup Matplotlib Figure and Axis
#        
#        """ The following is created in 2015_ 05_May28a"""
#        #self.fig = Figure()
#        self.fig = plt.figure()
#        self.fig.subplots_adjust(bottom=0.06) 
#        self.ax = self.fig.add_subplot(111) 
#
#        # initialization of the canvas
#        FigureCanvas.__init__(self, self.fig)
#        # we define the widget as expandable
#        """FigureCanvas.setSizePolicy(self,
#                                   QtGui.QSizePolicy.Expanding,
#                                   QtGui.QSizePolicy.Expanding)"""
#        # notify the system of updated policy
#        FigureCanvas.updateGeometry(self)

class WgtPlot_Wavelet(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas1()
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        # set the layout to the vertical box
        self.setLayout(self.vbl)
    
        
class WgtPlot_Scalogram(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas1()
        self.toolbar = NavigationToolbar(self.canvas, self)
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.toolbar)
        # set the layout to the vertical box
        self.setLayout(self.vbl)
        
