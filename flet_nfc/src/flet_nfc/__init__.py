import json
from typing import Callable, Any, Optional
from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber
from flet.core.types import ColorValue

class FletNfc(ConstrainedControl):
    def __init__(
        self,
        *,
        on_tag: Optional[Callable[[dict], Any]] = None,
        width: float | None = None,
        height: float | None = None,
        expand: bool = False,
        **kwargs
    ):
        # 1) Armazena callback
        self._on_tag = on_tag

        # 2) Chama super com handler do evento
        super().__init__(
            on_event=self._handle_event,
            width=width,
            height=height,
            expand=expand,
            **kwargs,
        )

    def _get_control_name(self):
        return "flet_nfc_ext"    # Deverá coincidir com o tipo no Dart

    def _handle_event(self, e):
        try:
            data = json.loads(e.data)
        except:
            data = e.data
        if callable(self._on_tag):
            self._on_tag(data)
