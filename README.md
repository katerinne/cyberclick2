# cyberclick2
-----------------------
* El Programa necesita de entrada un archivo input.txt con valores para procesar
* Tiene 3 salidas
    * Primera parte: 
        entrada: 1-3 a: abcde 
                 1-3 b: cdefg 
                 2-9 c: ccccccccc 

        Cada línea representa la política y la contraseña que debe cumplirla. La política de contraseñas indica el número mínimo y el número máximo de veces que se debe repetir la letra que hay a continuación. Así pues, "1-3 a" significa que la contraseña debe de contener la letra "a" un mínimo de 1 y un máximo de 3 veces. Siguiendo esta norma, en el ejemplo anterior hay un total de 2 contraseñas válidas. 


    * Segunda Parte: 

        La política describe lo siguiente: dos posiciones en la contraseña donde el número indica la posición del carácter (siendo 1 el primero, 2 el segundo… es decir, no hay índice 0). Entonces, exactamente 1 de las dos posiciones que aparecen deben de contener el carácter marcado, otras ocurrencias del carácter son irrelevantes. 
        
        Entonces: 
            1-3 a: abcde es válida: la posición 1 contiene a y la posición 3 no. 
            1-3 b: cdefg es no válida: Ni la posición 1 ni la 3 contienen el carácter b. 
            2-9 c: ccccccccc es no válida. Las dos posiciones 2 y 9 contienen el carácter c. 
    
    * Salir: Finaliza el programa.