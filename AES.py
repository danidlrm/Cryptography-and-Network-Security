from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
import os
import base64

#mensaje de texto
mensaje = "redhotchillipeppers"

#mensaje a bytes
mensaje_bytes = mensaje.encode("utf-8")

#datos asociados autenticados
aad = b"clase-aes-computacional"

#llave AES de 256 bits
llave = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(llave)

#nonce de 12 bytes
nonce = os.urandom(12)

#cifrado con AES-GCM
ciphertext = aesgcm.encrypt(nonce, mensaje_bytes, aad)
print("CIFRADO AES-GCM:")
print("llave en Base64:", base64.b64encode(llave).decode())
print("nonce en Base64:", base64.b64encode(nonce).decode())
print("ciphertext + tag en Base64:", base64.b64encode(ciphertext).decode())

#desifrado
descifrado = aesgcm.decrypt(nonce, ciphertext, aad)
print("\nDESCIFRADO:")
print("Mensaje descifrado:", descifrado.decode("utf-8"))

#modificar el ciphertext y descifrar
ciphertext_modificado = bytearray(ciphertext)
ciphertext_modificado[0] ^= 1
print("\nCIPHERTEXT CON BYTE MODIFICADO:")
try:
    aesgcm.decrypt(nonce, bytes(ciphertext_modificado), aad)
    print("Descifrado funciona")
except InvalidTag:
    print("Error")

#cambiar el AAD y descifrar 
aad_cambiado = b"clase-modificada"
print("\nAAD MODIFICADO:")
try:
    aesgcm.decrypt(nonce, ciphertext, aad_cambiado)
    print("Descifrado funciona")
except InvalidTag:
    print("Error")


#diferentes nonces
nonce1 = os.urandom(12)
nonce2 = os.urandom(12)
c1 = aesgcm.encrypt(nonce1, mensaje_bytes, aad)
c2 = aesgcm.encrypt(nonce2, mensaje_bytes, aad)
print("\nNONCES:")
print("C1:", base64.b64encode(c1).decode())
print("C2:", base64.b64encode(c2).decode())
