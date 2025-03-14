#Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
Lista = []
contador = 0
print ("Valores primera lista ")

while contador < 5:
    valor = (input ("Escribe el primer valor: "))
    contador = contador + 1
    Lista.append(valor)
print(Lista)
        
 