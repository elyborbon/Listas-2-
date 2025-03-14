#Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
Lista = []
Lista_2 = []
print ("Valores primera lista ")
valor_1=  (input ("Valor 1: "))
valor_2= (input ("Valor 2: "))
valor_3= (input ("Valor 3: "))
valor_4= (input ("Valor 4: "))
valor_5= (input ("Valor 5: "))

Lista.append(valor_1)
Lista.append(valor_2)
Lista.append(valor_3)
Lista.append(valor_4)
Lista.append(valor_5)

print ("Valores segundo lista ")
valor_11=  (input ("Valor 1: "))
valor_21= (input ("Valor 2: "))
valor_31= (input ("Valor 3: "))
valor_41= (input ("Valor 4: "))
valor_51= (input ("Valor 5: "))

Lista_2.append(valor_11)
Lista_2.append(valor_21)
Lista_2.append(valor_31)
Lista_2.append(valor_41)
Lista_2.append(valor_51)

print(Lista)
print(Lista_2)
suma = Lista +Lista_2
print ("La suma de la lista 1 y la lista 2 es : " ,suma)

