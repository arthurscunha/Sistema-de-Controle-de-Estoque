from arquivo import salvar_produtos
from util import ler_float, ler_inteiro, buscar_por_codigo


def cadastrar_produto(produtos):
    """Cadastra um novo produto no estoque."""
    print("\n--- CADASTRAR PRODUTO ---")

    codigo = input("Código do produto: ").strip()

    if buscar_por_codigo(produtos, codigo):
        print("Já existe um produto com esse código.")
        return

    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria: ").strip()
    marca = input("Marca: ").strip()
    quantidade = ler_inteiro("Quantidade: ")
    unidade = input("Unidade (saco, metro, litro, unidade etc.): ").strip()
    preco_compra = ler_float("Preço de compra: R$ ")
    preco_venda = ler_float("Preço de venda: R$ ")

    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "marca": marca,
        "quantidade": quantidade,
        "unidade": unidade,
        "preco_compra": preco_compra,
        "preco_venda": preco_venda
    }

    produtos.append(produto)
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")


def listar_produtos(produtos):
    """Lista todos os produtos cadastrados."""
    print("\n--- LISTA DE PRODUTOS ---")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print("-" * 40)
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Marca: {produto['marca']}")
        print(f"Quantidade: {produto['quantidade']} {produto['unidade']}")
        print(f"Preço de compra: R$ {produto['preco_compra']:.2f}")
        print(f"Preço de venda: R$ {produto['preco_venda']:.2f}")


def buscar_produto(produtos):
    """Busca produto por código ou nome."""
    print("\n--- BUSCAR PRODUTO ---")
    termo = input("Digite o código ou nome do produto: ").strip().lower()

    encontrados = []
    for produto in produtos:
        if termo in produto["codigo"].lower() or termo in produto["nome"].lower():
            encontrados.append(produto)

    if not encontrados:
        print("Nenhum produto encontrado.")
        return

    for produto in encontrados:
        print("-" * 40)
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']} {produto['unidade']}")
        print(f"Preço de venda: R$ {produto['preco_venda']:.2f}")


def atualizar_produto(produtos):
    """Atualiza os dados de um produto existente."""
    print("\n--- ATUALIZAR PRODUTO ---")
    codigo = input("Digite o código do produto: ").strip()
    produto = buscar_por_codigo(produtos, codigo)

    if not produto:
        print("Produto não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")

    nome = input(f"Nome atual ({produto['nome']}): ").strip()
    categoria = input(f"Categoria atual ({produto['categoria']}): ").strip()
    marca = input(f"Marca atual ({produto['marca']}): ").strip()
    unidade = input(f"Unidade atual ({produto['unidade']}): ").strip()

    if nome:
        produto["nome"] = nome
    if categoria:
        produto["categoria"] = categoria
    if marca:
        produto["marca"] = marca
    if unidade:
        produto["unidade"] = unidade

    alterar_quantidade = input("Deseja alterar a quantidade? (s/n): ").strip().lower()
    if alterar_quantidade == "s":
        produto["quantidade"] = ler_inteiro("Nova quantidade: ")

    alterar_compra = input("Deseja alterar o preço de compra? (s/n): ").strip().lower()
    if alterar_compra == "s":
        produto["preco_compra"] = ler_float("Novo preço de compra: R$ ")

    alterar_venda = input("Deseja alterar o preço de venda? (s/n): ").strip().lower()
    if alterar_venda == "s":
        produto["preco_venda"] = ler_float("Novo preço de venda: R$ ")

    salvar_produtos(produtos)
    print("Produto atualizado com sucesso!")


def excluir_produto(produtos):
    """Remove um produto do estoque."""
    print("\n--- EXCLUIR PRODUTO ---")
    codigo = input("Digite o código do produto: ").strip()
    produto = buscar_por_codigo(produtos, codigo)

    if not produto:
        print("Produto não encontrado.")
        return

    confirmacao = input(f"Tem certeza que deseja excluir {produto['nome']}? (s/n): ").strip().lower()

    if confirmacao == "s":
        produtos.remove(produto)
        salvar_produtos(produtos)
        print("Produto excluído com sucesso!")
    else:
        print("Exclusão cancelada.")
