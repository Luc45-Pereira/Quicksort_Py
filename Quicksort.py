# Cria uma lista pronta com uma ordem aleatória
lista = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
# Ordem crescente da Lista
# 2,4,6,8,9,2,10,53

# Função QuickSort, ela recebe 3 parâmetros, sendo a lista, left que seria o inicio da lista = 0, e right que seria o final da lista
def Quicksort(lista, left, right, msg):
    print(msg)
    # Se o inicio da lista for menor que o final ele executa o bloco
    if left < right:
        # Encontra o pivo, utilizando a função particionar, passando os mesmos 3 parâmetros da função QuickSort
        pivot = particionar(lista,left,right)
        # Utiliza da recursividade para organizar à esquerda e direita do pivo, esquerda passando o índice do pivo - 1, e direita passando o pivo
        Quicksort(lista,left, pivot - 1, 'esquerda')
        Quicksort(lista,pivot,right, 'direita')

# Função particionar usada para encontrar o pivo e organizar a lista
def particionar(lista, left, right):
    # Cria uma variável, com o intervalo entre o fim e inicio da lista elevado a 2
    center = (right - left) >> 1
    pivot = lista[left+center]
    j = right
    while True:
        while lista[left] < pivot:
            left += 1
        
        while lista[j] > pivot:
            j -= 1
        
        if left >= j:
            break
    
        aux = lista[left]
        lista[left] = lista[j]
        lista[j] = aux
        left += 1
        j -= 1
    aux = lista[left]
    lista[left] = lista[right]
    lista[right] = aux
    return left
        
Quicksort(lista, 0, len(lista)-1, 'inicio')
print(lista)