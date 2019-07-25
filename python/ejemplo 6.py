edad= int(input("dijite su edad"))
genero = input ("dijite su sexo, H hombre, M mujer")
if edad>=18:
    if genero in 'Hh':
        print ("señor usted es mayor de edad")
    elif genero in 'Mn':
        print ("señorita usted es mayor de edad")
    else:
        print("dato incorrecto")
else:
    if genero in 'Hh':
        print ("señor usted es menor de edad")
    elif genero in 'Mh':
        print ("señorita usted es menor de edad")
    else:
        print("dato in correcto")
