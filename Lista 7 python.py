#Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).



#Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
#Lista = [4,1,8,9,6,3,6]
#Lista.sort()
#print (Lista)

#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

mes = int ( input ("Coloque el numero del mes:  "))

enero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 31]
febrero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
marzo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 31]
abril = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
mayo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
junio = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 31]
julio = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30, 31]
agosto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
septiembre = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
octubre = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
noviembre = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
diciembre = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

if 1 == mes:
    print ("Es Enero y tiene ", len(enero)) 
elif 2 == mes:
    print ("Es Febrero y tiene ", len(febrero)) 
elif 3 == mes:
    print ("Es Marzo y tiene ", len(marzo)) 
elif 4 == mes:
    print ("Es Abril y tiene ", len(abril)) 
elif 5 == mes:
    print ("Es Mayo y tiene ", len(mayo)) 
elif 6 == mes:
    print ("Es Junio y tiene ", len(junio)) 
elif 7 == mes:
    print ("Es Julio y tiene ", len(julio)) 
elif 8 == mes:
    print ("Es Agosto y tiene ", len(agosto)) 
elif 9 == mes:
    print ("Es Septiembre y tiene ", len(septiembre)) 
elif 10 == mes:
    print ("Es Octubre y tiene ", len(octubre)) 
elif 11 == mes:
    print ("Es Noviembre y tiene ", len(noviembre)) 
elif 12 == mes:
    print ("Es Diciembre y tiene ", len(diciembre)) 
