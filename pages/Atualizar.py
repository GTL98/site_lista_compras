# --- Importar as bibliotecas --- #
from json import load
from PIL import Image
import streamlit as st
from tratar_dados import tratar_dados
from atualizar_lista import atualizar_lista

# --- Configuração da página --- #
favicon = Image.open('./imagem/logo.png')
st.set_page_config(
    page_title='Atualizar',
    page_icon=favicon,
    layout='wide'
)

# --- Adicionar título à página --- #
st.title('Atualizar a lista de compras')
st.write('---')

# --- Adicionar observações --- #
st.subheader('Nesta página você poderá atualizar a sua lista de compras.', divider='rainbow')

# --- Obter os itens e valores do arquivo JSON --- #
try:
    with open('./lista/lista.json', 'r') as doc:
        dados_json = load(doc)
except ValueError:
    st.subheader('Não há lista de compras criada.')
else:

    # --- Criar uma variável para armazenar a string dos itens e valores --- #
    dados = ''

    for chave in dados_json.keys():
        dados += f'{chave} {dados_json[chave]}\n\n'

    # --- Adicionar a caixa de texto para atualizar a lista de compras --- #
    itens_compras = st.text_area('Atualizar a lista de compras:', height=400, value=dados)

    # --- Criar o botão para guardar os itens --- #
    atualizar = st.button('Atualizar')

    # --- Verificar se o botão foi clicado --- #
    if atualizar:
        itens, valores = tratar_dados(itens_compras)
        atualizar_lista(itens, valores)
        st.subheader('A lista de compras foi atualizada com sucesso!')
