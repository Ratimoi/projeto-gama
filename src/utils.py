def lerInteiro(mensagem: str) -> int:
    while True:
        valor = input(mensagem)
        try:
            return int(valor)
        except ValueError:
            print("Digite um número válido.")

def lerFloat():
    return

def lerString():
    return

def limparTerminal():
    return
