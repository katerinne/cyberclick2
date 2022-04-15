from io import open
resp = "0"
lista = []

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