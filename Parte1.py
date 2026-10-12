def ler_inteiro(mensagem="Digite um valor inteiro valido: "):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")


# Verifica manualmente se um elemento pertence ao conjunto
def pertence(conjunto, valor):
    for elemento in conjunto:
        if elemento == valor:
            return True

    return False


# Verifica manualmente se todos os elementos de A estao em B
def esta_contido(A, B):
    for elemento in A:
        if not pertence(B, elemento):
            return False

    return True


# Verifica se A e um subconjunto proprio de B
# Ou seja: A esta contido em B, mas A e diferente de B
def subconjunto_proprio(A, B):
    return esta_contido(A, B) and not esta_contido(B, A)


def ler_conjunto(nome):
    conjunto = []

    quantidade = ler_inteiro(
        f"Quantos elementos tera o conjunto {nome}? "
    )

    while quantidade < 0:
        print("A quantidade nao pode ser negativa.")
        quantidade = ler_inteiro(
            f"Quantos elementos tera o conjunto {nome}? "
        )

    for i in range(quantidade):
        elemento = ler_inteiro(
            f"Digite o {i + 1}º elemento de {nome}: "
        )

        # Garante que nao existam elementos repetidos
        if not pertence(conjunto, elemento):
            conjunto.append(elemento)
        else:
            print("Elemento repetido. Ele sera ignorado.")

    # Mantem os elementos ordenados
    conjunto.sort()

    return conjunto


def uniao(A, B):
    caixa_result = []

    for x in A:
        if not pertence(caixa_result, x):
            caixa_result.append(x)

    for x in B:
        if not pertence(caixa_result, x):
            caixa_result.append(x)

    caixa_result.sort()

    return caixa_result


def intersecao(A, B):
    caixa_result = []

    for x in A:
        if pertence(B, x):
            caixa_result.append(x)

    caixa_result.sort()

    return caixa_result


def diferenca(A, B):
    caixa_result = []

    for x in A:
        if not pertence(B, x):
            caixa_result.append(x)

    caixa_result.sort()

    return caixa_result


def diferenca_simetrica(A, B):
    u = uniao(A, B)
    i = intersecao(A, B)

    return diferenca(u, i)


def complemento(U, A):
    return diferenca(U, A)


def verificar_pertinencia(A, B):
    elemento = ler_inteiro(
        "Digite um elemento para verificar: "
    )

    print(f"{elemento} pertence a A? {pertence(A, elemento)}")
    print(f"{elemento} pertence a B? {pertence(B, elemento)}")


def verificar_inclusao(A, B):
    print(f"A esta contido em B (A ⊆ B)? "
          f"{esta_contido(A, B)}")

    print(f"A esta estritamente contido em B (A ⊂ B)? "
          f"{subconjunto_proprio(A, B)}")

    print(f"B esta contido em A (B ⊆ A)? "
          f"{esta_contido(B, A)}")

    print(f"B esta estritamente contido em A (B ⊂ A)? "
          f"{subconjunto_proprio(B, A)}")


def comparar_nativo(A, B):
    # Esta funcao usa os operadores nativos SOMENTE
    # para validar os resultados das funcoes manuais.

    A_nativo = set(A)
    B_nativo = set(B)

    comparacoes = [
        (
            "Uniao",
            uniao(A, B),
            sorted(A_nativo | B_nativo)
        ),
        (
            "Intersecao",
            intersecao(A, B),
            sorted(A_nativo & B_nativo)
        ),
        (
            "Diferenca A - B",
            diferenca(A, B),
            sorted(A_nativo - B_nativo)
        ),
        (
            "Diferenca B - A",
            diferenca(B, A),
            sorted(B_nativo - A_nativo)
        ),
        (
            "Diferenca simetrica",
            diferenca_simetrica(A, B),
            sorted(A_nativo ^ B_nativo)
        ),
        (
            "A contido em B (A ⊆ B)",
            esta_contido(A, B),
            A_nativo.issubset(B_nativo)
        ),
        (
            "A estritamente contido em B (A ⊂ B)",
            subconjunto_proprio(A, B),
            A_nativo < B_nativo
        ),
        (
            "B contido em A (B ⊆ A)",
            esta_contido(B, A),
            B_nativo.issubset(A_nativo)
        ),
        (
            "B estritamente contido em A (B ⊂ A)",
            subconjunto_proprio(B, A),
            B_nativo < A_nativo
        )
    ]

    print("\n=== COMPARACAO: MANUAL X NATIVA ===")

    for nome, resultado_manual, resultado_nativo in comparacoes:
        print(f"\n{nome}:")
        print(f"Resultado manual: {resultado_manual}")
        print(f"Resultado nativo: {resultado_nativo}")

        if resultado_manual == resultado_nativo:
            print("Validacao: OK")
        else:
            print("Validacao: ERRO")


def mostrar_conjunto(A, B):
    print(f"A = {A}")
    print(f"B = {B}")


def main():
    print("=== PARTE 1 - TEORIA DOS CONJUNTOS ===")

    A = ler_conjunto("A")
    B = ler_conjunto("B")

    executando = True

    while executando:
        print("\n=== MENU ===")
        print("1 - Uniao (A U B)")
        print("2 - Intersecao (A ∩ B)")
        print("3 - Diferenca (A - B)")
        print("4 - Diferenca (B - A)")
        print("5 - Diferenca simetrica")
        print("6 - Verificar pertinencia")
        print("7 - Mostrar cardinalidade")
        print("8 - Informar universo e calcular complementos")
        print("9 - Mostrar os conjuntos")
        print("10 - Verificar inclusao")
        print("11 - Comparar resultados manuais e nativos")
        print("0 - Sair")

        opcao = ler_inteiro("Escolha uma opcao: ")

        if opcao == 1:
            print(f"A U B = {uniao(A, B)}")

        elif opcao == 2:
            print(f"A ∩ B = {intersecao(A, B)}")

        elif opcao == 3:
            print(f"A - B = {diferenca(A, B)}")

        elif opcao == 4:
            print(f"B - A = {diferenca(B, A)}")

        elif opcao == 5:
            print(f"A △ B = {diferenca_simetrica(A, B)}")

        elif opcao == 6:
            verificar_pertinencia(A, B)

        elif opcao == 7:
            print(f"|A| = {len(A)}")
            print(f"|B| = {len(B)}")

        elif opcao == 8:
            while True:
                U = ler_conjunto("U (universo)")

                if esta_contido(A, U) and esta_contido(B, U):
                    break

                print(
                    "Erro: o universo deve conter todos "
                    "os elementos de A e B."
                )
                print("Informe o universo novamente.")

            print(f"U = {U}")
            print(f"Complemento de A = {complemento(U, A)}")
            print(f"Complemento de B = {complemento(U, B)}")

        elif opcao == 9:
            mostrar_conjunto(A, B)

        elif opcao == 10:
            verificar_inclusao(A, B)

        elif opcao == 11:
            comparar_nativo(A, B)

        elif opcao == 0:
            executando = False
            print("Programa encerrado.")

        else:
            print("Opcao invalida. Escolha uma opcao do menu.")


if __name__ == "__main__":
    main()