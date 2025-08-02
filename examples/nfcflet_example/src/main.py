import flet as ft
from nfcflet import Nfcflet

def main(page: ft.Page):
    # instância com texto inicial
    nfc = Nfcflet(text="Escaneie uma tag NFC!")
    print(nfc.readNFC())

    # em algum callback de leitura NFC:
    # nfc.text = "ID da tag: 04A224B1C2"
    # page.update()  # opcional, mas nfc.update() já envia só o evento de extensão

ft.app(
    target=main,
    assets_dir="client",
)
