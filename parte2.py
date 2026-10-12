import re
from fractions import Fraction
from math import isqrt, sqrt


# Le um numero inteiro validando a entrada
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


# Transforma uma fracao em texto de forma simplificada
def formatar_fracao(valor):
    if valor.denominator == 1:
        return str(valor.numerator)

    return f"{valor.numerator}/{valor.denominator}"


# Classifica um numero racional nos conjuntos numericos
def classificar_racional(valor):
    if valor.denominator == 1:
        if valor.numerator >= 0:
            # Nesta implementacao, zero pertence a N
            return ["N", "Z", "Q", "R"]

        return ["Z", "Q", "R"]

    return ["Q", "R"]


# Analisa a entrada e identifica o tipo de numero
def analisar_numero(entrada):
    texto = entrada.strip().lower()
    texto = re.sub(r"\s+", "", texto)

    # Caso 1: raiz quadrada, como sqrt(9) ou raiz 2
    raiz = re.fullmatch(
        r"(?:√|sqrt|raiz)\s*\(?\s*(-?\d+)\s*\)?",
        texto
    )

    if raiz:
        radicando = int(raiz.group(1))

        if radicando < 0:
            raise ValueError(
                "Raizes de numeros negativos nao pertencem aos reais."
            )

        resultado = isqrt(radicando)

        if resultado * resultado == radicando:
            valor = Fraction(resultado, 1)

            return {
                "tipo": "Raiz exata",
                "valor": valor,
                "conjuntos": classificar_racional(valor),
                "justificativa": (
                    "A raiz e exata e seu resultado e um inteiro."
                ),
                "periodica": None,
                "geratriz": None,
                "aproximacao": None
            }

        return {
            "tipo": "Raiz irracional",
            "valor": None,
            "conjuntos": ["I", "R"],
            "justificativa": (
                "A raiz de um inteiro que nao e quadrado perfeito "
                "e irracional."
            ),
            "periodica": None,
            "geratriz": None,
            "aproximacao": sqrt(radicando)
        }

    # Caso 2: dizima periodica, como 0,(3) ou 1,2(5)
    periodica = re.fullmatch(
        r"([+-]?)(\d+)[,.](\d*)\((\d+)\)",
        texto
    )

    if periodica:
        sinal, parte_inteira, parte_nao_periodica, periodo = (
            periodica.groups()
        )

        # Digitos antes da repeticao
        prefixo = int(parte_inteira + parte_nao_periodica)

        # Digitos incluindo uma repeticao
        expandido = int(
            parte_inteira + parte_nao_periodica + periodo
        )

        numerador = expandido - prefixo

        denominador = (
            10 ** len(parte_nao_periodica)
            * (10 ** len(periodo) - 1)
        )

        if sinal == "-":
            numerador = -numerador

        valor = Fraction(numerador, denominador)

        return {
            "tipo": "Dizima periodica",
            "valor": valor,
            "conjuntos": classificar_racional(valor),
            "justificativa": (
                "Toda dizima periodica pode ser representada "
                "por uma fracao de inteiros."
            ),
            "periodica": (parte_nao_periodica, periodo),
            "geratriz": (numerador, denominador),
            "aproximacao": None
        }

    # Caso 3: fracao, como 3/4 ou -5/2
    if "/" in texto:
        valor = Fraction(texto)

        return {
            "tipo": "Fracao",
            "valor": valor,
            "conjuntos": classificar_racional(valor),
            "justificativa": (
                "A entrada e uma fracao de inteiros "
                "com denominador diferente de zero."
            ),
            "periodica": None,
            "geratriz": None,
            "aproximacao": None
        }

    # Caso 4: decimal exato, como 0,75 ou -2.5
    if "," in texto or "." in texto:
        valor = Fraction(texto.replace(",", "."))

        return {
            "tipo": "Decimal exato",
            "valor": valor,
            "conjuntos": classificar_racional(valor),
            "justificativa": (
                "Todo decimal exato pode ser escrito "
                "como uma fracao de inteiros."
            ),
            "periodica": None,
            "geratriz": None,
            "aproximacao": None
        }

    # Caso 5: numero inteiro
    valor = Fraction(int(texto), 1)

    return {
        "tipo": "Inteiro",
        "valor": valor,
        "conjuntos": classificar_racional(valor),
        "justificativa": (
            "O numero inteiro pode ser representado "
            "por uma fracao com denominador 1."
        ),
        "periodica": None,
        "geratriz": None,
        "aproximacao": None
    }


