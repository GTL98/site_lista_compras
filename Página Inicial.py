# --- Importar as bibliotecas --- #
import pandas as pd
from json import load
from PIL import Image
import streamlit as st
from tabela import tabela
from valores_reais import valores_reais

# --- Configuração da página --- #
favicon = Image.open('./imagem/logo.png')
st.set_page_config(
    page_title='Lista de Compras',
    page_icon=favicon,
    layout='wide'
)

# --- Título à página --- #
imagem = Image.open('./imagem/logo.png').resize((170, 170))
col_1, col_2 = st.columns((2, 1))
with col_1:
    st.title('Lista de compras')
with col_2:
    st.image(imagem)
st.write('---')

# --- Abrir o documento JSON --- #
try:
    with open('./lista/lista.json', 'r') as doc:
        dados = load(doc)
except ValueError:
    st.subheader('Não há itens na lista de compras.')
else:
    # --- Obter os itens do dicionário --- #
    itens = list(dados.keys())

    # --- Adicionar uma caixa de seleção para os itens --- #
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        item = st.selectbox(
            label='Escolha um item:',
            options=itens,
            placeholder='Selecione um item',
            index=None
        )

    # --- Adicionar uma caixa de texto para o valor real do item --- #
    with col_2:
        valor_real = st.text_input(
            label='Valor real:',
            placeholder='Digite o valor real do item'
        )

    # --- Adicionar o botão de envio do valor real --- #
    with col_3:
        st.write('\n')
        st.write('\n')
        enviar = st.button('Enviar')
    if enviar:
        valores_reais(item, valor_real)

    tabela(dados)
