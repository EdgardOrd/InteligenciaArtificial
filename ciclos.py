print("Ciclos for y while")

lista = ["Juan", "Pedro" ,"Enrique"]
numeros = [1,2,3,4,5,5,67,78,87]


#for index in range(0,10):#in, range recibe un valor inicial y un valor final
 #   print(index)

diccionario = {
    "nombre": "Juan",
    "Apellido": "Alvarenga",
    "Edad": "28"
}

# for value in diccionario.values():
#     print(value)

# for value in diccionario:
#     print(diccionario[value])

# for value in diccionario.items():
#     print(value)
algo =8
for key,value in diccionario.items():
    print(key,value)
    print(f"Key: {key}, value: {value}")#para concatenar
    print("key: " + key + ", value: " + value + " algo " + str(algo))
#  for value in lista:
#     print(value)

contador = 0

# while contador < len(numeros):
#     print(numeros[contador])
#     contador=contador + 1 """

numero = 6

for index in range(0,11):
    print(f"{numero}x{index} = {index*numero}")

while contador <=10:
    print(f"{numero}x{contador} = {contador*numero}")


    contador=contador+1
