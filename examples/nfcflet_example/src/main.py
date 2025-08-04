import flet as ft
from nfcflet import readNFC

def main(page: ft.Page):
    page.title = "Leitor NFC"

    tag = ft.Text("Tag NFC: -")

    async def read_nfc(e):
        tag = await readNFC()

        tag.value = tag.value.replace("-", tag)

        page.update()

    btn = ft.ElevatedButton(
        text="Ler Tag NFC",
        on_click=read_nfc
    )

    page.add(
        ft.Container(
            control=[
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
