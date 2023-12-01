import networkx as nx # Biblioteca para manipulação de grafo, utilizada para ler o arquivo sjdr.gml
import cobertura_minimal # Importa o módulo com a função de cobertura mínima

# Lê o grafo a partir do arquivo .gml
grafo = nx.read_gml("sjdr.gml", label = 'id')

# Faz uma cópia do grafo para poder obter os vizinhos de cada vértice na saída
grafo_copia = grafo.copy()

# Encontra a cobertura mínima de vértices usando a heurística personalizada
cobertura = cobertura_minimal.cobertura_minima(grafo)

# Obtém a lista de vizinhos do grafo copiado
vizinhos = {vertice: list(grafo_copia.neighbors(vertice)) for vertice in cobertura}

# Ordena os IDs em ordem crescente para melhorar a visualização da saída do alg
cobertura.sort()

# Impressão do resultado formatado por Vértice  |  ( Vizinhos )
print("Vértices  |  (Vizinhos)")
for vertice in cobertura:
    vizinhos_lista = vizinhos[vertice]
    print(f"{vertice}  |  ( {' '.join(map(str, vizinhos_lista))} )") # Transforma os vizinhos em string e concatena da maneira que eu queria