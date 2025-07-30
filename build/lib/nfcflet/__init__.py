from typing import Any, Callable, Optional
from flet.core.constrained_control import ConstrainedControl

class NFCControl(ConstrainedControl):
    def __init__(
        self,
        on_response: Optional[Callable] = None,
    ):
        super().__init__()
        self.on_response = on_response

    def call_flutter(self, payload: Any):
        self._set_attr("request_payload", payload)

    @property
    def on_response(self) -> Optional[Callable]:
        return self._get_event_handler("response")

    @on_response.setter
    def on_response(self, handler: Callable):
        self._add_event_handler("response", handler)

    def _get_control_name(self) -> str:
        return "nfcflet"
