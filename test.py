import flet as ft
import api

ACCESS_TOKEN = None

def main(page: ft.Page):
    page.title = "Maquininha Digital no seu celular"

    txt_main = ft.Text("Faça seu negócio com uma Maquininha Digital com a api do Mercado Pago")

    def page_paymentsType(e):
        global ACCESS_TOKEN

        txt_reg.visible = False
        txtb_ACCESS_TOKEN.visible = False
        btn_reg.visible = False

        btn_qrcodePix.visible = True

        page.update()

        ACCESS_TOKEN = txtb_ACCESS_TOKEN.value

    def page_QRCodePix(e):
        btn_qrcodePix.visible = False

        txtb_pixVal.visible = True
        btn_payefe.visible = True

        page.update()
    
    def page_QRCodePixIMG(e):
        txtb_pixVal.visible = False
        btn_payefe.visible = False

        val = 0

        if "." in txtb_pixVal.value:
            val = float(txtb_pixVal.value)
        elif "," in txtb_pixVal.value:
            val = float(txtb_pixVal.value.replace(",", "."))
        else:
            val = float(txtb_pixVal.value)

        qr_code_base64 = api.qrcode_pix(float(val), ACCESS_TOKEN)

        if qr_code_base64:
            img_qrCode.src_base64 = qr_code_base64
            img_qrCode.visible = True
            page.update()



    # Page Registration
    txt_reg = ft.Text("Faça o seu cadastro aqui", visible=True)
    txtb_ACCESS_TOKEN = ft.TextField(label="Seu Access-Token do Mercado Pago", visible=True)
    btn_reg = ft.ElevatedButton("Entrar", on_click=page_paymentsType, visible=True)

    # Page Payments Type
    btn_qrcodePix = ft.ElevatedButton("QRCode Pix", on_click=page_QRCodePix, visible=False)

    # Page QRCode Pix Payment
    txtb_pixVal = ft.TextField(label="Valor do Pagamento", visible=False)
    btn_payefe = ft.ElevatedButton("Efetuar Pagamento", on_click=page_QRCodePixIMG, visible=False)

    # Page QRCode Pix Image
    img_qrCode = ft.Image(src="", width=300, height=300, visible=False)
    
    page.add(
        txt_main,
        txt_reg,
        txtb_ACCESS_TOKEN,
        btn_reg,
        btn_qrcodePix,
        txtb_pixVal,
        btn_payefe,
        img_qrCode,
    )

ft.app(target=main)