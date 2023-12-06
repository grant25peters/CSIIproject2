from PyQt6.QtWidgets import *
from gui_television import *

class Logic(QMainWindow, Ui_television):
    '''
    Class for controlling the variables involved with a television
    '''

    MIN_VOLUME = 0
    MAX_VOLUME = 50
    MIN_CHANNEL = 0
    MAX_CHANNEL = 7


    def __init__(self) -> None:
        '''
        Method to set default values of the tv
        '''

        super().__init__()
        self.setupUi(self)

        self.status = False
        self.muted = False
        self.guide_status = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
        self.channel_text = 'DirectTV'


        self.power_button.clicked.connect(lambda:self.power())
        self.guide_button.clicked.connect(lambda:self.guide())
        self.mute_button.clicked.connect(lambda:self.mute())
        self.channel_up_button.clicked.connect(lambda:self.channel_up())
        self.channel_down_button.clicked.connect(lambda:self.channel_down())
        self.channel_button_0.clicked.connect(lambda:self.channel_0())
        self.channel_button_1.clicked.connect(lambda:self.channel_1())
        self.channel_button_2.clicked.connect(lambda:self.channel_2())
        self.channel_button_3.clicked.connect(lambda:self.channel_3())
        self.channel_button_4.clicked.connect(lambda:self.channel_4())
        self.channel_button_5.clicked.connect(lambda:self.channel_5())
        self.channel_button_6.clicked.connect(lambda:self.channel_6())
        self.channel_button_7.clicked.connect(lambda:self.channel_7())
        self.volume_up_button.clicked.connect(lambda:self.volume_up())
        self.volume_down_button.clicked.connect(lambda:self.volume_down())


    def guide(self) -> None:
        '''
        Method for opening the guide menu
        '''
        if self.status:
            if self.guide_status:
                font = QtGui.QFont()
                font.setPointSize(70)
                self.tv_view.setFont(font)
                self.tv_view.setText(f'{self.channel_text}')
                self.guide_status = False
            else:
                font = QtGui.QFont()
                font.setPointSize(26)
                self.tv_view.setFont(font)
                self.tv_view.setText(
                                    '0\t\tDirectTv\t\t\t\t\t\t\t'
                                    '1\t\tNBC\n'
                                    '2\t\tFOX\t\t\t\t\t\t\t\t'
                                    '3\t\tUSA\n'
                                    '4\t\tABC\t\t\t\t\t\t\t\t'
                                    '5\t\tESPN\n'
                                    '6\t\tCNN\t\t\t\t\t\t\t\t'
                                    '7\t\tCBS\n'
                )
                self.guide_status = True



    def power(self) -> None:
        '''
        Method for turning tv power status on (True) and off (False)
        '''
        if self.status:
            self.tv_view.setStyleSheet("background-color: black")
            self.status = False
        else:
            self.tv_view.setStyleSheet("background-color: white")
            self.status = True


    def mute(self) -> None:
        '''
        Method for muting (True) and unmuting (False) the tv volume
        '''
        if self.status:
            if self.muted:
                self.muted = False
                self.volume_level_label.setText(f'{self.volume}')
            else:
                self.muted = True
                self.volume_level_label.setText('0')


    def channel_up(self) -> None:
        '''
        Method for moving the channel value up one
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
                font = QtGui.QFont()
                font.setPointSize(70)
                self.tv_view.setFont(font)
                self.channel_text = 'DirectTV'
                self.tv_view.setText(f'{self.channel_text}')
            else:
                self.channel += 1
                font = QtGui.QFont()
                font.setPointSize(70)
                self.tv_view.setFont(font)
                if self.channel == 1:
                    self.channel_text = 'NBC'
                elif self.channel == 2:
                    self.channel_text = 'FOX'
                elif self.channel == 3:
                    self.channel_text = 'USA'
                elif self.channel == 4:
                    self.channel_text = 'ABC'
                elif self.channel == 5:
                    self.channel_text = 'ESPN'
                elif self.channel == 6:
                    self.channel_text = 'CNN'
                elif self.channel == 7:
                    self.channel_text = 'CBS'
                self.tv_view.setText(f'{self.channel_text}')
    

    def channel_down(self) -> None:
        '''
        Method for moving the channel value down one
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
                font = QtGui.QFont()
                font.setPointSize(70)
                self.tv_view.setFont(font)
                self.channel_text = 'CBS'
                self.tv_view.setText(f'{self.channel_text}')
            else:
                self.channel -= 1
                font = QtGui.QFont()
                font.setPointSize(70)
                self.tv_view.setFont(font)
                if self.channel == 0:
                    self.channel_text = 'DirectTV'
                elif self.channel == 1:
                    self.channel_text = 'NBC'
                elif self.channel == 2:
                    self.channel_text = 'FOX'
                elif self.channel == 3:
                    self.channel_text = 'USA'
                elif self.channel == 4:
                    self.channel_text = 'ABC'
                elif self.channel == 5:
                    self.channel_text = 'ESPN'
                elif self.channel == 6:
                    self.channel_text = 'CNN'
                self.tv_view.setText(f'{self.channel_text}')

    
    def channel_0(self) -> None:
        '''
        Method for setting the channel to 0
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 0
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'DirectTV'
            self.tv_view.setText(f'{self.channel_text}')

    def channel_1(self) -> None:
        '''
        Method for setting the channel to 1
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 1
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'NBC'
            self.tv_view.setText(f'{self.channel_text}')

    def channel_2(self) -> None:
        '''
        Method for setting the channel to 2
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 2
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'FOX'
            self.tv_view.setText(f'{self.channel_text}')

    def channel_3(self) -> None:
        '''
        Method for setting the channel to 3
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 3
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'USA'
            self.tv_view.setText(f'{self.channel_text}')
        
    def channel_4(self) -> None:
        '''
        Method for setting the channel to 4
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 4
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'ABC'
            self.tv_view.setText(f'{self.channel_text}')

    def channel_5(self) -> None:
        '''
        Method for setting the channel to 5
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 5
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'ESPN'
            self.tv_view.setText(f'{self.channel_text}')

    def channel_6(self) -> None:
        '''
        Method for setting the channel to 6
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 6
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'CNN'
            self.tv_view.setText(f'{self.channel_text}')

    def channel_7(self) -> None:
        '''
        Method for setting the channel to 7
        '''
        if self.status:
            if self.guide_status:
                self.guide_status = False
            self.channel = 7
            font = QtGui.QFont()
            font.setPointSize(70)
            self.tv_view.setFont(font)
            self.channel_text = 'CBS'
            self.tv_view.setText(f'{self.channel_text}')

    def volume_up(self) -> None:
        '''
        Method for moving the volume value up one
        '''
        if self.status:
            self.muted = False

            if self.volume != self.MAX_VOLUME:
                self.volume += 1
                self.volume_level_label.setText(f'{self.volume}')

    def volume_down(self) -> None:
        '''
        Method for moving the volume value down one
        '''
        if self.status:
            self.muted = False
            if self.volume != self.MIN_VOLUME:
                self.volume -= 1
                self.volume_level_label.setText(f'{self.volume}')


