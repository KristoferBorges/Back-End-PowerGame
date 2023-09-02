import pandas as pd
from app import path
import openpyxl

# Informações de coleta
"""
Multiplicador
Pontos
Batalhas
ValorAcumulado
Resultado
"""


def colletData(item, multiplicador, pontos, batalhas, valorApostado, valorAcumulado, resultado):
    try:
        """print('Coletando dados...')
        print('Item: ', item)
        print('Multiplicador: ', multiplicador)
        print('Pontos: ', pontos)
        print('Batalhas: ', batalhas)
        print('Valor Apostado: ', valorApostado)
        print('Valor Acumulado: ', valoracumulado)
        print('Resultado: ', resultado)"""

        # Carrega o arquivo excel
        df_storage = pd.read_excel(path)

        # Cria um dicionário com os dados
        novoDado = {
            'Item': item,
            'Multiplicador' : float(multiplicador),
            'Pontos': pontos,
            'Batalhas': batalhas,
            'ValorApostado': float(valorApostado),
            'ValorAcumulado': float(valorAcumulado),
            'Resultado': resultado
        }

        # Insere os dados no dataframe
        df_storage.loc[len(df_storage)] = novoDado

        # Salva o arquivo
        df_storage.to_excel(path, index=False)

    except Exception as error:
        print(error)



