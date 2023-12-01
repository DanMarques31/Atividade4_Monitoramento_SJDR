# Atividade4_Monitoramento_SJDR

Aluno: Daniel Luiz Araújo Marques

O programa foi desenvolvido no WSL 2 : Ubuntu 22.04 LTS utilizando Python 3.10.6.

Tudo referente ao código está devidamente comentado no mesmo.

Heurística:

O problema de cobertura de vértices é um problema np-completo que se trata de
obter o conjunto de vértices de maneira que qualquer aresta do grafo tem pelo
menos incidência em um dos vértices do conjunto. Devido a ser np-completo é
necessário o desenvolvimento de uma heurística aproximada.
A heurística desenvolvida foi bastante simples, ela funciona basicamente
encontrando o vértice de maior grau. O algoritmo obtém o vértice de maior grau (ou
seja, vértice com maior número de arestas conectadas a ele) e o coloca em uma
lista indicando que uma câmera será instalada nesse vértice. Após isso ele remove
as arestas que estavam conectadas a esse vértice já que essas arestas (ruas)
agora estão sendo monitoradas pela câmera (vértice). O algoritmo continua desse
jeito até remover todas as arestas, ou seja, até que todas as ruas estejam sendo
monitoradas. É importante dizer que se trata de uma heurística, logo não será a
solução ótima apesar de estar bem próximo dela.

Execução:

O arquivo de nome “sjdr.gml” deve estar no mesmo diretório do arquivo main.py,
depois é só executar a seguinte linha :

                            python3 main.py

Caso esteja no VsCode também é possível executar pelo botão Run