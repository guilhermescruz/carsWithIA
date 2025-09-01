import os
from mistralai import Mistral

api_key = os.getenv("MISTRAL_API_KEY")
model = os.getenv("MISTRAL_MODEL", "mistral-tiny")

if not api_key:
    raise ValueError("MISTRAL_API_KEY não encontrada nas variáveis de ambiente")

client = Mistral(api_key=api_key)

def get_car_ai_bio(brand, year, model_name):
    prompt = f"Escreva uma biografia para um carro da marca {brand}, ano {year}, modelo {model_name}, em apenas 250 caracteres."

    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing automotivo."},
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content.strip()