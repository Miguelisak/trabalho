# Laboratório de Matemática Aplicada à Programação

## 📚 Sobre o projeto

Este repositório contém as atividades práticas de Matemática Aplicada à Programação, desenvolvidas em Python. O objetivo é aplicar conceitos matemáticos na resolução de problemas computacionais, utilizando funções, estruturas de repetição, condicionais e operações com conjuntos.

O trabalho está dividido em três partes:

1. **Parte 1 — Teoria dos Conjuntos**
2. **Parte 2 — Conjuntos Numéricos**
3. **Parte 3 — Mini-Projeto: Sistema de Recomendação por Interesses**

## 🛠️ Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git e GitHub

## 📂 Organização dos arquivos

```text
laboratorio-matematica/
│
├── parte1.py
├── parte2.py
├── parte3.py
└── README.md
```

> Os nomes dos arquivos podem ser ajustados conforme a organização utilizada no repositório.

---

## 1. Parte 1 — Teoria dos Conjuntos

### Objetivo

Implementar as principais operações da teoria dos conjuntos utilizando funções próprias em Python, permitindo que o usuário informe os conjuntos e escolha as operações por meio de um menu interativo.

### Funcionalidades

- Leitura dos conjuntos A e B.
- Remoção de elementos duplicados.
- União de conjuntos.
- Interseção de conjuntos.
- Diferença entre conjuntos, incluindo A − B e B − A.
- Diferença simétrica.
- Verificação de pertinência.
- Verificação de inclusão e inclusão estrita.
- Cálculo da cardinalidade.
- Cálculo do complemento em relação ao universo informado.
- Comparação entre os resultados manuais e os operadores nativos do Python.
- Validação de entradas e do universo utilizado nos complementos.

### Conceitos aplicados

| Operação | Descrição |
|---|---|
| União (A ∪ B) | Reúne os elementos dos dois conjuntos sem duplicatas. |
| Interseção (A ∩ B) | Retorna os elementos presentes nos dois conjuntos. |
| Diferença (A − B) | Retorna os elementos de A que não pertencem a B. |
| Diferença simétrica (A △ B) | Retorna os elementos que pertencem a apenas um dos conjuntos. |
| Pertinência | Verifica se determinado elemento pertence a um conjunto. |
| Inclusão | Verifica se todos os elementos de um conjunto estão contidos em outro. |
| Cardinalidade | Calcula a quantidade de elementos de um conjunto. |
| Complemento | Retorna os elementos do universo que não pertencem ao conjunto. |

### Implementação

As operações principais são implementadas manualmente por meio de funções, laços de repetição e condicionais. A comparação com os operadores nativos é utilizada separadamente para validar os resultados.

### Exemplos de teste

Considere:

```text
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
```

Resultados esperados:

```text
União: [1, 2, 3, 4, 5, 6]
Interseção: [3, 4]
A - B: [1, 2]
B - A: [5, 6]
Diferença simétrica: [1, 2, 5, 6]
Cardinalidade de A: 4
Cardinalidade de B: 4
```

Também são considerados testes com conjuntos vazios, iguais, disjuntos e com elementos repetidos.

---

## 2. Parte 2 — Conjuntos Numéricos

### Objetivo

Desenvolver um classificador capaz de identificar a quais conjuntos numéricos um determinado número pertence, apresentando sua classificação e uma justificativa matemática.

### Conjuntos estudados

| Símbolo | Conjunto | Exemplos |
|---|---|---|
| ℕ | Naturais | 0, 1, 2, 3... |
| ℤ | Inteiros | ... −3, −2, −1, 0, 1, 2... |
| ℚ | Racionais | 1/2, −3/4, 0,75 |
| I | Irracionais | √2, √3, π |
| ℝ | Reais | Todos os racionais e irracionais |

Nesta implementação, considera-se que o zero pertence ao conjunto dos números naturais.

### Funcionalidades

- Classificação de números inteiros.
- Interpretação de frações.
- Classificação de decimais exatos.
- Identificação de dízimas periódicas.
- Cálculo da fração geratriz de dízimas periódicas.
- Identificação de raízes quadradas exatas e irracionais de inteiros não negativos.
- Geração de números primos até um limite informado.
- Listagem dos divisores positivos de um número inteiro.

### Exemplos de classificação

| Entrada | Classificação |
|---|---|
| 7 | ℕ, ℤ, ℚ e ℝ |
| −3 | ℤ, ℚ e ℝ |
| 3/4 | ℚ e ℝ |
| 0,75 | ℚ e ℝ |
| 0,(3) | ℚ e ℝ |
| √9 | ℕ, ℤ, ℚ e ℝ |
| √2 | I e ℝ |

### Fração geratriz

O programa representa dízimas periódicas por frações equivalentes.

Exemplo:

```text
Entrada: 0,(3)
Fração geratriz: 3/9
Fração simplificada: 1/3
Classificação: Q e R
```

Outro exemplo:

```text
Entrada: 1,2(5)
Fração geratriz: 113/90
Classificação: Q e R
```

Para representar frações com exatidão, o programa utiliza a biblioteca `fractions` do Python. A análise de raízes quadradas utiliza recursos da biblioteca `math`, e os formatos de entrada são identificados por expressões regulares.

**Observação:** o classificador de raízes trabalha com radicandos inteiros. A classificação considera o valor matemático da expressão, e não somente uma aproximação decimal.

---

## 3. Parte 3 — Mini-Projeto: Sistema de Recomendação por Interesses

### Opção escolhida: Sistema de Recomendação por Interesses

