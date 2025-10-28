def criar_grafo():
    grafo = {}
    return grafo



def inserir_vertice(grafo, vertice):
    if vertice in grafo:
        print("Vértice já existe.")
        return False
    grafo[vertice] = []
    return True


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)
    return True

def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        return []

def listar_vizinhos(grafo, vertice):
    if vertice not in grafo:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return None

    lista = vizinhos(grafo, vertice)

    if lista:
        print(f"Vizinhos do vértice '{vertice}': {lista}")
    else:
        print(f"O vértice '{vertice}' não possui vizinhos.")

    return lista
    
def exibir_grafo(grafo, nao_direcionado=False):
    if not grafo:
        print("O grafo está vazio.")
        return

    vertices = sorted(grafo.keys())
    arestas = set()

    for origem, vizinhos in grafo.items():
        for destino in vizinhos:
            if nao_direcionado:
                # Ordena para garantir que {a,b} = {b,a}
                par = tuple(sorted([origem, destino]))
                arestas.add(par)
            else:
                arestas.add((origem, destino))

    # Exibir vértices
    print("V(G) = {" + ", ".join(vertices) + "}")

    # Exibir arestas
    if nao_direcionado:
        # Transformar cada par em string com chaves, sem duplicidade
        e_str = ", ".join([f"{{{u},{v}}}" for u, v in sorted(arestas)])
        print("E(G) = {" + e_str + "}")
    else:
        # Direcionado: parênteses
        e_str = ", ".join([f"({u},{v})" for u, v in sorted(arestas)])
        print("E(G) = {" + e_str + "}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    """
    Remove a aresta entre origem e destino.
    Passos:
    1. Verificar se 'origem' existe; se não, terminar.
    2. Se destino estiver em grafo[origem], remover essa ocorrência.
    3. Se for não direcionado, também:
        - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
    """
    if origem not in grafo:
        print(f"O vértice '{origem}' não existe no grafo.")
        return False

    if destino in grafo[origem]:
        grafo[origem].remove(destino)
        print(f"Aresta removida: {origem} -> {destino}")
    else:
        print(f"Não existe aresta de {origem} para {destino}.")

    # Se o grafo for não direcionado, remover o inverso também
    if nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)
            print(f"Aresta removida: {destino} -> {origem}")

    return True


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return False

    # Remover o vértice das listas de vizinhos de todos os outros
    for v in list(grafo.keys()):  # cópia para evitar erro de modificação durante iteração
        if vertice in grafo[v]:
            grafo[v].remove(vertice)
            # Se for grafo não direcionado, não precisa de nada adicional,
            # pois a remoção é simétrica ao remover o próprio vértice depois.

    # Agora, remover o próprio vértice
    del grafo[vertice]
    print(f"Vértice '{vertice}' e todas as arestas associadas foram removidos com sucesso.")
    return True



def existe_aresta(grafo, origem, destino):
    if origem not in grafo:
        return False  # origem nem existe, logo a aresta não existe
    
    return destino in grafo[origem]

def grau_vertices(grafo):
    graus = {}

    # Passo 2: inicializa graus com zeros
    for vertice in grafo:
        graus[vertice] = {'in': 0, 'out': 0, 'total': 0}

    # Passo 3: calcula grau de saída (out)
    for origem, vizinhos in grafo.items():
        graus[origem]['out'] = len(vizinhos)

    # Passo 3b: calcula grau de entrada (in)
    for origem, vizinhos in grafo.items():
        for destino in vizinhos:
            if destino in graus:  # garante que o destino exista no grafo
                graus[destino]['in'] += 1

    # Passo 4: calcula grau total
    for vertice in graus:
        graus[vertice]['total'] = graus[vertice]['in'] + graus[vertice]['out']

    return graus


def percurso_valido(grafo, caminho):
    # 1. Caminhos de 0 ou 1 vértice são triviais
    if len(caminho) < 2:
        return True

    # 2. Verificar se há aresta entre cada par consecutivo
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False  # assim que uma ligação falha, o caminho é inválido

    # 3. Todas as arestas existem
    return True



def main():
    grafo = criar_grafo()
    
    while True:
        print("\n=== MENU DO GRAFO ===")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos de um Vértice")
        print("7 - Listar Vizinhos de Todos os Vértices")
        print("8 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            nd = input("O grafo é não direcionado? (s/n): ").strip().lower() == 's'
            exibir_grafo(grafo, nao_direcionado=nd)
        elif opcao == '2':
            v = input("Digite o vértice a inserir: ").strip()
            inserir_vertice(grafo, v)
        elif opcao == '3':
            o = input("Digite o vértice de origem: ").strip()
            d = input("Digite o vértice de destino: ").strip()
            nd = input("O grafo é não direcionado? (s/n): ").strip().lower() == 's'
            inserir_aresta(grafo, o, d, nao_direcionado=nd)
        elif opcao == '4':
            v = input("Digite o vértice a remover: ").strip()
            remover_vertice(grafo, v)
        elif opcao == '5':
            o = input("Digite o vértice de origem da aresta: ").strip()
            d = input("Digite o vértice de destino da aresta: ").strip()
            nd = input("O grafo é não direcionado? (s/n): ").strip().lower() == 's'
            remover_aresta(grafo, o, d, nao_direcionado=nd)
        elif opcao == '6':
            v = input("Digite o vértice para listar vizinhos: ").strip()
            listar_vizinhos(grafo, v)
        elif opcao == '7':
            print("Vizinhos de todos os vértices:")
            for vertice in sorted(grafo.keys()):
                lista = vizinhos(grafo, vertice)
                print(f"{vertice} -> {', '.join(lista) if lista else '(sem vizinhos)'}")
        elif opcao == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


