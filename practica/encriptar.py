
def encriptarValor(valor):
    codigo = ""
    for letra in valor:
        if not letra.isalpha():
            continue
        letra = letra.upper()
        asciiLetra = ord(letra) + 1
        if asciiLetra > ord("Z"):
            asciiLetra = ord("A")
        codigo += chr(asciiLetra)
    print(codigo)
