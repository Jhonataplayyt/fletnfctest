import flet as ft
from flet_nfc.src.flet_nfc import FletNfc

def main(page: ft.Page):
    def on_tag(event):
        page.snack_bar = ft.SnackBar(ft.Text(f"ID NFC: {event['id']}"))
        page.snack_bar.open = True
        page.update()

    page.add(
        FletNfc(on_tag=on_tag, width=200, height=200, expand=True)
    )
    page.update()

ft.app(main)
