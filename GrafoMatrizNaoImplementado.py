def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print(f"Vértice '{vertice}' já existe.")
        return False

    tamanho = len(vertices)
    vertices.append(vertice)

    for i in range(tamanho):
        matriz[i].append(0)

    matriz.append([0] * (tamanho + 1))
    return True


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    if matriz[i][j] == 1:
        print(f"Aresta de {origem} para {destino} já existe.")
        return False  

    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1
    return True


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return False

    pos = vertices.index(vertice)
    matriz.pop(pos)
    for linha in matriz:
        linha.pop(pos)
    vertices.pop(pos)
    return True


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        print("Um dos vértices não existe.")
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)
    if matriz[i][j] == 0:
        print(f"Aresta de {origem} para {destino} não existe.")
        return False

    matriz[i][j] = 0
    if nao_direcionado:
        matriz[j][i] = 0
    return True


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []
    i = vertices.index(vertice)
    return [vertices[j] for j, val in enumerate(matriz[i]) if val == 1]


def listar_vizinhos(matriz, vertices, vertice):
    lista = vizinhos(matriz, vertices, vertice)
    if lista:
        print(f"{vertice} -> {', '.join(lista)}")
    else:
        print(f"{vertice} -> (sem vizinhos)")
    return lista


def grau_vertices(matriz, vertices):
    graus = {}
    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(row[i] for row in matriz)
        total = saida + entrada
        graus[v] = {'saida': saida, 'entrada': entrada, 'total': total}
    return graus


def percurso_valido(matriz, vertices, caminho):
    if len(caminho) < 2:
        return True

    for k in range(len(caminho) - 1):
        origem = caminho[k]
        destino = caminho[k + 1]
        if origem not in vertices or destino not in vertices:
            return False
        i = vertices.index(origem)
        j = vertices.index(destino)
        if matriz[i][j] != 1:
            return False
    return True


def exibir_grafo(matriz, vertices):
    print("\nMatriz de Adjacência:")
    print("   ", end="")
    for v in vertices:
        print(v, end=" ")
    print()
    for i, v in enumerate(vertices):
        print(v, end="  ")
        for val in matriz[i]:
            print(val, end=" ")
        print()


def input_nao_direcionado():
    while True:
        nd = input("O grafo é não direcionado? (s/n): ").strip().lower()
        if nd == "s":
            return True
        elif nd == "n":
            return False
        else:
            print("Opção inválida, digite apenas 's' ou 'n'.")


def main():
    matriz, vertices = criar_grafo()

    while True:
        print("\n=== MENU ===")
        print("1 - Mostrar Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos")
        print("7 - Grau dos Vértices")
        print("8 - Verificar Percurso")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_grafo(matriz, vertices)
        elif opcao == "2":
            v = input("Digite o vértice a inserir: ").strip()
            inserir_vertice(matriz, vertices, v)
        elif opcao == "3":
            o = input("Digite o vértice de origem: ").strip()
            d = input("Digite o vértice de destino: ").strip()
            nd = input_nao_direcionado()
            inserir_aresta(matriz, vertices, o, d, nao_direcionado=nd)
        elif opcao == "4":
            v = input("Digite o vértice a remover: ").strip()
            remover_vertice(matriz, vertices, v)
        elif opcao == "5":
            o = input("Digite o vértice de origem da aresta: ").strip()
            d = input("Digite o vértice de destino da aresta: ").strip()
            nd = input_nao_direcionado()
            remover_aresta(matriz, vertices, o, d, nao_direcionado=nd)
        elif opcao == "6":
            v = input("Digite o vértice para listar vizinhos: ").strip()
            listar_vizinhos(matriz, vertices, v)
        elif opcao == "7":
            graus = grau_vertices(matriz, vertices)
            for v, g in graus.items():
                print(f"{v}: saída={g['saida']}, entrada={g['entrada']}, total={g['total']}")
        elif opcao == "8":
            caminho = input("Digite o percurso (ex: A B C): ").strip().split()
            if percurso_valido(matriz, vertices, caminho):
                print("O percurso é possível.")
            else:
                print("O percurso NÃO é possível.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
