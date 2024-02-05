def tratar_dados(dados: list):
    """
    Função responsável por tratar os dados.
    :param dados: Dados brutos.
    :return: Tupla com o item e valor, nessa ordem.
    """
    # --- Obter somente o itens e o valores --- #
    itens_bruto = [item for item in dados.split('\n') if item != '']

    # --- Obter somente os itens --- #
    itens = [item.split('-')[0].strip() for item in itens_bruto]

    # --- Obter somente o valores --- #
    valores = [float(valor.split('-')[1].strip().replace(',', '.')) for valor in itens_bruto]

    return itens, valores
