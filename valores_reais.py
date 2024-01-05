# --- Importar a biblioteca --- #
import json
import streamlit as st


def valores_reais(item: str, valor: str):
    """
    Função responsável por alimentar o JSON com o valor real do item.
    :param item: Item selecionado.
    :param valor: Valor real do item.
    """
    # --- Abrir o arquivo JSON --- #
    try:
        with open('lista/valores_reais.json', 'r') as doc_1:
            dados = json.load(doc_1)
    except ValueError:
        pass
    else:
        # --- Escrever no dicionário JSON --- #
        if valor != '':
            valor_float = float(valor.replace(',', '.'))
            dados[item] = valor_float

        # --- Atualizar o JSON dos preços reais --- #
        with open('lista/valores_reais.json', 'w') as doc_2:
            json.dump(
                dados,
                doc_2,
                indent=4
            )
