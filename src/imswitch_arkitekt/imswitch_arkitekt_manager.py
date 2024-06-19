
from imswitch.imcontrol.view.guitools.ViewSetupInfo import ViewSetupInfo as SetupInfo
from imswitch.imcommon.framework import Signal, SignalInterface
from imswitch.imcommon.model import initLogger


class imswitch_arkitekt_manager(SignalInterface):
    sigSIMMaskUpdated = Signal(object)  # (maskCombined)

    def __init__(self, pluginInfo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__logger = initLogger(self)

        self.global_app = None
        
        if pluginInfo is None:
            # import imswitch_sim_info.py
            return

    def set_global_app(self, app):
        self.global_app = app