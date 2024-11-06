def codificar_palavra(palavra):
    pilha = []
    codificacao = []

    # Processa as letras conforme o índice
    for i, letra in enumerate(palavra):
        if i % 2 == 0:  # Índice par, adiciona na pilha
            pilha.append(letra)
        else:           # Índice ímpar, anota na codificação
            codificacao.append(letra)

    # Adiciona as letras restantes na pilha em ordem inversa
    while pilha:
        codificacao.append(pilha.pop())

    # Retorna a palavra codificada como string
    return ''.join(codificacao)

# Exemplo de uso:
palavra = input().strip()  # Lê a palavra
print(codificar_palavra(palavra))
