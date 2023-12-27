# Graph Processing Application

## Descrição
Este programa é uma aplicação em Python para manipular e analisar grafos não-direcionados com pesos nas arestas. Ele realiza três tarefas principais:

1. **Cálculo da Distância e do Caminho Mínimo (Tarefa A)**: Calcula a distância e o caminho mínimo entre um vértice inicial e vários vértices alvo usando o algoritmo de Dijkstra.
2. **Árvore Geradora Mínima (Tarefa B)**: Encontra a árvore geradora mínima do grafo utilizando o algoritmo de Kruskal.
3. **Cálculo da Excentricidade de Vértices (Tarefa C)**: Calcula a excentricidade de vértices especificados.

## Estrutura do Projeto
O projeto é composto pelos seguintes componentes principais:

- `Graph`: Classe que representa um grafo não-direcionado com pesos.
- `DisjointSet`: Classe auxiliar para o algoritmo de Kruskal.
- `build_graph_from_file`: Função para construir um grafo a partir de um arquivo de texto.
- `task_a`, `task_b`, `task_c`: Funções para executar as tarefas A, B e C, respectivamente.

## Como Executar
Para executar o programa, siga estes passos:

1. Certifique-se de que o Python está instalado no seu sistema.
2. Coloque os arquivos de texto do grafo no mesmo diretório do programa.
3. Execute o script Python principal.

## Formato do Arquivo de Entrada
O arquivo de entrada deve estar no seguinte formato:

- A primeira linha contém o número total de vértices no grafo.
- As linhas subsequentes representam as arestas, cada uma com um par de vértices e um peso (por exemplo, "1 2 3.45" representa uma aresta entre os vértices 1 e 2 com peso 3.45).

## Exemplo de Uso
```
python main.py
```
