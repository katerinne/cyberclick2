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
    except FileNotFoundError:
        print("No se ha conseguido el archivo")        
    except:
        print("Ha ocurrido un error con el archivo")
    finally:
        print("Ha finalizado el programa")
        quit()
    
    
def separador_cadena(linea): # Metodo que procesa la linea de entrada	
	linea1=linea.replace(':' , '')
	linea2=linea1.replace('-' , ' ')
	cadenaespacios=linea2.split(' ')	
	return cadenaespacios

leer_archivo()

while (resp!= '3'):	
	print("\n**  Menú  ***")
	print("1.- Primera parte ")
	print("2.- Segunda parte")
	print("3.- Salir")	
	resp = input("Opcion: ")
	if (resp == '1'):
		pass#primera_parte()
	elif (resp == '2'):
		pass#segunda_parte()	
	elif (resp == '3'):
		print("Adios...")
	else:
		print("Opcion incorrecta")