Para a terceira parte da atividade, foi escolhido o mini-projeto **Sistema de Recomendação por Interesses**, uma das quatro opções propostas no enunciado.

O objetivo é aplicar os conceitos de teoria dos conjuntos desenvolvidos na Parte 1 em uma aplicação prática que compara os interesses de dois usuários.

O sistema permite cadastrar interesses, identificar elementos em comum, calcular a similaridade entre os usuários utilizando o índice de Jaccard e recomendar interesses que uma pessoa ainda não possui.

**Arquivo do projeto:** `parte3.py`.

### Conceitos matemáticos utilizados

- União de conjuntos.
- Interseção de conjuntos.
- Diferença entre conjuntos.
- Cardinalidade.
- Índice de Jaccard.

### Funcionamento

O programa solicita o nome e os interesses de dois usuários. Os interesses são informados separados por vírgulas e armazenados sem duplicatas.

Após o cadastro, é possível:

- Comparar os interesses dos usuários.
- Exibir os perfis cadastrados.
- Atualizar os interesses de cada usuário.
- Calcular a união e a interseção dos interesses.
- Identificar interesses exclusivos de cada pessoa.
- Calcular o índice de similaridade de Jaccard.
- Recomendar interesses do outro usuário que ainda não estão no perfil.
- Executar três cenários de teste.

### Índice de Jaccard

A similaridade é calculada pela fórmula:

**J(A, B) = |A ∩ B| / |A ∪ B|**

Em que:

- A ∩ B representa os interesses em comum.
- A ∪ B representa todos os interesses distintos dos dois usuários.
- O índice varia de 0 a 1 quando a união não está vazia.

Quanto maior o índice, maior a proporção de interesses compartilhados.

### Exemplo de aplicação

Considere os usuários:

```text
Ana:
rock, jazz, cinema, games

Caio:
games, tecnologia, cinema
```

Resultados esperados:

```text
Interesses em comum:
['cinema', 'games']

União dos interesses:
['cinema', 'games', 'jazz', 'rock', 'tecnologia']

Quantidade de interesses em comum: 2
Quantidade total de interesses: 5

Índice de Jaccard: 0.40
Similaridade: 40.00%

Sugestões para Ana:
['tecnologia']

Sugestões para Caio:
['jazz', 'rock']
```

O índice de 40% indica a proporção de interesses compartilhados em relação ao total de interesses diferentes dos dois perfis.

As sugestões representam interesses que o outro usuário possui e que ainda não aparecem no perfil analisado. Elas não garantem que o usuário realmente gostará dessas atividades.

### Cenários de teste

**Teste 1 — Interesses parcialmente iguais**

Verifica se o programa identifica corretamente os interesses em comum e calcula o índice de Jaccard.

**Teste 2 — Conjuntos iguais**

Verifica se o sistema identifica 100% de similaridade quando os dois usuários possuem exatamente os mesmos interesses.

**Teste 3 — Conjuntos sem interesses em comum**

Verifica se o sistema retorna similaridade de 0% quando os usuários não compartilham nenhum interesse.

Quando os dois usuários não informam interesses, o índice não é definido matematicamente. Nesse caso, o programa informa que não é possível calcular o índice.

---

## ▶️ Como executar o projeto

### Pré-requisitos

- Python 3 instalado.
- Editor de código, como Visual Studio Code.

As bibliotecas utilizadas nas três partes fazem parte da biblioteca padrão do Python. Não é necessário instalar pacotes externos.

### Execução

Abra o terminal na pasta do projeto e execute o arquivo desejado:

```bash
python parte1.py
```

```bash
python parte2.py
```

```bash
python parte3.py
```

Em alguns ambientes Windows, pode ser necessário utilizar o comando `py` no lugar de `python`.

Cada arquivo possui seu próprio menu interativo.

---

## 🧪 Testes e validação

Os testes têm como objetivo verificar se os resultados apresentados pelo programa correspondem às regras matemáticas estudadas.

Na Parte 1, os resultados das operações manuais são comparados com os resultados obtidos pelos conjuntos nativos do Python.

Na Parte 2, são utilizados números de diferentes classificações, incluindo inteiros, frações, decimais, dízimas periódicas e raízes.

Na Parte 3, são testados perfis com interesses parcialmente iguais, perfis idênticos e perfis sem interesses compartilhados.

Os exemplos apresentados neste documento representam os resultados esperados. As evidências finais de execução devem ser verificadas no ambiente utilizado pelo grupo.

---

## 📖 Aprendizados

Durante o desenvolvimento das atividades, são trabalhados os seguintes conhecimentos:

- Aplicação da teoria dos conjuntos na programação.
- Implementação de funções reutilizáveis.
- Utilização de listas, laços de repetição e condicionais.
- Validação e tratamento de entradas do usuário.
- Classificação de números e representação de frações.
- Desenvolvimento de menus interativos.
- Aplicação de conceitos matemáticos em um sistema de recomendação.
- Testes e validação de resultados.
- Organização de projetos com Git e GitHub.

## 👥 Integrantes

- Nome: Miguel Isak Nunes da Silva
- Nome: Matheus Alves de Oliveira


## 🎓 Instituição

**Fatec Osasco — Centro Paula Souza**

Curso: Desenvolvimento de Software Multiplataforma (DSM)

Disciplina: Matemática Aplicada à Programação

---

Este projeto foi desenvolvido para fins acadêmicos, com o objetivo de demonstrar a aplicação prática dos conceitos matemáticos por meio da programação em Python.
