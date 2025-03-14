#Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día

Lista = []
Lista_2 = []
contador = 0

print ("Escribre la temperatura maxima de 5 dias")
while contador<3:
    valor =int( (input ("Escribe la temperatura maxima: ")))
    valor_2 = int ((input ("Escribe la temperatura minima: ")))
    contador = contador + 1
    Lista.append(valor)
    Lista_2.append(valor_2)
print (Lista)
print (Lista_2)
temperatura0 = (Lista[0] + Lista_2[0])/2 
#temperatura1 = (Lista[1] + Lista_2[1])/2 
#temperatura2 = (Lista[2] + Lista_2[2])/2 
#temperatura3 = (Lista[3] + Lista_2[3])/2 
#temperatura4 = (Lista[4] + Lista_2[4])/2 
 
print (temperatura0)
#print(Lista)

for i in Lista:
    if i > 6:
        print (i)



