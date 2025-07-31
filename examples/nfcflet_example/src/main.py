import flet
from flet import app, Page, Text, ElevatedButton
from nfcflet import Nfcflet

def main(page: Page):
    page.title = "NFC Flet Demo"

    # 1) Create your NFC control
    nfc = Nfcflet()

    # 2) Add it to the page before calling any methods
    page.add(nfc)

    # 3) Wire up a button to scan/write NFC
    def on_scan(e):
        tag = nfc.read_nfc()
        page.add(Text(f"NFC Tag: {tag}"))
        page.update()

    def on_write(e):
        res = nfc.write_nfc("Hello NFC")
        page.add(Text(f"Write result: {res}"))
        page.update()

    page.add(
        ElevatedButton("Scan NFC", on_click=on_scan),
        ElevatedButton("Write NFC", on_click=on_write),
    )

    page.update()

if __name__ == "__main__":
    app(target=main)
