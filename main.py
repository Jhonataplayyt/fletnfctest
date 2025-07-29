import flet as ft
from flet import Page, PluginEvent

def main(page: Page):
    # Inicia a sessão NFC
    page.pubsub.publish("plugin:flet_nfc", {"method": "startSession"})

    # Manipulador de evento do plugin
    def on_nfc(e: PluginEvent):
        tag_id = e.data.get("event")
        print("Tag lida:", tag_id)
        page.controls.append(ft.Text(f"Tag NFC: {tag_id}"))
        page.update()

    page.plugin_event = on_nfc
    page.add(ft.ElevatedButton("Parar NFC", on_click=lambda e: 
        page.pubsub.publish("plugin:flet_nfc", {"method": "stopSession"})))

ft.app(target=main, assets_dir="assets", flutter_plugins=["flet_nfc"])
