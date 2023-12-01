
def cobertura_minima(grafo):
    
    cameras_instaladas = [] # Variável para armazenar lista de vértices (câmeras)

    # Enquanto houver arestas não cobertas continua o Loop
    while grafo.edges():
        # Encontra o vértice de maior grau
        graus = dict(grafo.degree())
        
        # Verifica se há vértices no grafo
        if not graus:
            break

        vertice_maior_grau = max(graus, key = graus.get) # Obtém o vértice de maior grau para poder colocar na lista

        # Adiciona o vértice à lista de câmeras instaladas
        cameras_instaladas.append(vertice_maior_grau)

        # Remove arestas cobertas pelo vértice
        arestas_cobertas = set(grafo.edges(vertice_maior_grau))
        grafo.remove_edges_from(arestas_cobertas)

    return cameras_instaladas

