import json
import os

ARQUIVO_PRODUTOS = "produtos.json"


def carregar_produtos():
    """Carrega os produtos salvos no arquivo JSON."""
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return []

    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return []


def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo JSON."""
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
