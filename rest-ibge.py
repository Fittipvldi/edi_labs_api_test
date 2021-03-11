import requests
import csv

try:
    response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/')

    if response.status_code == 200:
        dados = response.json()

        regioes = []

        for i in dados:
            regioes.append(i['regiao']['nome'])

        nome_regioes = set(regioes)

        with open('qtd_regioes.csv', 'w') as file:
            columns = ['Região', 'Quantidade'] # header
            escrever = csv.DictWriter(file, fieldnames=columns, delimiter='|', lineterminator='\n')
            escrever.writeheader() # escreve o header

            for regiao in sorted(nome_regioes): # sorted retorna em ordem alfabética
                escrever.writerow({'Região': regiao, 'Quantidade': regioes.count(regiao)})
    else:
        print(f'ERRO! {response.status_code}')
except Exception as erro:
    print(f"ERRO! {erro}")
