from arquivo import carregar_produtos
from crud import (
    cadastrar_produto,
    listar_produtos,
    buscar_produto,
    atualizar_produto,
    excluir_produto
)
from estoque import (
    entrada_estoque,
    saida_estoque,
    estoque_baixo,
    relatorio
)
from menu import exibir_menu
from util import limpar_tela, pausar


def main():
    """Função principal do sistema."""
    produtos = carregar_produtos()

    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            buscar_produto(produtos)
        elif opcao == "4":
            atualizar_produto(produtos)
        elif opcao == "5":
            excluir_produto(produtos)
        elif opcao == "6":
            entrada_estoque(produtos)
        elif opcao == "7":
            saida_estoque(produtos)
        elif opcao == "8":
            estoque_baixo(produtos)
        elif opcao == "9":
            relatorio(produtos)
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

        pausar()


if __name__ == "__main__":
    main()
