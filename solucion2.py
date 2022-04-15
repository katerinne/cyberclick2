from io import open


resp = "0"
lista = []

def leer_archivo(): # Metodo para leer el archivo 
    try:
        fichero = open('input.txt','r')
        lineas = fichero.readlines()
        fichero.close()
        for linea in lineas:
            lista.append(separador_cadena(linea))
    except:
        print("No se ha conseguido el archivo")        
        print("Ha finalizado el programa")
        quit()
        
    
    
def separador_cadena(linea): # Metodo que procesa la linea de entrada	
	linea1=linea.replace(':' , '')
	linea2=linea1.replace('-' , ' ')
	cadenaespacios=linea2.split(' ')	
	return cadenaespacios

def primera_parte():
	cont =0
	for linea in lista:
		li=int(linea[0])
		ls=int(linea[1])
		letra=(linea[2])
		i=int(linea[3].count(letra))	
		if (i>=li and i<=ls):
			cont +=1
	print("\nEn la primera parte hay ",cont," contraseñas validas en el input")

def segunda_parte():
	cont = 0
	for linea in lista:
		li=int(linea[0])-1
		ls=int(linea[1])-1
		letra=linea[2]	
		contrasena=linea[3]
		if(contrasena[li]==letra):
			if(contrasena[ls]!=letra):
				cont += 1
		else:
			if(contrasena[ls]==letra):
				cont += 1
	print("\nEn la segunda parte hay ",cont," contraseñas validas en el input")

leer_archivo()

while (resp!= '3'):	
	print("\n**  Menú  ***")
	print("1.- Primera parte ")
	print("2.- Segunda parte")
	print("3.- Salir")	
	resp = input("Opcion: ")
	if (resp == '1'):
		primera_parte()
	elif (resp == '2'):
		segunda_parte()	
	elif (resp == '3'):
		print("Adios...")
	else:
		print("Opcion incorrecta")