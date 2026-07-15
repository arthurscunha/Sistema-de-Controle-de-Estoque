from arquivo import salvar_produtos
from util import ler_inteiro, buscar_por_codigo


def entrada_estoque(produtos):
    """Adiciona quantidade ao estoque de um produto."""
    print("\n--- ENTRADA DE ESTOQUE ---")
    codigo = input("Código do produto: ").strip()
    produto = buscar_por_codigo(produtos, codigo)

    if not produto:
        print("Produto não encontrado.")
        return

    quantidade = ler_inteiro("Quantidade recebida: ")
    produto["quantidade"] += quantidade
    salvar_produtos(produtos)

    print("Entrada registrada com sucesso!")
    print(f"Nova quantidade: {produto['quantidade']} {produto['unidade']}")


def saida_estoque(produtos):
    """Remove quantidade do estoque de um produto."""
    print("\n--- SAÍDA DE ESTOQUE ---")
    codigo = input("Código do produto: ").strip()
    produto = buscar_por_codigo(produtos, codigo)

    if not produto:
        print("Produto não encontrado.")
        return

    quantidade = ler_inteiro("Quantidade vendida: ")

    if quantidade > produto["quantidade"]:
        print("Estoque insuficiente.")
        return

    produto["quantidade"] -= quantidade
    salvar_produtos(produtos)

    print("Saída registrada com sucesso!")
    print(f"Quantidade restante: {produto['quantidade']} {produto['unidade']}")


def estoque_baixo(produtos):
    """Mostra produtos com quantidade menor que 10."""
    print("\n--- PRODUTOS COM ESTOQUE BAIXO ---")
    encontrados = False

    for produto in produtos:
        if produto["quantidade"] < 10:
            encontrados = True
            print("-" * 40)
            print(f"Código: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']} {produto['unidade']}")

    if not encontrados:
        print("Nenhum produto com estoque baixo.")


def relatorio(produtos):
    """Exibe um relatório geral do estoque."""
    print("\n--- RELATÓRIO DO ESTOQUE ---")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    total_produtos = len(produtos)
    total_itens = sum(produto["quantidade"] for produto in produtos)
    valor_total = sum(produto["quantidade"] * produto["preco_venda"] for produto in produtos)
    lucro_potencial = sum(
        produto["quantidade"] * (produto["preco_venda"] - produto["preco_compra"])
        for produto in produtos
    )

    produto_mais_caro = max(produtos, key=lambda produto: produto["preco_venda"])
    produto_mais_barato = min(produtos, key=lambda produto: produto["preco_venda"])

    print(f"Total de produtos cadastrados: {total_produtos}")
    print(f"Quantidade total de itens: {total_itens}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")
    print(f"Lucro potencial estimado: R$ {lucro_potencial:.2f}")
    print(f"Produto mais caro: {produto_mais_caro['nome']} - R$ {produto_mais_caro['preco_venda']:.2f}")
    print(f"Produto mais barato: {produto_mais_barato['nome']} - R$ {produto_mais_barato['preco_venda']:.2f}")
