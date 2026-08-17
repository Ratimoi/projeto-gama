from menu import (
    menuInicial,
    menuSelecaoArquivo,
    menuEstatisticas,
)

df = menuSelecaoArquivo()

if df is not None:
    while True:
        opcao = menuInicial()

        if opcao == 1:
            novoDf = menuSelecaoArquivo()
            if novoDf is not None:
                df = novoDf
        elif opcao == 2:
            menuEstatisticas(df)
        elif opcao == 0:
            break
        else:
            print("Opção inválida.")
