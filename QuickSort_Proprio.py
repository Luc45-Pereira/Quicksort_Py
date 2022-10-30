lista = [12,23,11,12,40,135,2,0]

# 1 - particonar
# 2 - testa um menor e um maior até que o inicio e fim se encontrem
# 3 - inverte os valores
def Quicksort(lista, left, right):
    print(str(left)+'direita')
    print(str(right)+'esquerda')
    # Se o inicio da lista for menor que o final ele executa o bloco
    if left < right:
        print(str(left)+'direita')
        print(str(right)+'esquerda')
        # Encontra o pivo, utilizando a função particionar, passando os mesmos 3 parâmetros da função QuickSort
        pivot = partition(lista,left,right)
        # Utiliza da recursividade para organizar à esquerda e direita do pivo, esquerda passando o índice do pivo - 1, e direita passando o pivo
        Quicksort(lista,left, pivot - 1)
        Quicksort(lista,pivot,right)

def partition(lista, inicio, fim):
    pivo = int(fim-inicio/2)
    i = inicio
    f = fim
    while True:
        while lista[pivo] < lista[f]:
            f -= 1

        while lista[pivo] > lista[i]:
            i += 1
        
        if i >= f:
            break
        lista[i], lista[f] = lista[f], lista[i]
        print(str(lista)+'while')

    return i

Quicksort(lista, 0, len(lista)-1)

# [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
# [2, 0, 1, 8, 7, 3, 5, 4, 9, 6]
# []
# 
# 
# 
# 
# 1