
def validarString(valor):
    if(valor.isalpha()):
        print("Solo letras")
    else:
        print("No alfabético")

def validarNumero(valor):
    if(valor.isdigit()):
        print("Solo número")
    else:
        print("No es número")

def validarNumero(valor):
    if(valor.isalnum()):
        print("Solo letras y número")
    else:
        print("No es número ni letras")

def convertir(valor):
    valorAscci = ord(valor)
    print(valorAscci)
    print(chr(valorAscci))
    