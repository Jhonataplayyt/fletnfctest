from flet.core.constrained_control import ConstrainedControl
from flet.core.event_handler import EventHandler

class NfcReader(ConstrainedControl):
    def __init__(
        self,
        on_tag_discovered: EventHandler = None,
        tooltip: str = None,
        **kwargs
    ):
        super().__init__(tooltip=tooltip, **kwargs)
        self.on_tag_discovered = on_tag_discovered

    def _get_control_name(self):
        return "nfc_reader"
