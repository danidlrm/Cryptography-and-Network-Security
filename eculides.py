def Euclides (a,b):
    while True:
        residuo = a % b
        if residuo == 0:
            return b
        else:
            a = b
            b = residuo 
            
a = int(input("ingresa el primer numero: "))
b = int(input("ingrese el segundo numero: "))

Euclides(a,b)
resultado = Euclides(a,b)
print("el maximo comun divisor es: ", resultado)