from imswitch.imcontrol.view.widgets.basewidgets import Widget
from imswitch.imcommon.model import initLogger
from arkitekt.qt.magic_bar import MagicBar
from arkitekt.builders import publicscheduleqt
import numpy as np
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass
from qtpy import QtCore, QtWidgets

global_app = None
class imswitch_arkitekt_widget(Widget):
    """Linked to the Arkitekt Controller ."""

    sigLoadParamsFromHDF5 = QtCore.Signal()
    sigPickSetup = QtCore.Signal()
    sigClosing = QtCore.Signal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # initialize the logger
        self.__logger = initLogger(self)
        self.__logger.debug("Initializing")

        # create the main widget layout
        self.cwidget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        self.cwidget.setLayout(layout)
        
        # Initialize the Magic Bar (Arkitekt) to have the menu available
        identifier = "github.io.jhnnsrs.mikro-napari"
        version = "latest"
        logo = "https://avatars.githubusercontent.com/u/127734217?s=200&v=4"
        settings = QtCore.QSettings("imswitch", f"{identifier}:{version}")
        self.global_app = publicscheduleqt(
            identifier, version, parent=self.cwidget, logo=logo, settings=settings
        )
        self.magic_bar = MagicBar(self.global_app, dark_mode=True)


        self.loadParamsAction = QtWidgets.QAction(
            "Load parameters from saved HDF5 file…", self
        )

        # Buttons
        self.loadParamsButton = QtWidgets.QPushButton("Load Parameters")
        self.loadParamsButton.clicked.connect(self.sigLoadParamsFromHDF5.emit)
        
        self.pickSetupButton = QtWidgets.QPushButton("Pick Setup")
        self.pickSetupButton.clicked.connect(self.sigPickSetup.emit)

        self.fileSelectButton = QtWidgets.QPushButton("Select File")
        self.fileSelectButton.clicked.connect(self.sigPickSetup.emit)
        
        # Adding widgets to layout
        layout.addWidget(self.magic_bar)
        layout.addWidget(self.loadParamsButton)
        layout.addWidget(self.pickSetupButton)
        layout.addWidget(self.fileSelectButton)
        layout.addStretch()

        self.setLayout(layout)
        


@dataclass
class _DockInfo:
    name: str
    yPosition: int
