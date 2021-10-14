import os
import sys
import requests

#
# TRATAR POSSÍVEIS ERROS
#

separador = '--------------------------------------------------------------------------------------------------------------------------'


def main(args):
    cnpj = args[1]
    if len(cnpj) != 14:
        print('Quantidade de dígitos inválida!')
        exit()

    r = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
    data = r.json()

    print(f'{separador}')

    print(f'CNPJ:                       {data["cnpj"]}')
    print(f'Razão Social:               {data["nome"]}')
    print(f'Nome Fantasia:              {data["fantasia"]}')

    print(f'{separador}')

    print(f'Tipo:                       {data["tipo"]}')
    print(f'Data Abertura:              {data["abertura"]}')
    print(f'Situação Cadastral:         {data["situacao"]}')
    print(f'Data Situação Cadastral:    {data["data_situacao"]}')
    print(f'Capital Social:             R${data["capital_social"]}')

    print(f'{separador}')

    print(f'Natureza Jurídica:          {data["natureza_juridica"]}')
    # print(f'Empresa MEI:                {data[""]}')

    print(f'{separador}')

    print(f'Logradouro:                 {data["logradouro"]}')
    print(f'Número:                     {data["numero"]}')
    print(f'Complemento:                {data["complemento"]}')
    print(f'CEP:                        {data["cep"]}')

    print(f'{separador}')

    print(f'Bairro:                     {data["bairro"]}')
    print(f'Município:                  {data["municipio"]}')
    print(f'UF:                         {data["uf"]}')

    print(f'{separador}')

    print(f'Telefone:                   {data["telefone"]}')
    print(f'E-mail:                     {data["email"]}')

    print(f'{separador}')

    return 0


if __name__ == '__main__':
    os.system('cls || clear')
    sys.exit(main(sys.argv))
