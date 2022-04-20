"""Programa No. 7:
Verificar si dos números son diferentes"""

print("----------------------------")
print("-----NÚMEROS DIFERENTES-----")
print("----------------------------")

#input 
X = int(input("Digite el valor de X: "))
Y = int(input("Digite el valor de Y: "))

#processing
if X != Y:
    msj = "Son diferentes"
    print("Son diferentes")
else: 
    msj = "Son iguales"
#espacios son indentación: las líneas se ejecutan si las condiciones son o verdaderas, o falsas. 

#output
print("Los números " + msj)
