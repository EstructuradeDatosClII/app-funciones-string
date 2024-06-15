def resumen(valor):
    suma = 0
    listNumeros = valor.split()
    try:
        for num in listNumeros:
            suma += float(num)
        print("La suma es: ", suma)
        print("Cantidad de número", len(listNumeros))
        print("Cantidad de caracteres del valor: ", len(valor))
    except:
        print("Un valor de la lista no es NÚMERO")

def mensajeAlReves(valor):
    print(valor[::-1])

def validarPalindromo(valor):
    valorAlReves = valor[::-1]
    if(valor == valorAlReves):
        print("La Palabra es palíndromo")
    else:
        print("La Palabra no es palíndromo")