def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    inserir_vertice(vertices, origem)
    inserir_vertice(vertices, destino)

    if [origem, destino] not in arestas:
        arestas.append([origem, destino])

    if nao_direcionado and [destino, origem] not in arestas:
        arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        arestas[:] = [a for a in arestas if vertice not in a]


def existe_aresta(arestas, origem, destino):
    for o, d in arestas:
        if o == origem and d == destino:
            return True
    return False


def vizinhos(vertices, arestas, vertice):
    vizinhos = []
    for origem, destino in arestas:
        if origem == vertice:
            vizinhos.append(destino)
    return vizinhos


def grau_vertices(vertices, arestas):
    graus = {v: {"entrada": 0, "saida": 0, "total": 0} for v in vertices}

    for origem, destino in arestas:
        if origem in graus:
            graus[origem]["saida"] += 1
        if destino in graus:
            graus[destino]["entrada"] += 1

    for v in graus:
        graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]

    return graus


def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(arestas, caminho[i], caminho[i + 1]):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    viz = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {viz}")


def exibir_grafo(vertices, arestas):
    print("\nVértices:", vertices)
    print("Arestas:")
    for origem, destino in arestas:
        print(f"({origem} -> {destino})")

    print("\nLista de Adjacência:")
    adj = {v: [] for v in vertices}
    for origem, destino in arestas:
        adj[origem].append(destino)

    for v in adj:
        print(f"{v}: {adj[v]}")


def main():
    vertices, arestas = criar_grafo()

    print("=== Criação de Grafo ===")
    while True:
        origem = input("\nDigite o vértice de origem (ou ENTER para parar): ").strip()
        if origem == "":
            break
        destino = input("Digite o vértice de destino: ").strip()
        tipo = input("Aresta não direcionada? (s/n): ").strip().lower()
        nao_direcionado = tipo == "s"

        inserir_aresta(vertices, arestas, origem, destino, nao_direcionado)

    exibir_grafo(vertices, arestas)

    print("\nGrau dos vértices:")
    for v, g in grau_vertices(vertices, arestas).items():
        print(f"{v}: {g}")

    print("\n=== Verificação de Percurso ===")
    caminho = input("Digite o percurso (ex: A-B-D): ").strip().split("-")
    print("Percurso é válido?", percurso_valido(arestas, caminho))


if __name__ == "__main__":
    main()
