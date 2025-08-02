from enum import Enum 
from typing import Any, Optional 
from flet.core.constrained_control import ConstrainedControl 
from flet.core.control import OptionalNumber 
from flet.core.types import ColorEnums, ColorValue 
class Nfcflet(ConstrainedControl): 
    def __init__( self, # # Control # 
        opacity: OptionalNumber = None, 
        tooltip: Optional[str] = None, 
        visible: Optional[bool] = None, 
        data: Any = None, 
        # # ConstrainedControl # 
        left: OptionalNumber = None, 
        top: OptionalNumber = None, 
        right: OptionalNumber = None, 
        bottom: OptionalNumber = None, 

        text: "ReadNFC"
        x=''
    ):
        ConstrainedControl.__init__( 
            self, 
            tooltip=tooltip, 
            opacity=opacity, 
            visible=visible, 
            data=data, 
            left=left, 
            top=top, 
            right=right, 
            bottom=bottom, 
        ) 
    
    def _get_control_name(self): 
        return "nfcflet"
    
    @property
    def text(self) -> Optional[str]:
        return self._get_attr("text")

    @text.setter
    def text(self, value: str):
        self._set_attr("text", value)
    
    @property
    def x(self) -> Optional[str]:
        return self._get_attr("x")

    @x.setter
    def x(self, value: str):
        self._set_attr("text", value)