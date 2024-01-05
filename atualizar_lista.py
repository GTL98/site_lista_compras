# --- Importar a biblioteca --- #
from json import dumps


def atualizar_lista(itens: list, valores: list):
    """
    Função responsável por atualizar a lista de compras.
    :param itens: Itens da compra.
    :param valores: Valores dos itens.
    """
    # --- Criar o dicionário com os itens e valores --- #
    dados = {}

    # --- Iterar sobre cada item em conjunto com o valor --- #
    for item, valor in zip(itens, valores):
        # Adicionar o item e valor ao dicionário
        dados[item] = valor

    # --- Transformar o dicionário em JSON --- #
    dados_json = dumps(
        obj=dados,  # dicionário utilizado
        indent=4  # espaço da indentação
    )

    # --- Escrever no documento JSON --- #
    with open(f'./lista/lista.json', 'w') as doc:
        doc.write(dados_json)
