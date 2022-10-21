opcion = 100

ciclistas = []

print("1. Agregar ciclista")
print("2. Ver resultados")

while(opcion != 0):

    datos = {}
    opcion = int(input('Digite una opcion: '))
    if opcion == 1:
        datos['nombre'] = input('Digite el nombre: ')
        datos['edad'] = input('Digite la edad: ')
        datos['pais'] = input('Digite el pais: ')
        datos['equipo'] = input('Digite el equipo: ')
        datos['tiempo'] = int(input('Digite el tiempo: '))
        ciclistas.append(datos)
        print(ciclistas)

    elif opcion == 2:

        tiempo = 100
        for ciclista in ciclistas:
            if ciclista['tiempo'] < tiempo:
                tiempo = ciclista['tiempo']
        print(f"El ciclista mas rápido es {ciclista['nombre']} con un tiempo de: {tiempo} min")
    
    elif opcion == 0:
        break
    else: 
        print('Opcion no válida')