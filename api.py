import requests
import json
import uuid

def qrcode_pix(value: float, ACCESS_TOKEN: str):  
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Idempotency-Key": str(uuid.uuid4()),
    }

    payload = {
        "transaction_amount": value,
        "description": "Pagamento Pix QR Code",
        "payment_method_id": "pix",
        "payer": {
            "email": "opcional@email.com",
            "first_name": "opc",
            "last_name": "opc",
            "identification": {
                "type": "CPF",
                "number": "11144477735"
            },
            "address": {
                "zip_code": "103456",
                "street_name": "inexistente",
                "street_number": "12768",
                "neighborhood": "Inexistente",
                "city": "inexistente",
                "federal_unit": "Inexistente"
            }
        }
    }

    response = requests.post(
        "https://api.mercadopago.com/v1/payments",
        headers=headers,
        json=payload
    )

    data = response.json()

    try:
        return data["point_of_interaction"]["transaction_data"]["qr_code_base64"]
    except KeyError:
        print("⚠️ Erro: Estrutura inesperada na resposta da API:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        raise KeyError("A chave 'point_of_interaction' não foi encontrada na resposta da API.")