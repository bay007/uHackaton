'''
#EJERCICIO 2
respuesta_usuario = float(input("Respuesta Area\n"))

base = 10.3
altura = 5

respuesta_area = (base * altura)/2

def area_triangulo (x):
    if x == respuesta_area:
        print (True)

    else:
        print (False)

y = area_triangulo(respuesta_usuario)
'''

#Ejercicio 4
def palabras ():
    for
oraciones_palindroma_1 = "Anita lava la tina"
palindroma_1 = oraciones_palindroma_1.lower()
x = palindroma_1.replace(" ","")

x_1 = x[::-1]

oraciones_palindroma_2 = "A mi me mima"
palindroma_2 = oraciones_palindroma_2.lower()
y = palindroma_2.replace(" ","")

y_1 = y[::-1]

oraciones_palindroma_3 = "Mi mama masa la masa en la mesa"
palindroma_3 = oraciones_palindroma_3.lower()
z = palindroma_3.replace(" ","")

z_1 = z[::-1]

print (x)
print (y)
print (z)

print (x_1)
print (y_1)
print (z_1)

#Ejercicio 6
#cliente = int(input("Cuantos son?\n"))

def leche (x):
    leche_total = 1.5
    cada_vasito = 0.125

    total_vasitos = leche_total / cada_vasito

    respuesta_6 = (int(total_vasitos))

    if x = total_vasitos:
        print (True)
    else:
        print (False)

leche(29)