# Exibe a classificacao completa do numero
def mostrar_classificacao(entrada):
    resultado = analisar_numero(entrada)

    todos_conjuntos = ["N", "Z", "Q", "I", "R"]
    conjuntos = resultado["conjuntos"]

    nao_pertence = [
        conjunto
        for conjunto in todos_conjuntos
        if conjunto not in conjuntos
    ]

    print("\n=== CLASSIFICACAO DO NUMERO ===")
    print(f"Entrada: {entrada}")
    print(f"Tipo: {resultado['tipo']}")

    if resultado["valor"] is not None:
        print(
            "Valor exato:",
            formatar_fracao(resultado["valor"])
        )
    else:
        print(
            f"Valor aproximado: "
            f"{resultado['aproximacao']:.10f}"
        )

    # Mostra os detalhes da dizima periodica
    if resultado["periodica"] is not None:
        parte, periodo = resultado["periodica"]

        if parte:
            texto_parte = parte
        else:
            texto_parte = "nenhuma"

        print(
            f"Parte nao periodica: {texto_parte}"
        )
        print(f"Periodo: {periodo}")

        numerador, denominador = resultado["geratriz"]

        print(
            f"Fracao geratriz: {numerador}/{denominador}"
            f" = {formatar_fracao(resultado['valor'])}"
        )

    print("Pertence a:", ", ".join(conjuntos))
    print("Nao pertence a:", ", ".join(nao_pertence))
    print("Justificativa:", resultado["justificativa"])


# Bonus: gera todos os primos ate n usando o crivo de Eratostenes
def gerar_primos(limite):
    if limite < 2:
        return []

    eh_primo = [True] * (limite + 1)
    eh_primo[0] = False
    eh_primo[1] = False

    for numero in range(2, isqrt(limite) + 1):
        if eh_primo[numero]:
            for multiplo in range(
                numero * numero,
                limite + 1,
                numero
            ):
                eh_primo[multiplo] = False

    primos = []

    for numero in range(2, limite + 1):
        if eh_primo[numero]:
            primos.append(numero)

    return primos


# Bonus: lista os divisores positivos de um numero
def listar_divisores(numero):
    if numero == 0:
        print(
            "Zero possui infinitos divisores positivos; "
            "nao e possivel listar todos."
        )
        return

    divisores = []
    numero_absoluto = abs(numero)

    for divisor in range(1, numero_absoluto + 1):
        if numero_absoluto % divisor == 0:
            divisores.append(divisor)

    print(
        f"Divisores positivos de {numero}: {divisores}"
    )


# Menu principal
def main():
    executando = True

    while executando:
        print("\n=== PARTE 2 - CONJUNTOS NUMERICOS ===")
        print("1 - Classificar um numero")
        print("2 - Gerar numeros primos ate N")
        print("3 - Listar divisores de um numero")
        print("0 - Sair")

        opcao = ler_inteiro("Escolha uma opcao: ")

        if opcao == 1:
            entrada = input(
                "Digite um numero:"
            )

            try:
                mostrar_classificacao(entrada)
            except (ValueError, ZeroDivisionError):
                print(
                    "Entrada invalida. Verifique o formato "
                    "do numero e o denominador da fracao."
                )

        elif opcao == 2:
            limite = ler_inteiro(
                "Gerar primos ate qual numero? "
            )

            print(
                f"Primos ate {limite}: {gerar_primos(limite)}"
            )

        elif opcao == 3:
            numero = ler_inteiro(
                "Digite um numero inteiro: "
            )

            listar_divisores(numero)

        elif opcao == 0:
            executando = False
            print("Programa encerrado.")

        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()