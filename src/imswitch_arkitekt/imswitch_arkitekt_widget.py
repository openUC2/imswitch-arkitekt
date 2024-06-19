from imswitch.imcontrol.view.widgets.basewidgets import Widget
import numpy as np
from typing import Any, Dict, List, Optional, Tuple

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class imswitch_arkitekt_widget(Widget):
    """Linked to CameraPluginWidget."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
