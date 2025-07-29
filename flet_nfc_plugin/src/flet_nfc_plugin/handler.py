from flet.extension import PluginEventListener, PluginEvent

class NfcPlugin(PluginEventListener):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def on_event(self, e: PluginEvent):
        """
        Recebe → e.data:
          • chamadas Python → Flutter: {"method": "startSession" / "stopSession"}
          • eventos  Flutter → Python: {"event": "<tag_id>"}
        """
        data = e.data or {}

        # 1) Python solicitou ação no Flutter (iniciar / parar sessão NFC)
        if data.get("method") in ("startSession", "stopSession"):
            # dispara o método no lado Flutter
            # o próprio runtime Flet se encarrega de enviar esse payload para a camada native
            e.call(data)

        # 2) Flutter notificou que leu uma tag NFC
        elif data.get("event"):
            tag_id = data["event"]
            # dispara evento na página Python (main.py), acessível via page.plugin_event
            self.page.dispatch_event("plugin:flet_nfc", {"event": tag_id})
