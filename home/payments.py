
# SDK do Mercado Pago
import mercadopago
# Adicione as credenciais
sdk = mercadopago.SDK("TEST-2660057787623497-042519-3b4d9f2d00767056b4773fd836409649-162016798")

request = {
	"items": [
		{
			"id": "1",
			"title": "Prime Portal Feedback",
			"description": "APlicação para feedback/ avaliações de clientes",
			"quantity": 1,
			"currency_id": "BRL",
			"unit_price": 39.90,
		},
	],
	
	"back_urls": {
		"success": "http://127.0.0.1:8000/aprovado/",
		
	},
	"auto_return": "approved",
    }

preference_response = sdk.preference().create(request)
preference = preference_response["response"]
print(preference)