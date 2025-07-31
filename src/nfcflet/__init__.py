# src/nfcflet/__init__.py

from flet import Control

class Nfcflet(Control):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _get_control_name(self) -> str:
        return "nfcflet"

    async def read_nfc(self) -> str:
        return await self.invoke_method_async("readNFC")

    async def write_nfc(self, data: str) -> str:
        return await self.invoke_method_async("writeNFC", [data])

__all__ = ["Nfcflet"]
