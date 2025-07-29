import flet as ft

def main(page: ft.Page):
    page.title = "Leitor NFC Flet"
    page.padding = 20

    status = ft.Text("Inicializando...", size=16)
    output = ft.Text("Aguardando tag...", multiline=True, height=120)
    scan_btn = ft.ElevatedButton("Escanear NFC")
    page.add(status, scan_btn, output)
    page.update()

    try:
        from jnius import autoclass, cast
        from android import activity
        from android.runnable import run_on_ui_thread
    except ImportError:
        status.value = "NFC não suportado nesta plataforma"
        page.update()
        return

    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    act = PythonActivity.mActivity
    NfcAdapter = autoclass("android.nfc.NfcAdapter").getDefaultAdapter(act)
    if not NfcAdapter:
        status.value = "NFC não disponível neste dispositivo"
        page.update()
        return

    Intent = autoclass("android.content.Intent")
    PendingIntent = autoclass("android.app.PendingIntent")
    IntentFilter = autoclass("android.content.IntentFilter")
    Ndef = autoclass("android.nfc.tech.Ndef")

    intent = Intent(act, act.getClass())
    intent.addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP)
    pi = PendingIntent.getActivity(act, 0, intent, 0)

    filters = []
    for action in (
        NfcAdapter.ACTION_NDEF_DISCOVERED,
        NfcAdapter.ACTION_TECH_DISCOVERED,
        NfcAdapter.ACTION_TAG_DISCOVERED,
    ):
        f = IntentFilter(action)
        f.addCategory(Intent.CATEGORY_DEFAULT)
        try:
            f.addDataType("*/*")
        except:
            pass
        filters.append(f)

    @run_on_ui_thread
    def enable_dispatch():
        NfcAdapter.enableForegroundDispatch(act, pi, filters, None)

    @run_on_ui_thread
    def disable_dispatch():
        NfcAdapter.disableForegroundDispatch(act)

    def on_new_intent(intent):
        tag = intent.getParcelableExtra(NfcAdapter.EXTRA_TAG)
        if not tag:
            return

        ndef = cast("android.nfc.tech.Ndef", Ndef.get(tag))
        ndef.connect()
        msg = ndef.getCachedNdefMessage()
        payload = ""
        if msg:
            recs = msg.getRecords()
            if recs:
                pl = recs[0].getPayload()
                payload = bytearray(pl[1:]).decode("utf-8", "ignore")
        ndef.close()

        uid = ":".join(f"{b:02X}" for b in tag.getId())
        output.value = f"UID: {uid}\nPayload: {payload}"
        page.update()

        disable_dispatch()
        activity.unbind(on_new_intent=on_new_intent)

    def scan(_):
        status.value = "Aproxime a tag NFC…"
        page.update()
        activity.bind(on_new_intent=on_new_intent)
        enable_dispatch()

    scan_btn.on_click = scan

    status.value = "Pronto para escanear"
    page.update()

if __name__ == "__main__":
    ft.app(target=main)