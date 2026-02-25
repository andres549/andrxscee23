
print ("Registro de Participantes, Taller de Programación")
cantidad_personas = int (input ("¿Cuántas personas desea registrar?: "))



for i in range (cantidad_personas):
    nombre= input("Ingrese su nombre:")
    edad = int (input("Ingrese su edad: "))

    if edad < 15: 
        print ("No cumple con los requisitos de edad.")

    while edad < 0: 
        print ("Ingresó una edad inadecuada.")
        edad = int (input ("Ingrese nuevamente la edad: "))
        if edad >= 15:
            print ("Puede continuar")
        else:
            print ("No cumple con los requisitos de edad.")

    conocimientos = input ("¿Tiene conocimientos básicos de computación? ingrese s/n: ")
    if conocimientos == "no":
        print ("No cuenta con los conocimientos requeridos.")  
    if conocimientos == "no":
        print ("No es apto para el taller.")
if conocimientos == "si":
    print ("Puede realizar el taller.")

print ("Ha finalizado el registro.")