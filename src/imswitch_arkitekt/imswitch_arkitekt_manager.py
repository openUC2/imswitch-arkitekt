
from imswitch.imcontrol.view.guitools.ViewSetupInfo import ViewSetupInfo as SetupInfo
from imswitch.imcommon.framework import Signal, SignalInterface
from imswitch.imcommon.model import initLogger


class imswitch_arkitekt_manager(SignalInterface):
    sigSIMMaskUpdated = Signal(object)  # (maskCombined)

    def __init__(self, pluginInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__logger = initLogger(self)

        if pluginInfo is None:
            # import imswitch_sim_info.py
            return

        self.__pluginInfo = pluginInfo
        self.__wavelength = self.__pluginInfo.wavelength
        self.__pixelsize = self.__pluginInfo.pixelSize
        self.__angleMount = self.__pluginInfo.angleMount
        self.__simSize = (self.__pluginInfo.width, self.__pluginInfo.height)
        self.__patternsDir = self.__pluginInfo.patternsDir
        self.isSimulation = self.__pluginInfo.isSimulation
        self.nRotations = self.__pluginInfo.nRotations
        self.nPhases = self.__pluginInfo.nPhases
        self.simMagnefication = self.__pluginInfo.nPhases
        self.isFastAPISIM = self.__pluginInfo.isFastAPISIM
        self.simPixelsize = self.__pluginInfo.simPixelsize
        self.simNA = self.__pluginInfo.simNA
        self.simN = self.__pluginInfo.simN # refr
        self.simETA = self.__pluginInfo.simETA
