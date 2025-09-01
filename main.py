# Dia 12 - Tabuada com List Comprehension + Loops Aninhados (extra)
# Objetivo:
# 1) Gerar a tabuada de um número usando list comprehension (forma "pythônica" e enxuta).
# 2) (Extra) Mostrar a tabuada completa de 1 a 10 usando loops aninhados (for dentro de for).

# --- Entrada segura ---
try:
    # Pedimos um número inteiro para gerar a tabuada específica
    numero = int(input("Digite um número inteiro para ver a tabuada: "))
except ValueError:
    # Caso o usuário digite algo que não seja número inteiro, avisamos e encerramos
    print("Erro: digite um número inteiro válido!")
    # exit() encerra o programa de forma limpa
    import sys
    sys.exit(0)

# --- Tabuada com List Comprehension ---
# A expressão abaixo cria uma lista de strings no formato "N x i = produto"
# para i variando de 1 a 10 (range(1, 11) vai de 1 até 10 inclusive).
tabuada = [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]

print("\n=== Tabuada (List Comprehension) ===")
# Percorremos a lista gerada e imprimimos cada linha
for linha in tabuada:
    print(linha)

# --- Extra: Tabuada completa 1 a 10 com loops aninhados ---
# Perguntamos se o usuário quer ver a “matriz” de tabuadas de 1 a 10.
ver_completa = input("\nDeseja ver a tabuada completa de 1 a 10? (s/n): ").strip().lower()

if ver_completa == "s":
    print("\n=== Tabuada Completa (Loops Aninhados) ===")
    # Primeiro loop escolhe o número da tabuada (1 a 10)
    for n in range(1, 11):
        # Segundo loop vai de 1 a 10 para multiplicar pelo n atual
        linha_resultados = []  # guardamos os resultados para imprimir a linha inteira
        for i in range(1, 11):
            linha_resultados.append(f"{n}x{i}={n*i}")
        # 'join' junta a lista em uma string única separada por 2 espaços
        print("  ".join(linha_resultados))
