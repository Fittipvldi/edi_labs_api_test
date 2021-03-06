import requests
import csv

response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/')
json = response.json()

# print(json)

norte = 0
nordeste = 0
sul = 0
sudeste = 0
centro_oeste = 0

for i in json:
    regiao = (i['regiao']['nome'])

    if regiao == 'Norte':
        norte += 1
    elif regiao == 'Nordeste':
        nordeste += 1
    elif regiao == 'Sul':
        sul += 1
    elif regiao == 'Sudeste':
        sudeste += 1
    else:
        centro_oeste += 1

print(f'Norte: {norte}, Nordeste: {nordeste}, Sul: {sul}, Sudeste: {sudeste}, Centro-Oeste: {centro_oeste}')

with open('qtd_regioes.csv', 'w', newline='') as file:
    the_writer = csv.writer(file, delimiter='|')

    the_writer.writerow(['Regiao', 'Qtd. Estados']) # header
    the_writer.writerow(['Norte', norte])
    the_writer.writerow(['Nordeste', nordeste])
    the_writer.writerow(['Sul', sul])
    the_writer.writerow(['Sudeste', sudeste])
    the_writer.writerow(['Centro-Oeste', centro_oeste])
