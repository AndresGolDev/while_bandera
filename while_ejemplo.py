#bucle while
print(f"Digite un valor o escriba fin para finalizar el Programa\n")

bandera = 0

while  bandera == 0:
    valor = input("Digite el valor: ")
    if valor == "Fin".lower():
        print("Fin del Programa")
        bandera = 1
    else:
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                print("Es positivo")
            elif valor < 0:
                print("Es Negativo")
            else:
                print("El numero es 0")
        else:
            print("solo se permiten numero enteros")
