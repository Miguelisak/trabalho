# PARTE 3 - SISTEMA DE RECOMENDACAO POR INTERESSES


# Verifica manualmente se um elemento existe em uma lista
def pertence(conjunto, valor):
    for elemento in conjunto:
        if elemento == valor:
            return True

    return False


# Le os interesses de um usuario e remove duplicatas
def ler_interesses(nome):
    interesses = []

    print(f"\nDigite os interesses de {nome}.")
    print("Separe os interesses por virgula.")
    print("Exemplo: rock, cinema, games, tecnologia")

    entrada = input("Interesses: ").strip().lower()

    for item in entrada.split(","):
        interesse = item.strip()

        if interesse != "":
            if not pertence(interesses, interesse):
                interesses.append(interesse)

    interesses.sort()

    return interesses


# Calcula a uniao de dois conjuntos
def uniao(A, B):
    resultado = []

    for elemento in A:
        if not pertence(resultado, elemento):
            resultado.append(elemento)

    for elemento in B:
        if not pertence(resultado, elemento):
            resultado.append(elemento)

    resultado.sort()

    return resultado


# Calcula a intersecao de dois conjuntos
def intersecao(A, B):
    resultado = []

    for elemento in A:
        if pertence(B, elemento):
            resultado.append(elemento)

    resultado.sort()

    return resultado


# Calcula a diferenca entre dois conjuntos
def diferenca(A, B):
    resultado = []

    for elemento in A:
        if not pertence(B, elemento):
            resultado.append(elemento)

    resultado.sort()

    return resultado


# Calcula o indice de Jaccard
def calcular_jaccard(A, B):
    interesses_comuns = intersecao(A, B)
    todos_interesses = uniao(A, B)

    quantidade_comum = len(interesses_comuns)
    quantidade_total = len(todos_interesses)

    # Se ambos os conjuntos estiverem vazios,
    # o indice matematico nao esta definido.
    if quantidade_total == 0:
        return None

    return quantidade_comum / quantidade_total


# Exibe a analise e as recomendacoes
def analisar_usuarios(nome_a, A, nome_b, B):
    print("\n===================================")
    print(" ANALISE DE COMPATIBILIDADE")
    print("===================================")

    print(f"\nInteresses de {nome_a}: {A}")
    print(f"Interesses de {nome_b}: {B}")

    # Operacoes entre os conjuntos
    comuns = intersecao(A, B)
    todos = uniao(A, B)
    exclusivos_a = diferenca(A, B)
    exclusivos_b = diferenca(B, A)

    print("\n--- OPERACOES COM CONJUNTOS ---")

    print(f"Interesses em comum: {comuns}")
    print(f"Uniao dos interesses: {todos}")

    print(f"Interesses exclusivos de {nome_a}: {exclusivos_a}")
    print(f"Interesses exclusivos de {nome_b}: {exclusivos_b}")

    print(f"\nQuantidade de interesses em comum: {len(comuns)}")
    print(f"Quantidade total de interesses: {len(todos)}")

    # Calculo do indice de Jaccard
    indice = calcular_jaccard(A, B)

    print("\n--- INDICE DE JACCARD ---")

    if indice is None:
        print("Nao e possivel calcular o indice.")
        print("Os dois usuarios nao informaram interesses.")
    else:
        print(f"Indice de Jaccard: {indice:.2f}")
        print(f"Similaridade: {indice * 100:.2f}%")

        if indice == 1:
            print("Os dois usuarios possuem os mesmos interesses.")
        elif indice == 0:
            print("Os usuarios nao possuem interesses em comum.")
        else:
            print("Os usuarios possuem alguns interesses em comum.")

    # Recomenda para A os interesses de B que A ainda nao possui
    recomendacoes_a = diferenca(B, A)

    # Recomenda para B os interesses de A que B ainda nao possui
    recomendacoes_b = diferenca(A, B)

    print("\n--- RECOMENDACOES ---")

    if len(recomendacoes_a) > 0:
        print(f"Sugestoes para {nome_a}: {recomendacoes_a}")
    else:
        print(f"Nao ha novas sugestoes para {nome_a}.")

    if len(recomendacoes_b) > 0:
        print(f"Sugestoes para {nome_b}: {recomendacoes_b}")
    else:
        print(f"Nao ha novas sugestoes para {nome_b}.")


# Exibe os perfis cadastrados
def mostrar_perfis(nome_a, A, nome_b, B):
    print("\n--- PERFIS CADASTRADOS ---")
    print(f"{nome_a}: {A}")
    print(f"{nome_b}: {B}")


# Permite alterar os interesses de um usuario
def atualizar_interesses(nome):
    print(f"\nAtualizando interesses de {nome}.")
    return ler_interesses(nome)


# Executa tres cenarios para testar o sistema
def executar_testes():
    print("\n===================================")
    print(" CENARIOS DE TESTE")
    print("===================================")

    # Teste 1: alguns interesses em comum
    A = ["rock", "jazz", "cinema", "games"]
    B = ["games", "tecnologia", "cinema"]

    analisar_usuarios("Ana", A, "Caio", B)

    # Teste 2: conjuntos iguais
    A = ["cinema", "games"]
    B = ["cinema", "games"]

    analisar_usuarios("Maria", A, "Pedro", B)

    # Teste 3: conjuntos sem interesses em comum
    A = ["rock"]
    B = ["culinaria"]

    analisar_usuarios("Lucas", A, "Julia", B)


# Le um numero inteiro para o menu
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Digite uma opcao valida.")


# Programa principal
def main():
    print("===================================")
    print(" SISTEMA DE RECOMENDACAO")
    print("===================================")

    nome_a = input("Nome do usuario A: ").strip()

    if nome_a == "":
        nome_a = "Usuario A"

    A = ler_interesses(nome_a)

    nome_b = input("\nNome do usuario B: ").strip()

    if nome_b == "":
        nome_b = "Usuario B"

    B = ler_interesses(nome_b)

    executando = True

    while executando:
        print("\n========== MENU ==========")
        print("1 - Comparar usuarios")
        print("2 - Mostrar perfis")
        print("3 - Atualizar interesses do usuario A")
        print("4 - Atualizar interesses do usuario B")
        print("5 - Executar tres cenarios de teste")
        print("0 - Sair")

        opcao = ler_inteiro("Escolha uma opcao: ")

        if opcao == 1:
            analisar_usuarios(nome_a, A, nome_b, B)

        elif opcao == 2:
            mostrar_perfis(nome_a, A, nome_b, B)

        elif opcao == 3:
            A = atualizar_interesses(nome_a)

        elif opcao == 4:
            B = atualizar_interesses(nome_b)

        elif opcao == 5:
            executar_testes()

        elif opcao == 0:
            executando = False
            print("Programa encerrado.")

        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()