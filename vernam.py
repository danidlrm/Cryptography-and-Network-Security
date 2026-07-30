def cifrar(mensaje, clave):
    resultado = []

    for i in range(len(mensaje)):
        xor = ord(mensaje[i]) ^ ord(clave[i])
        resultado.append(xor)

    return resultado


def descifrar(cifrado, clave):
    mensaje = ""

    for i in range(len(cifrado)):
        letra = chr(cifrado[i] ^ ord(clave[i]))
        mensaje += letra

    return mensaje


mensaje = "VALAR DOHARYS"
clave = "VALAR MORGHULIS"

cifrado = cifrar(mensaje, clave)

print("Mensaje:", mensaje)
print("Clave:", clave)
print("Cifrado:", cifrado)

descifrado = descifrar(cifrado, clave)
print("Descifrado:", descifrado)