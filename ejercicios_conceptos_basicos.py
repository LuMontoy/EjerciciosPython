from datetime import date


print("********** EJERCICIO 1 **********")
base = float(input("Ingrese el valor de la base: \n"))
altura = float(input("Ingrese el valor de la altura: \n"))

area = (base * altura) / 2

print("El área del triángulo es ", area)
print("********************************* \n")


print("********** EJERCICIO 2 **********")
PRECIO_DOLAR = 3910.5
cantidad_dolares = float(input("Ingrese la cantidad de dólares que desea convertir: \n"))

equivalente_pesos = cantidad_dolares * PRECIO_DOLAR

print(cantidad_dolares, " dólares equivalen a ", equivalente_pesos, " pesos colombianos")
print("*********************************\n")


print("********** EJERCICIO 3 **********")
temperatura_centigrados = float(input("Ingrese la temperatura en grados centígrados: \n"))

temperatura_fahrenheit = (temperatura_centigrados * (9/5)) + 32

print(temperatura_centigrados, " grados centígrados equivalen a ", temperatura_fahrenheit, " grados fahrenheit")
print("*********************************\n")


print("********** EJERCICIO 4 **********")
segundos_lustro = 5 * 365 * 24 * 60 * 60

print("Un lustro equivale a ", segundos_lustro, " segundos")
print("********************************* \n")


print("********** EJERCICIO 5 **********")
VELOCIDAD_LUZ = 3 * (10 ** 8)
DISTANCIA_SOL_MARTE = 25 * (10 ** 10)

tiempo = DISTANCIA_SOL_MARTE / VELOCIDAD_LUZ

print("La cantidad de segundos que le toma a la luz viajar de sol a Marte es: ", tiempo)
print("********************************* \n")


print("********** EJERCICIO 6 **********")
DIAMETRO = 50
DISTANCIA = 100000
PI = 3.14

distancia_una_vuelta = PI * DIAMETRO
vueltas = DISTANCIA / distancia_una_vuelta

print("El númeo de vueltas que da la llanta en 1Km es: ", vueltas)
print("********************************* \n")


print("********** EJERCICIO 7 **********")
ALTURA = 20
ANGULO = 22

# Tangente (22°) = 0.4 
sombra = 20 / (0.4)

print("La sombra del edificio es: ", sombra, " metros")
print("********************************* \n")


print("********** EJERCICIO 8 **********")
edad_uno = int(input("USUARIO 1 \n Ingrese su edad: \n"))
edad_dos = int(input("USUARIO 2 \n Ingrese su edad: \n"))

igual = edad_uno is edad_dos

print("¿Las edades son iguales?: ", igual)
print("********************************* \n")


print("********** EJERCICIO 9 **********")
hoy = date.today()
print("INGRESE SU FECHA DE NACIMIENTO \n")
dia_nacimiento = int(input("Día: \n"))
mes_nacimiento = int(input("Mes (número de 1 a 12): \n"))
ano_nacimiento = int(input("Año: \n"))
fecha_nacimiento = date(ano_nacimiento, mes_nacimiento, dia_nacimiento)

diferencia_dias = hoy - fecha_nacimiento
diferencia_meses = int(diferencia_dias.days / 30)

print("Desde su fecha de nacimiento han pasado: ", diferencia_meses, " meses")
print("********************************* \n")


print("********** EJERCICIO 10 **********")
print("INGRESE LA NOTA DE CADA MATERIA \n")
nota_espanol = float(input("Español: \n"))
nota_matematicas = float(input("Matematicas: \n"))
nota_economia = float(input("Economia: \n"))
nota_programacion = float(input("Programación: \n"))
nota_ingles = float(input("Ingles: \n"))

promedio = (nota_ingles + nota_programacion + nota_economia + 
	nota_matematicas + nota_espanol) / 5

print("Tu promedio es: ", promedio)
print("********************************* \n")