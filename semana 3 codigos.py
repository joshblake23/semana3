print("Bienvenido, estimado")
nombre=input("Ingrese su nombre")
apellido1=input("Ingrese primerApellido")
apellido2=input("Ingrese segundoApellido")

print("Calculadora simple")
numero1=input("Ingresar un numero")
numero2=input("Ingresar un segundo numero")             
operacion1= int(numero1) + int(numero2)
operacion2= int(numero1) - int(numero2)
operacion3= int(numero1) / int(numero2)
operacion4= int(numero1) * int(numero2)
print("El resultado de la suma es=" +str(operacion1))
print("El resultado de la resta es=" +str(operacion2))
print("El resultado de la división es=" +str(operacion3))
print("El resultado de la multiplicación es=" +str(operacion4))

print("Área y perímetro de un cuadrado")
lado1=input("Ingresar un numero")
calculo1= int(lado1) * int(lado1)
calculo2= int(lado1) * int(4)
print("El área de un cuadrado es= "+str(calculo1))
print("El peímetro de un cuadrado es= "+str(calculo2))

print("Programa de un numero elevado a la potencia")
numero1= input("Ingresar un numero")
numero2= input("Ingresar un segundo numero")
operacion= int(numero1)** int(numero2)
print("El resultado es= "+str(operacion))
