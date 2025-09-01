# Tabuada em Python com List Comprehension + Loops Aninhados

Programa em Python que:
- Gera a **tabuada de um número** fornecido pelo usuário usando **list comprehension**.
- (Extra) Mostra a **tabuada completa de 1 a 10** utilizando **loops aninhados** (`for` dentro de `for`).

## 🚀 Código principal
```python
# Entrada segura: garante que o usuário digitou um inteiro
try:
    numero = int(input("Digite um número inteiro para ver a tabuada: "))
except ValueError:
    print("Erro: digite um número inteiro válido!")
    import sys
    sys.exit(0)

# List Comprehension: cria a lista de linhas da tabuada (1 a 10)
tabuada = [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]

print("\n=== Tabuada (List Comprehension) ===")
for linha in tabuada:
    print(linha)

# Extra: tabuada completa 1 a 10 com loops aninhados
ver_completa = input("\nDeseja ver a tabuada completa de 1 a 10? (s/n): ").strip().lower()

if ver_completa == "s":
    print("\n=== Tabuada Completa (Loops Aninhados) ===")
    for n in range(1, 11):           # escolhe o número da tabuada
        linha_resultados = []
        for i in range(1, 11):       # multiplica n por 1..10
            linha_resultados.append(f"{n}x{i}={n*i}")
        print("  ".join(linha_resultados))

O que foi aprendido
Diferença entre loops tradicionais e list comprehension.
Como usar list comprehension para criar listas de forma enxuta.
Loops aninhados (for dentro de for) para gerar combinações.
Boas práticas de validação de entrada (try/except).
Formatação de saída com join para construir linhas legíveis.

💭 Comentário pessoal

Gostei de ver como o list comprehension simplifica o código da tabuada.
Os loops aninhados ajudaram a entender como percorrer combinações (ex.: 1x1 até 10x10).
Senti o código mais limpo e “pythonico”, e já imagino aplicar essa técnica em outras listas.
