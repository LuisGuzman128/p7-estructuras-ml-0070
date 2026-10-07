# UI Act 10 Estructuras de decisión y repetición
# Luis Axel Guzman Martinez
# NC 0070


# =========================
# IF
# =========================

# Ejemplo 1
edad = 18

if edad >= 18:
    print("Es mayor de edad")


# Ejemplo 2
calificacion = 90

if calificacion >= 60:
    print("Aprobado")


# =========================
# ELIF
# =========================

# Ejemplo 1
calificacion = 80

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Bien")


# Ejemplo 2
temperatura = 25

if temperatura > 30:
    print("Hace calor")
elif temperatura >= 20:
    print("Temperatura agradable")


# =========================
# ELSE
# =========================

# Ejemplo 1
edad = 15

if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")


# Ejemplo 2
numero = 7

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")


# =========================
# FOR
# =========================

# Ejemplo 1
for numero in range(1, 6):
    print(numero)


# Ejemplo 2
for numero in range(1, 11):
    print(numero * 2)


# Ejemplo 3
for letra in "Python":
    print(letra)


# =========================
# WHILE
# =========================

# Ejemplo 1
numero = 1

while numero <= 5:
    print(numero)
    numero += 1


# Ejemplo 2
contador = 10

while contador >= 1:
    print(contador)
    contador -= 1


# Ejemplo 3
numero = 2

while numero <= 10:
    print(numero)
    numero += 2


print("Programa realizado por Axel Guzman 0070")