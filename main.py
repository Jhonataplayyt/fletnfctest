import flet as ft

def main(page: ft.Page):
    # Inicia a sessão NFC
    page.pubsub.publish("plugin:flet_nfc", {"method": "startSession"})

    # Manipulador de evento do plugin
    # Não precisamos importar PluginEvent — basta receber 'e'
    def on_nfc(e):
        # 'e.data' já contém o payload do plugin
        tag_id = e.data.get("event")
        print("Tag lida:", tag_id)
        page.controls.append(ft.Text(f"Tag NFC: {tag_id}"))
        page.update()

    # Registra o handler
    page.plugin_event = on_nfc

    # Botão para encerrar a sessão NFC
    page.add(
        ft.ElevatedButton(
            "Parar NFC",
            on_click=lambda _: page.pubsub.publish("plugin:flet_nfc", {"method": "stopSession"})
        )
    )

ft.app(
    target=main,
    assets_dir="assets",
)

