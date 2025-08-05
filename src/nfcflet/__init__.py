from enum import Enum 
from typing import Any, Optional, Callable
from flet.core.constrained_control import ConstrainedControl 
from flet.core.control import OptionalNumber 
from flet.core.types import ColorEnums, ColorValue 
import flet as ft
import asyncio

class Nfcflet(ConstrainedControl): 
    def __init__(
        self,
        text: str = "readNFC",
        x: str = "",
        on_result: Optional[Callable[[ft.ControlEvent], None]] = None,     

        # # Control # 
        opacity: OptionalNumber = None, 
        tooltip: Optional[str] = None, 
        visible: Optional[bool] = None, 
        data: Any = None, 
        # # ConstrainedControl # 
        left: OptionalNumber = None, 
        top: OptionalNumber = None, 
        right: OptionalNumber = None, 
        bottom: OptionalNumber = None, 
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

        self.text = text
        self.x = x

        self.on_event = on_result
    
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
        self._set_attr("x", value)
    
    @property
    def value(self) -> Optional[str]:
        return self._get_attr("value")
    
    @value.setter
    def value(self, value: str):
        self._set_attr("value", value)

def readNFC() -> str:
    text = ft.Text("")

    def _on_nfc(e: ft.ControlEvent, result: ft.Text):
        result.value = e.control.attrs.get("value", "without data")
        e.page.update()

    nfc = Nfcflet(
        text="readNFC",
        x="",
        on_result=lambda e: _on_nfc(e, text),
    )

    return text.value

def writeNFC(x: Any):
    text = ft.Text("")

    def _on_nfc(e: ft.ControlEvent, result: ft.Text):
        result.value = e.control.attrs.get("value", "without data")

        e.page.update()

    Nfcflet(
        text="writeNFC",
        x=x,
        on_result=lambda e: _on_nfc(e, text)
    )

    return text.value