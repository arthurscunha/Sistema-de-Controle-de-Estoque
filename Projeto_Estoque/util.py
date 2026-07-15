import os


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """Pausa o programa até o usuário pressionar ENTER."""
    input("\nPressione ENTER para continuar...")


def ler_inteiro(mensagem):
    """Lê um número inteiro com validação."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Digite um valor maior ou igual a zero.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_float(mensagem):
    """Lê um número decimal com validação."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < 0:
                print("Digite um valor maior ou igual a zero.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Digite um número decimal.")


def buscar_por_codigo(produtos, codigo):
    """Busca um produto pelo código."""
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None
