import requests

url = "https://api.portaldatransparencia.gov.br/api-de-dados/novo-bolsa-familia-sacado-por-nis"
headers = {
    "chave-api-dados": "36d3205cace845b28a3c7b97014a3a3d"
}
params = {
    "nis": "12463573564",
    "anoMesReferencia": "202401",
    "anoMesCompetencia": "202312",
    "pagina": "1"
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    # Faça o que precisar com os dados retornados
    print(data)
else:
    print("Erro ao acessar a API:", response.status_code)
