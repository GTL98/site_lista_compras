# --- Importar a biblioteca --- #
from json import load
import streamlit as st


def tabela(dados: dict):
    """
    Função responsável por escrever a tabela com os itens, valor especulado e valor real.
    :param dados: Dicionário com os itens e valores.
    """
    # --- Obter os itens do dicionário --- #
    itens = list(dados.keys())

    # --- Criar as colunas --- #
    col_1, col_2, col_3 = st.columns(3)

    # --- Escrever o cabeçalho da tabela --- #
    with col_1:
        st.subheader('Itens')
    with col_2:
        st.subheader('Valor estimado')
    with col_3:
        st.subheader('Valor real')

    # --- Colocar os itens, valores especulados e valores reais --- #
    for item in itens:
        with col_1:
            st.write(item)
        with col_2:
            st.write(str(dados[item]).replace('.', ','))
        with col_3:
            with open('./lista/valores_reais.json', 'r') as doc:
                dados_json = load(doc)
            if item in dados_json.keys():
                st.write(str(dados_json[item]).replace('.', ','))
            else:
                st.write('0,00')

    # --- Colocar o total de itens e valor especulado --- #
    with col_1:
        st.subheader(f'Total: {len(itens)}')
    with col_2:
        total_especulado = round(0, 2)
        for item in itens:
            valor_item_especulado = float(dados[item])
            total_especulado += valor_item_especulado
        if len(itens) == 0:
            pass
        else:
            media_especulada = round(total_especulado/len(itens), 2)
            st.subheader(f'Total: R$ {str(total_especulado).replace(".", ",")} '
                         f'({str(media_especulada).replace(".", ",")} por produto)')

    # --- Colocar o total do valor real --- #
    with col_3:
        with open('./lista/valores_reais.json', 'r') as doc:
            dados_json = load(doc)
        total_real = round(0, 2)
        for item in dados_json:
            valor_item_real = float(dados_json[item])
            total_real += valor_item_real
        # Obter a quantidade de itens nos valores reais
        itens_reais = [item for item in dados_json if item != 'temp']
        if len(itens_reais) == 0:
            pass
        else:
            media_real = round(total_real / len(itens_reais), 2)
            st.subheader(f'Total: R$ {str(total_real).replace(".", ",")} '
                         f'({str(media_real).replace(".", ",")} por produto)')
