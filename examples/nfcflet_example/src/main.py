import flet as ft
from nfcflet import readNFC

def main(page: ft.Page):
    page.title = "Leitor NFC"

    tag = ft.Text("Tag NFC: -")

    def read_nfc(e):
        tag_nfc = readNFC(page)

        tag.value = tag_nfc

        page.update()

    btn = ft.ElevatedButton(
        text="Ler Tag NFC",
        on_click=read_nfc
    )

    page.add(
        ft.Column(
            controls=[
                tag,
                btn,
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True
        )
    )

ft.app(
    target=main,
)
