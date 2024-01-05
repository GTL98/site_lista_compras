# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st
from tratar_dados import tratar_dados
from adicionar_itens import adicionar_itens

# --- Configuração da página --- #
favicon = Image.open('./imagem/logo.png')
st.set_page_config(
    page_title='Adicionar',
    page_icon=favicon,
    layout='wide'
)

# --- Adicionar um título à página --- #
st.title('Adicionar compras')
st.write('---')

# --- Adicionar uma observação --- #
st.subheader('Colocar os preços separados por espaço e dois ENTER após cada produto adicionado.')
st.subheader('''Exemplo:
- Cebola 5,99
- Laranja 3,89''',
             divider='rainbow')

# --- Caixa para adicionar os itens de compra --- #
itens_compras = st.text_area(
    'Lista de compras',
    height=400
)

# --- Criar o botão para guardar os itens --- #
salvar = st.button('Salvar')

# --- Verificar se o botão foi clicado --- #
if salvar:
    itens, valores = tratar_dados(itens_compras)
    adicionar_itens(itens, valores)
    st.subheader('A lista de compras foi salva com sucesso!')
