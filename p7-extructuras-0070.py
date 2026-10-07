# UI Act 10 Estructuras de decisión y repetición
# Luis Axel Guzman Martinez
# NC 0070

print("=== IF ===")

edad = 18

if edad >= 18:
    print("Es mayor de edad")


calificacion = 90

if calificacion >= 60:
    print("Aprobado")


print("=== ELIF ===")

calificacion = 80

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Bien")


temperatura = 25

if temperatura > 30:
    print("Hace calor")
elif temperatura >= 20:
    print("Temperatura agradable")


print("=== ELSE ===")

edad = 15

if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")


numero = 7

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")


print("=== FOR ===")

for numero in range(1, 6):
    print(numero)


for numero in range(1, 11):
    print(numero * 2)


for letra in "Python":
    print(letra)


print("=== WHILE ===")

numero = 1

while numero <= 5:
    print(numero)
    numero += 1


contador = 10

while contador >= 1:
    print(contador)
    contador -= 1


numero = 2

while numero <= 10:
    print(numero)
    numero += 2


print("Programa realizado por Axel Guzman 0070")