import flet as ft
from flet_nfc import NfcReader

def main(page: ft.Page):
    def on_tag(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Tag: {e.data['id']}"))
        page.snack_bar.open = True
        page.update()
    page.add(NfcReader(on_tag=on_tag))
    page.update()

ft.app(main)
