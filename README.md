# Codificador de Palavras com Pilha

Este programa codifica uma palavra com base em um método de cartas e pilha, onde a palavra é transformada seguindo uma sequência de movimentações. Ele é útil para criar um formato secreto de anotação para proteger o conteúdo escrito, conforme solicitado pelo problema de codificação.

## Descrição

O programa segue o seguinte procedimento:
1. Percorre as letras da palavra de entrada.
2. Coloca a primeira letra em uma pilha.
3. Anota a segunda letra e a descarta.
4. Coloca a terceira letra na pilha, anota e descarta a quarta, e assim por diante.
5. Após o final da palavra, o programa retira todas as letras restantes na pilha e as anota na ordem inversa.

Esse método de codificação gera uma palavra embaralhada, que segue um padrão específico de posicionamento. 

## Exemplo

Entrada: `MANTEIGA`  
Saída: `ATIAGENM`

Entrada: `MUITO`  
Saída: `UTOIM`

## Instalação e Execução

Este programa foi escrito em Python e requer o Python 3.6 ou superior para ser executado.

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/lisboatm/codificador_pilha.git
cd codificador_pilha
```

### Passo 2: Executar o Código

Para codificar uma palavra, basta rodar o script principal:

```bash
python codificador.py
```

O programa solicitará uma palavra de entrada ou pode ser adaptado para aceitar diretamente a palavra como argumento de entrada.

## Estrutura do Projeto

```
codificador-pilha/
├── codificador.py    # Arquivo principal do programa
├── README.md         # Documentação do projeto
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou fazer um _pull request_ para melhorar este projeto.

## Licença

Este projeto é distribuído sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.
