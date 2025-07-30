import flet as ft

from nfcflet import NFCControl

def main(page: ft.Page):
    page.title = "Teste  de leitura NFC"

    nfc = NFCControl()

    def handle_nfc_response(event):
        tag_id = event.data.get("id", "desconhecido")
        text.value = f"ID da tag: {tag_id}"
        page.update()

    text = ft.Text("tag id: -")

    btn = ft.ElevatedButton(
        "Escanear NFC",
        on_click=lambda e: nfc.call_flutter({})
    )


    nfc.on_response = handle_nfc_response

    page.add(
        text,
        btn
    )


ft.app(main)
