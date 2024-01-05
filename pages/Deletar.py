# --- Importar a biblioteca --- #
import json
from PIL import Image
import streamlit as st

# --- Configuração da página --- #
favicon = Image.open('./imagem/logo.png')
st.set_page_config(
    page_title='Deletar',
    page_icon=favicon,
    layout='wide'
)

# --- Título à página --- #
st.title('Deletar lista')
st.write('---')

# --- Observação --- #
st.subheader(
    'Aqui você deletará somente os valores reais.',
    divider='rainbow'
)

# --- Botão de deletar as lista de compras --- #
col_1, col_2, col_3, col_4, col_5 = st.columns(5)
with col_3:
    deletar = st.button('Deletar')
if deletar:
    with open('./lista/valores_reais.json', 'w') as doc_2:
        dados_temp = {'temp': 0}
        dados_temp_json = json.dumps(
            obj=dados_temp,
            indent=4
        )
        doc_2.write(dados_temp_json)
    st.subheader('Lista de compras deleta com sucesso!')