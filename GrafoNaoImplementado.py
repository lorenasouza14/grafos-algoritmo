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
                par = tuple(sorted([origem, destino]))
                arestas.add(par)
            else:
                arestas.add((origem, destino))

    print("V(G) = {" + ", ".join(vertices) + "}")


    if nao_direcionado:
        e_str = ", ".join([f"{{{u},{v}}}" for u, v in sorted(arestas)])
        print("E(G) = {" + e_str + "}")
    else:
    
        e_str = ", ".join([f"({u},{v})" for u, v in sorted(arestas)])
        print("E(G) = {" + e_str + "}")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        print(f"O vértice '{origem}' não existe no grafo.")
        return False

    if destino in grafo[origem]:
        grafo[origem].remove(destino)
        print(f"Aresta removida: {origem} -> {destino}")
    else:
        print(f"Não existe aresta de {origem} para {destino}.")

    if nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)
            print(f"Aresta removida: {destino} -> {origem}")

    return True


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return False

    for v in list(grafo.keys()):  
        if vertice in grafo[v]:
            grafo[v].remove(vertice)

    del grafo[vertice]
    print(f"Vértice '{vertice}' e todas as arestas associadas foram removidos com sucesso.")
    return True


def existe_aresta(grafo, origem, destino):
    if origem not in grafo:
        return False 
    
    return destino in grafo[origem]

def grau_vertices(grafo, nao_direcionado=False):
    graus = {}

    for vertice in grafo:
        graus[vertice] = {'in': 0, 'out': len(grafo[vertice]), 'total': 0}

    if not nao_direcionado:
    
        for origem, vizinhos in grafo.items():
            for destino in vizinhos:
                if destino not in graus:
                    graus[destino] = {'in': 0, 'out': 0, 'total': 0}
                graus[destino]['in'] += 1
    else:

        for origem, vizinhos in grafo.items():
            for destino in vizinhos:
                if destino not in graus:
                    graus[destino] = {'in': 0, 'out': 0, 'total': 0}
                graus[destino]['in'] += 1 
                graus[destino]['total'] = graus[destino]['in'] + graus[destino]['out']

    for vertice in graus:
        graus[vertice]['total'] = graus[vertice]['in'] + graus[vertice]['out']

    return graus

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True


def bfs(grafo, inicio, direcionado=True):
    if inicio not in grafo:
        print("Vértice inicial não existe.")
        return [], {}

    fila = [inicio]
    visitados = set([inicio])
    ordem = []
    

    while fila:
        atual = fila.pop(0)
        ordem.append(atual)

        vizinhos = grafo[atual][:]
        vizinhos.sort()

        for v in vizinhos:
            if v not in visitados:
                visitados.add(v)
                
                fila.append(v)

        if not direcionado:
            for u in grafo:
                if atual in grafo[u]:
                    if u not in visitados:
                        visitados.add(u)
                        
                        fila.append(u)

    return ordem


def menor_caminho_bfs(grafo, inicio, destino, direcionado=True):
    if inicio not in grafo or destino not in grafo:
        print("Vértice inicial ou final não existe.")
        return None

    from collections import deque

    fila = deque([inicio])
    visitados = set([inicio])

    anterior = {inicio: None}

    while fila:
        atual = fila.popleft()

        if atual == destino:
            break

        for v in sorted(grafo[atual]):
            if v not in visitados:
                visitados.add(v)
                anterior[v] = atual
                fila.append(v)

        if not direcionado:
            for u in grafo:
                if atual in grafo[u] and u not in visitados:
                    visitados.add(u)
                    anterior[u] = atual
                    fila.append(u)

    if destino not in anterior:
        return None

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]

    caminho.reverse()
    return caminho

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
        print("8 - Exibir Grau dos Vértices")
        print("9 - Verificar se um percurso é possível")
        print("10 - Verificar se existe uma aresta entre dois vértices")
        print("11 - Busca em Largura (BFS)")
        print("12 - Menor Caminho (BFS)")
        print("0 - Sair")

        
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
            nd = input("O grafo é não direcionado? (s/n): ").strip().lower() == 's'
            graus = grau_vertices(grafo, nao_direcionado=nd)
            for v, g in graus.items():
                print(f"Vértice {v}: Grau de entrada = {g['in']}, saída = {g['out']}, total = {g['total']}")
                
        elif opcao == '9':
            caminho = input("Digite o percurso (vértices separados por espaço): ").strip().split()
            if percurso_valido(grafo, caminho):
                print("O percurso é possível.")
            else:
                print("O percurso NÃO é possível.")

        elif opcao == '10':
            o = input("Digite o vértice de origem: ").strip()
            d = input("Digite o vértice de destino: ").strip()
            if existe_aresta(grafo, o, d):
                print(f"Existe uma aresta de {o} para {d}.")
            else:
                print(f"Não existe aresta de {o} para {d}.")

        elif opcao == '11':
            inicio = input("Digite o vértice inicial: ").strip()
            tipo = input("Grafo é direcionado? (s/n): ").strip().lower() == 's'
    
            ordem = bfs(grafo, inicio, direcionado=tipo)
            print("Ordem BFS:", " -> ".join(ordem))

        elif opcao == '12':
            inicio = input("Vértice inicial: ").strip()
            destino = input("Vértice destino: ").strip()
            tipo = input("Grafo é direcionado? (s/n): ").strip().lower() == 's'

            caminho = menor_caminho_bfs(grafo, inicio, destino, direcionado=tipo)

            if caminho:
                print("Menor caminho:", " -> ".join(caminho))
            else:
                print("Não existe caminho entre os vértices.")
            
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
    