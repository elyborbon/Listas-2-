#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
#lista = [1,2,3,4,5,6,7,8,9,10]

#for listas in lista:
 #   cuadrado = pow (listas, 2) 
  #  cubo = pow (listas, 3)
  #  print (cuadrado, cubo)

#Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
#Lista = []

#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
list = []

Nota_1 = int (input("Calificacion nota 1: "))
Nota_2 = int (input("Calificacion nota 1: "))
Nota_3 = int (input("Calificacion nota 1: "))
Nota_4 = int (input("Calificacion nota 1: "))
Nota_5 = int (input("Calificacion nota 1: "))

list.append(Nota_1)
list.append(Nota_2)
list.append(Nota_3)
list.append(Nota_4)
list.append(Nota_5)
for i in list:
    print (i)
media = sum(list)/len(list)
Nota_alta = max(list)
Nota_baja = min(list)
print ("La media de la lista es: ", media)
print ("La nota mas alta es: ", Nota_alta)
print ("La nota mas baj es: ", Nota_baja)

