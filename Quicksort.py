
lista = [10,9,8,6,4,53,2]
# 2,4,6,8,9,2,10,53

def Quicksort(lista, left, right):
    if left < right:
        pivot = particionar(lista,left,right)
        Quicksort(lista,left, pivot - 1)
        Quicksort(lista,pivot,right)

def particionar(lista, left, right):
    pivot = (right - left) >> 1
    pivot = lista[left+pivot]
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
        
Quicksort(lista, 0, len(lista)-1)
print(lista)