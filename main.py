import flet
from flet_nfc import NfcReader

def main(page: flet.Page):
    def on_tag(e):
        page.snack_bar = flet.SnackBar(flet.Text(f"Tag lida: {e.data['id']}"))
        page.snack_bar.open = True
        page.update()

    page.add(NfcReader(on_tag=on_tag))
    page.update()

if __name__ == "__main__":
    flet.app(target=main)
