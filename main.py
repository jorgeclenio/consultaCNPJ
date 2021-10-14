import os
import sys
import requests

separador = '====================================================================='


def main(args):
    cnpj = args[1]
    if len(cnpj) != 14:
        print(f'{separador}\n| Quantidade de dígitos inválida!\n{separador}')
        exit()

    r = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
    data = r.json()
    if 'ERROR' not in data["status"]:
        print(f'{separador}\n| CNPJ: {data["cnpj"]}\n| Razão Social: {data["nome"]}\n| Nome Fantasia: {data["fantasia"]}\n{separador}\n| Tipo: {data["tipo"]}\n| Data Abertura: {data["abertura"]}\n| Situação Cadastral: {data["situacao"]}\n| Data Situação Cadastral: {data["data_situacao"]}\n| Data Situação Cadastral: {data["data_situacao"]}\n| Capital Social: R${data["capital_social"]}\n{separador}\n| Natureza Jurídica: {data["natureza_juridica"]}\n{separador}\n| Logradouro: {data["logradouro"]}\n| Número: {data["numero"]}\n| Complemento: {data["complemento"]}\n| CEP: {data["cep"]}\n{separador}\n| Bairro: {data["bairro"]}\n| Município: {data["municipio"]}\n| UF: {data["uf"]}\n{separador}\n| Telefone: {data["telefone"]}\n| E-mail: {data["email"]}\n{separador}')
    else:
        print('{}'.format(data["message"]))
    return 0


if __name__ == '__main__':
    os.system('cls || clear')
    sys.exit(main(sys.argv))
