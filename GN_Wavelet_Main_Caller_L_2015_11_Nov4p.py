# -*- coding: utf-8 -*-
"""
Wavelet Main Calling 

Created on Wed May 27 19:57:06 2015
Updated on wed Nov 4 23:05 2015

@author: Green Neuroscience Laboratory
         Linh Pham
         Elan Ohayon     
"""

from PyQt4 import QtGui, QtCore
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from GN_Wavelet_GUI_Main_Panel import Ui_UiWaveletPanel
from Tkinter import Tk
import tkMessageBox

class MainWindow(QtGui.QMainWindow,Ui_UiWaveletPanel):
    def __init__(self, parent=None):
        super(MainWindow,self). __init__(parent)
        self.setupUi(self)

        # Signal duration and sampeling rates 
        self.WgtDSpinBox_SigSmpSec.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_SigLen.valueChanged.connect(self.update_plot_sig1)

        # Signal Part 1 Settings
        self.WgtDSpinBox_Sig1Freq.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig1Start.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig1Stop.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig1Amp.valueChanged.connect(self.update_plot_sig1)

        # Signal Part 2 Settings
        self.WgtDSpinBox_Sig2Freq.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig2Start.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig2Stop.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig2Amp.valueChanged.connect(self.update_plot_sig1)

        # Signal Part 3 Settings
        self.WgtDSpinBox_Sig3Freq.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig3Start.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig3Stop.valueChanged.connect(self.update_plot_sig1)
        self.WgtDSpinBox_Sig3Amp.valueChanged.connect(self.update_plot_sig1)

        # Signal Part 4 (Noise) Settings
        self.WgtDSpinBox_Sig3Amp.valueChanged.connect(self.update_plot_sig1)
     
        # Signal Load from file
        self.WgtPushButton_LoadFileSig.clicked.connect(self.load_SigFile)

        # Wavelet / Scalorgam Calculate
        QtCore.QObject.connect(self.WgtPushButton_RUN, QtCore.SIGNAL("clicked()"), self.update_Scalogram)
        
        # Write Files 

        self.WgtComboBox_WavType.activated.connect(self.update_mwav)
        self.WgtComboBox_ScaleVsFreq.activated.connect(self.update_mwav)

        self.WgtPushButton_WriteFiles.clicked.connect(self.Write_Files)

        self.WgtCheckBox_Out_Do_Sig.clicked.connect(self.update_boxes)
        self.WgtCheckBox_Out_Do_Wav.clicked.connect(self.update_boxes)


        
        # Initial Load
        self.initial_load()
    # Set up intial signal
    def initial_load(self):
        import os
        filename_out = str(os.getcwd()) + "\TEMP_"
        self.WgtLineEdit_FileName_Out_BASE.setText(filename_out)

        self.WgtDSpinBox_Sig2Amp.setValue(.5)
        self.update_plot_sig1()
        self.update_mwav() 
        self.WgtComboBox_Resolution.setCurrentIndex(2)  # 300 DPI
        self.WgtProgressBar1.setValue(0)
        self.WgtComboBox_WavType.setCurrentIndex(1)
        self.WgtComboBox_ScaleVsFreq.setCurrentIndex(1)
        self.WgtComboBox_CodeType.setCurrentIndex(1)
        #self.WgtWidget_Plot_Scalogram.canvas.fig.colorbar()

              
    # Doesn't show up on my screen
    def update_boxes(self):
        from Tkinter import Tk
        import tkMessageBox
        Tk().withdraw()

        if self.WgtCheckBox_Out_Do_Sig():
            #self.WgtCheckBox_Out_Sig_PNG. s Checked:
            WgtCheckBox_Out_Sig_PNG
            self.tkMessageBox.showinfo(title="Greetings", message="Box On!")  

        else:
            self.tkMessageBox.showinfo(title="Greetings", message="Box Offff!")  
            self.WgtCheckBox_Out_Sig_PNG.setHidden(true)
            self.WgtCheckBox_Out_Sig_PNG.setHidden(true)

    # mother wavelet
    def mother (self,f,t):
        return (np.e**(-1j*f*t )-np.e**(-1/2*f**2))*np.e**(-1/2*t**2)

    # draw a wavelet
    def update_mwav(self):
        wavInd= int(self.WgtComboBox_WavType.currentIndex())
        mx= np.linspace(-4,4, num = 1601)
        wavelet=self.mother(6,mx)
        # choose real morlet
        if wavInd == 0 :
            waveletz = wavelet.real
        # choose complex morlet
        elif wavInd == 1 :
            waveletz = wavelet
        # choose imagination morlet
        elif wavInd == 2:
            waveletz = wavelet.imag
        # choose ricker/ mexican hat
        elif wavInd == 3:
            waveletz= signal.ricker

        # plot it in the plot
        self.WgtWidget_Plot_WavMom.canvas.ax.clear()
        self.WgtWidget_Plot_WavMom.canvas.ax.plot(waveletz)
        self.WgtWidget_Plot_WavMom.canvas.draw()

        return mx, waveletz

    def load_SigFile(self):
        from Tkinter import Tk
        from tkFileDialog import askopenfilename
        import os
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        
        filename_out = os.path.splitext(filename)[0] # works


        self.WgtLineEdit_FileName_In.setText(filename)
        self.WgtLineEdit_FileName_Out_BASE.setText(filename_out)

        self.update_from_SigFile()
        print(filename)

    # load a signal from a file and plot it
    def update_from_SigFile(self):
        # load signal
        file_in = self.WgtLineEdit_FileName_In.text()
        file_in= str(file_in)
        data= np.loadtxt(file_in, delimiter= ",")
        data= np.array(data)

        # plot sginal
        self.WgtWidget_Plot_Sig1.canvas.ax1.clear()
        self.WgtWidget_Plot_Sig1.canvas.ax1.plot(data)
        self.WgtWidget_Plot_Sig1.canvas.draw()

        self.WgtWidget_Plot_Convolution.canvas.ax.clear()
        self.WgtWidget_Plot_Convolution.canvas.ax.plot(data)
        self.WgtWidget_Plot_Convolution.canvas.draw()
    
        
    #DEL @property
    # get the information of the signal's first component (frequency, component's location in time, the amplitude the component )
    def get_sig1info(self):

        SamplesPerS = int(self.WgtDSpinBox_SigSmpSec.value())
        slength = self.WgtDSpinBox_SigLen.value()

        sigfreq = self.WgtDSpinBox_Sig1Freq.value()
        sigstart = self.WgtDSpinBox_Sig1Start.value()
        sigstop = self.WgtDSpinBox_Sig1Stop.value()
        sigamp = self.WgtDSpinBox_Sig1Amp.value()

        samples = (slength * SamplesPerS) +1

        # get x domain 
        sx = np.linspace(0,slength, num=samples)

        # construct y (pulse signal)
        sy = np.zeros(sigstart*SamplesPerS)
        pulse_mid_domain=np.linspace(sigstart,sigstop, num=(sigstop-sigstart)*SamplesPerS +1)
        sy = np.append(sy, sigamp*np.sin(2*sigfreq*pulse_mid_domain*np.pi))
        sy = np.append(sy, np.zeros((slength-sigstop)*SamplesPerS))

        return sx, sy
    # get the information of the signal's second component
    def get_sig2info(self):

        SamplesPerS = int(self.WgtDSpinBox_SigSmpSec.value())
        slength = self.WgtDSpinBox_SigLen.value()

        sigfreq = self.WgtDSpinBox_Sig2Freq.value()
        sigstart = self.WgtDSpinBox_Sig2Start.value()
        sigstop = self.WgtDSpinBox_Sig2Stop.value()
        sigamp = self.WgtDSpinBox_Sig2Amp.value()

        samples = (slength * SamplesPerS) +1

        # get x domain 
        sx = np.linspace(0,slength, num=samples)

        # construct y (pulse signal)
        sy = np.zeros(sigstart*SamplesPerS)
        pulse_mid_domain=np.linspace(sigstart,sigstop, num=(sigstop-sigstart)*SamplesPerS +1)
        sy = np.append(sy, sigamp*np.sin(2*sigfreq*pulse_mid_domain*np.pi))
        sy = np.append(sy, np.zeros((slength-sigstop)*SamplesPerS))

        return sx, sy
    # get the information of the signal's third component
    def get_sig3info(self):

        SamplesPerS = int(self.WgtDSpinBox_SigSmpSec.value())
        slength = self.WgtDSpinBox_SigLen.value()

        sigfreq = self.WgtDSpinBox_Sig3Freq.value()
        sigstart = self.WgtDSpinBox_Sig3Start.value()
        sigstop = self.WgtDSpinBox_Sig3Stop.value()
        sigamp = self.WgtDSpinBox_Sig3Amp.value()

        samples = (slength * SamplesPerS) +1

        # get x domain
        sx = np.linspace(0,slength, num=samples)

        # construct y (pulse signal)
        sy = np.zeros(sigstart*SamplesPerS)
        pulse_mid_domain=np.linspace(sigstart,sigstop, num=(sigstop-sigstart)*SamplesPerS +1)
        sy = np.append(sy, sigamp*np.sin(2*sigfreq*pulse_mid_domain*np.pi))
        sy = np.append(sy, np.zeros((slength-sigstop)*SamplesPerS))

        return sx, sy

    # plot signal and its three components
    def update_plot_sig1(self):

        sx1, sy1 = self.get_sig1info()
        sx2, sy2 = self.get_sig2info()
        sx3, sy3 = self.get_sig3info()
        # Noise goes here

        sy5 = sy1+sy2
        sy5= sy5+sy3 #sy5 is signal

        self.WgtWidget_Plot_Sig1.canvas.ax1.clear()
        self.WgtWidget_Plot_Sig1.canvas.ax1.plot(sx1,sy1)
        
        self.WgtWidget_Plot_Sig1.canvas.ax2.clear()
        self.WgtWidget_Plot_Sig1.canvas.ax2.plot(sx1,sy2)

        self.WgtWidget_Plot_Sig1.canvas.ax3.clear()
        self.WgtWidget_Plot_Sig1.canvas.ax3.plot(sx1,sy3)
        
        self.WgtWidget_Plot_Sig1.canvas.ax4.clear()
        # This is to plot the noise
        #self.WgtWidget_Plot_Sig1.canvas.ax4.plot(sx1,sy4)

        self.WgtWidget_Plot_Sig1.canvas.ax5.clear()
        self.WgtWidget_Plot_Sig1.canvas.ax5.plot(sx1,sy5)

        
        self.WgtWidget_Plot_Sig1.canvas.draw()

        self.WgtWidget_Plot_Convolution.canvas.ax.clear()
        self.WgtWidget_Plot_Convolution.canvas.ax.plot(sx1,sy5)# plot signal in the convolution box
        self.WgtWidget_Plot_Convolution.canvas.draw()

    # Prepare for CAWT
    """def cawt_prep(self):
        sx, sy1=self.get_sig1info()
        mx, waveletz= self. update_mwav()
        mxmax = max(mx)-mx[0]
        stepwav=mx[1]-mx[0]
        start_scale_sine= 1
        stop_scale_sine = 1000
        step_scale_sine=1
        scale_sine = np.arange(start_scale_sine, stop_scale_sine,step_scale_sine)
        start_freq_sine = 1
        stop_freq_sine= 100
        num_freq_sine =100
        freq_sine= np.linspace(start_freq_sine, stop_freq_sine, num_freq_sine)
        list_max= []
        for h in  freq_sine:
            sine= np.sin(2*np.pi*sx*h)
            cwtmatr_sine= np.empty((0, len(sine)))
            for s in scale_sine:
                mxInd= np.arange(s*mxmax)/(s*stepwav)
                setInd = mxInd.astype(int)
                setInd = setInd[::-1]
                conv_sine= -1/np.sqrt(s)*signal.fftconvolve(sine,waveletz[setInd],'same') # convolve the signal and the wavelet
                cwtmatr_sine= np.append(cwtmatr_sine, np.array([conv_sine]),axis=0)
            list_cwtmatrxz["cwtmatr_sine{0}".format(h)] = cwtmatr_sine
            max_val= np.amax(cwtmatr_sine)
            list_max= np.append(list_max, max_val)
        return list_max"""



    # Do wavelet transform and create a scalogram
    def update_Scalogram(self):
        
        SigTab = int(self.WgtTabWidget_Sig.currentIndex())
        if SigTab ==0: #Generated signal 
            sx, sy1=self.get_sig1info()
            sx, sy2=self.get_sig2info()
            sx, sy3=self.get_sig3info()
            sy5 = sy1+sy2
            sy5=sy5+sy3

        elif SigTab == 1: #ReadFile
            file_in = self.WgtLineEdit_FileName_In.text()
            file_in= str(file_in)
            data= np.loadtxt(file_in, delimiter= ",")
            sy5= np.array(data)
            # need to get sampling rate from the input
            SamplesPerS= 1000
            sx=np.linspace (0,len(sy5)/SamplesPerS,SamplesPerS)
            #self.WgtWidget_Plot_Sig1.canvas.ax1.clear()
            #self.WgtWidget_Plot_Sig1.canvas.ax1.plot(sy5)
            #self.WgtWidget_Plot_Sig1.canvas.draw()

            self.WgtWidget_Plot_Convolution.canvas.ax.clear()
            self.WgtWidget_Plot_Convolution.canvas.ax.plot(sy5)
            self.WgtWidget_Plot_Convolution.canvas.draw()

        # get wavelet information
        # scale/ freq start, stop, step
        wavDilStart = self.WgtDSpinBox_WavDilStart.value()
        wavDilStop = self.WgtDSpinBox_WavDilStop.value()
        wavDilStep = self.WgtDSpinBox_WavDilStep.value()

        # wavelet type
        wavInd= int(self.WgtComboBox_WavType.currentIndex())
        codeInd= int(self.WgtComboBox_CodeType.currentIndex())
        scaleVsFreq= int(self.WgtComboBox_ScaleVsFreq.currentIndex())



        widths= np.linspace(wavDilStart, wavDilStop, num= int((wavDilStop- wavDilStart)/wavDilStep +1))

        # using wavelet inmplemented in scipy package
        if codeInd == 0:
            if wavInd ==0:
                wavelet=signal.morlet
            elif wavInd == 1:
                wavelet=signal.morlet
            elif wavInd == 2:
                wavelet=signal.morlet
            elif wavInd == 3:
                wavelet=signal.ricker
            cwtmatr = signal.cwt(sy5, wavelet, widths)
            origin_set= "upper"

        # using wavelet custom code
        elif codeInd ==1:
            mx, waveletz = self. update_mwav()
            mxmax = max(mx)-mx[0]
            stepwav=mx[1]-mx[0]
            zscale = np.arange(wavDilStart, (wavDilStop+wavDilStep), wavDilStep)
            cwtmatr= np.empty((0, len(sy5)))
            # do covolution using scale
            if scaleVsFreq ==0:
                for s in zscale:
                    mxInd= np.arange(s*mxmax)/(s*stepwav)
                    setInd = mxInd.astype(int)
                    setInd = setInd[::-1]
                    conv2= -1/np.sqrt(s)*signal.fftconvolve(sy5,waveletz[setInd],'same') # convolve the signal and the wavelet
                    cwtmatr= np.append(cwtmatr, np.array([conv2]),axis=0)
                    #self.WgtWidget_Plot_Convolution.canvas.ax.clear()
                    #self.WgtWidget_Plot_Convolution.canvas.ax.plot(conv2)# plot convolution
                    #self.WgtWidget_Plot_Convolution.canvas.draw()
                    origin_set= "upper"
                    self.WgtLineEdit_Current_Scale.setText(str(s)) # show the current scale
                    zdone = s
                    self.WgtProgressBar1.setValue(zdone)# show progress
            # do convolution using frequency
            elif scaleVsFreq==1:
                for h in zscale:
                    s = 1000/h # assume frequency =  sampling rate/ scale
                    mxInd= np.arange(s*mxmax)/(s*stepwav)
                    setInd = mxInd.astype(int)
                    setInd = setInd[::-1]
                    conv2= -1/np.sqrt(s)*signal.fftconvolve(sy5,waveletz[setInd],'same') # convolve the signal and the wavelet
                    cwtmatr= np.append(cwtmatr, np.array([conv2]),axis=0)
                    #self.WgtWidget_Plot_Convolution.canvas.ax.clear()
                    #self.WgtWidget_Plot_Convolution.canvas.ax.plot(conv2)# plot convolution
                    #self.WgtWidget_Plot_Convolution.canvas.draw()
                    origin_set= "lower"
                    self.WgtLineEdit_Current_Scale.setText(str(h)) # show the current scale
                    zdone = h
                    self.WgtProgressBar1.setValue(zdone)# show progress

        # using wavelet custom code with CAWT
        elif codeInd ==2:
            mx, waveletz = self. update_mwav()
            mxmax = max(mx)-mx[0]
            stepwav=mx[1]-mx[0]
            zscale = np.arange(wavDilStart, (wavDilStop+wavDilStep), wavDilStep)
            cwtmatr= np.empty((0, len(sy5)))
            if scaleVsFreq ==0:
                for s in zscale:
                    mxInd= np.arange(s*mxmax)/(s*stepwav)
                    setInd = mxInd.astype(int)
                    setInd = setInd[::-1]
                    conv2= -1/np.sqrt(s)*signal.fftconvolve(sy5,waveletz[setInd],'same') # convolve the signal and the wavelet
                    cwtmatr= np.append(cwtmatr, np.array([conv2]),axis=0)
                    #self.WgtWidget_Plot_Convolution.canvas.ax.clear()
                    #self.WgtWidget_Plot_Convolution.canvas.ax.plot(conv2)# plot convolution
                    #self.WgtWidget_Plot_Convolution.canvas.draw()
                    #self.WgtLineEdit_Current_Scale.setText(str(s)) # show the current scale
                    self.WgtLineEdit_Current_Scale.setText(str(s))
                    zdone = s
                    self.WgtProgressBar1.setValue(zdone)# show progress
            elif scaleVsFreq ==1:
                #list_max = self.cawt_prep()
                max_list= np.loadtxt("Table_Of_Max_Generated_by_Freq_CWT_2015_10_Oct15b.txt", delimiter= ",")
                for fq in zscale:
                    if fq>101:
                        cawt_num=1
                    elif fq<101:
                        cawt_num=max_list[fq-1]
                    s = 1000/fq
                    mxInd= np.arange(s*mxmax)/(s*stepwav)
                    setInd = mxInd.astype(int)
                    setInd = setInd[::-1]
                    conv2= -1/np.sqrt(s)*signal.fftconvolve(sy5,waveletz[setInd],'same')*1/cawt_num # convolve the signal and the wavelet
                    cwtmatr= np.append(cwtmatr, np.array([conv2]),axis=0)
                    #self.WgtWidget_Plot_Convolution.canvas.ax.clear()
                    #self.WgtWidget_Plot_Convolution.canvas.ax.plot(conv2)# plot convolution
                    #self.WgtWidget_Plot_Convolution.canvas.draw()
                    origin_set ="lower"
                    self.WgtLineEdit_Current_Scale.setText(str(fq))
                    zdone = fq
                    self.WgtProgressBar1.setValue(zdone)




        # draw a scalogram
        xstart=np.amin(sx)
        xstop=np.amax(sx)
        import ctypes  # An included library with Python install.

        self.toolbar = self.addToolBar('MainToolbar')

        self.WgtWidget_Plot_Scalogram.canvas.fig.clear()
        self.WgtWidget_Plot_Scalogram.canvas.fig.subplots_adjust(bottom=0.2)
        self.WgtWidget_Plot_Scalogram.canvas.ax= self.WgtWidget_Plot_Scalogram.canvas.fig.add_subplot(111)
        cax=self.WgtWidget_Plot_Scalogram.canvas.ax.imshow(np.abs(cwtmatr), interpolation= 'none', aspect='auto',origin= origin_set,extent=[xstart,xstop,wavDilStart,wavDilStop])

        CB_Ind= int(self.WgtComboBox_ScalogramCBar_1.currentIndex())
        if CB_Ind == 0:
            #ctypes.windll.user32.MessageBoxA(0, "No Color Bar", "Your title", 1)
            # ClrBar="OFF"
            x=1
        elif CB_Ind == 1:
            #ctypes.windll.user32.MessageBoxA(0, "Include Color Bar", "Your title", 1)
            self.WgtWidget_Plot_Scalogram.canvas.fig.colorbar(cax,  orientation="vertical")
            #ClrBar="ON"
        #elif waxInd == 2:
        #   ctypes.windll.user32.MessageBoxA(0, "Imagie", "Your title", 1)
        # elif waxInd == 3:
        #   ctypes.windll.user32.MessageBoxA(0, "Rig", "Your title", 1)


        self.WgtWidget_Plot_Scalogram.canvas.draw()
        return cwtmatr
        
    # save scalogram and the generated signal
    def Write_Files(self):
        from Tkinter import Tk
        

        FileNameBase = str(self.WgtLineEdit_FileName_Out_BASE.text())

        Res = str(self.WgtComboBox_Resolution.currentText())
        ResInt = int(Res)        


        if self.WgtCheckBox_Out_Do_Sig.isChecked:

            # saving sig as png
            if self.WgtCheckBox_Out_Sig_PNG.isChecked:
                FileNameSigPNG = FileNameBase + "_SIG_" + Res + ".png"
                self.WgtWidget_Plot_Convolution.canvas.print_figure(FileNameSigPNG, dpi=ResInt)

            """ # saving sig as pdf
            if self.WgtCheckBox_Out_Sig_PDF.isChecked:
                FileNameSigPDF = FileNameBase + "_SIG_" + Res + ".pdf"
                self.WgtWidget_Plot_Convolution.canvas.print_figure(FileNameSigPDF, dpi=ResInt)

            # saving sig as txt
            if self.WgtCheckBox_Out_Sig_TXT.isChecked:
                FileNameSigTXT = FileNameBase +"_SIG_" + Res+ ".txt"
                sx1,sy1 = self.get_sig1info()
                sx2,sy2 = self.get_sig2info()
                sx3,sy3 = self.get_sig3info()
                sy5 = sy1+sy2
                sy5 = sy5+sy5
                np.savetxt(FileNameSigTXT, sy3, fmt='%.5f', delimiter= ', ')"""
        else :
            return

        if self.WgtCheckBox_Out_Do_Wav.isChecked:
            # saving scalogram as png
            """if self.WgtCheckBox_Out_Wav_PNG.isChecked:
                FileNameWavPNG = FileNameBase + "_WAV_" + Res + ".png"
                self.WgtWidget_Plot_Scalogram.canvas.print_png(FileNameWavPNG, dpi=ResInt)

            else:
                return"""

            # saving scalogram as pdf ?????
            CB_Ind= int(self.WgtComboBox_ScalogramCBar_1.currentIndex())
            if CB_Ind == 0:
                #ctypes.windll.user32.MessageBoxA(0, "No Color Bar", "Your title", 1)
                ClrBar="OFF"
            elif CB_Ind == 1:
                #ctypes.windll.user32.MessageBoxA(0, "Include Color Bar", "Your title", 1)
                #self.WgtWidget_Plot_Scalogram.canvas.fig.colorbar(cax,  orientation="vertical")
                ClrBar="ON"
            
            CodeType_Ind= int(self.WgtComboBox_CodeType.currentIndex())
            if CodeType_Ind == 0:
                CodeType="Scipy"
            elif CodeType_Ind == 1:
                CodeType="GN_Raw"
            elif CodeType_Ind == 2:
                CodeType="GN_CAWT"
                
            if self.WgtCheckBox_Out_Wav_PDF.isChecked:
                #WORKS FileNameWavPDF = FileNameBase + "_WAV_" + Res + ".jpg"
                #WORKS self.WgtWidget_Plot_Scalogram.canvas.print_jpg(FileNameWavPDF, dpi=ResInt)
                FileNameWavFig = FileNameBase + "_WAV_Code_" + CodeType + "_Res_" + Res + "_CrlBar_" + ClrBar + ".png"
                self.WgtWidget_Plot_Scalogram.canvas.print_figure(FileNameWavFig, dpi=ResInt)

            else:
                return

            """# saving scalogram as txt file
            if self.WgtCheckBox_Out_Wav_TXT.isChecked:
                FileNameWavTXT = FileNameBase + "_WAV_" + Res + ".txt"
                cwtmatr = self.update_Scalogram()
                np.savetxt(FileNameWavTXT, cwtmatr, fmt='%.5f',delimiter= ', ')"""
        else:
            return


            
        
if __name__ =='__main__':
    import sys  
    app= QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
