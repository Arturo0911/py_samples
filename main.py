# Solo declaramos la lista de opciones para poder usar una funcion que las muestre por pantalla cada vez que llame a la funcion
options_list = ["1. INGRESO DE PELICULAS","2. INGRESO DE ACTORES DE PELICULAS.","3. REPORTE DE ACTORES.",
"4. CALIFICACION DE PROTAGONISTAS","5. RANKING DE PELICULAS.","6. SALIR"]



# ESTO ES PARA LA OPCION 1
db_movies = {} # aqui declaraemos un diccionario donde agregaremos a las peliculas y sus respectivos promedios de puntajes
db_movies_points = {}

db_backup = {} # esto es para hacer pruebas con las demás opciones, no le paren bola xD

lista_peliculas = []
lista_puntaje = []
lista_TOP = []
lista_promedios = []

# ESTO ES DE LA OPCION 3
lista_backup = []



# ESTO ES PARA LA OPCION 4
peliculas_actores = {}
calificacion_de_audiencia = {}
################################


#========================================================================== FUNCIONES =======================================================

def show_options(): # esta funcion es para mostrar por pantalla las listas de opciones una tras de otra
    print("\n")
    for x in options_list:
        print(x,"\n")

def validator(values_): # esta funcion verifica que sea numeros menores a 10
    split = ","
    values_list = values_.split(split)
    counter = 0
    
    for i in values_list:
        #print(int(i))
        if (int(i) > 10):
            counter = counter +1
    if(counter >0):
        return False
    else:
        return True
            

   

def delete_comma(values): # esta funciona es para eliminar la coma y sacar el promedio

    suma = 0 # esta suma es la que nos indicará el valor del puntaje de cada pelicula
    promedio = 0 # para calcular el promedio de cada pelicula
    split = "," # esta variables es para poder elinminar la coma de lo que se ingresa por teclado
    values_list = values.split(split)
    for z in values_list:
        suma = suma + int(z)
    promedio = "{0:.0f}".format((suma/ len(values_list)))
    return promedio



def OPTION_1(movie, points): # esta es la funcion de la opcion uno
    suma = 0 # esta suma es la que nos indicará el valor del puntaje de cada pelicula
    promedio = 0 # para calcular el promedio de cada pelicula
    split = ","
    values_list = points.split(split)
    print(values_list)

    
    for z in values_list:
        suma = suma + int(z)
    promedio = int(suma/ len(values_list))
        
    lista_peliculas.append(movie)
    lista_puntaje.append(promedio)
    print(lista_puntaje)
    lista_puntaje.sort(reverse=True)
    print(lista_puntaje)
    db_movies[movie] = promedio
    db_movies_points[promedio] = movie
    return db_movies




def sort_list():
    
    for k in lista_puntaje:
        lista_TOP.append(db_movies_points[k])

    print("El TOP peliculas es=>: ")
    for l in lista_TOP:
        """if(l not in lista_backup ):
            lista_backup.append(l)"""

        print(l, "pelicula... \n")
    #print(lista_TOP)


#==================================2

# ESTO ES PARA LA OPCION 2

lsita_backup_actores = []
lista_actores_ordenada = []


def validator_actor(actor):
    split = ", "
    lista_actores = actor.split(split)
    counter = 0
    for items in lista_actores:
        if (items[len(items)-1] != "F" and items[len(items)-1] != "f" and
             items[len(items)-1] != "M" and items[len(items)-1] != "m"):
            counter = counter + 1
    if(counter > 0):
        return False
    else:
        return True


def OPTION_2(actors):
    split = ", "
    lista_actores = actors.split(split)
    
    
    for a in lista_actores:
        
        if(a not in lista_actores_ordenada):
            if(a[len(a)-1] == "F" or a[len(a)-1] == "f"):
                #print(a,a[len(a)-1])
                lista_actores_ordenada.append(a)
                #lista_actores.remove(a)
            else:
                lsita_backup_actores.append(a)
                #lista_actores.remove(a)

    print(lista_actores_ordenada)

def incorporar_actores():
    
    for c in lsita_backup_actores:
        lista_actores_ordenada.append(c)
    print(lista_actores_ordenada)



#==================================3
nueva_lista = [] # esto es para verficiar que cuando querramos contar los actores que estan en cada rankin no se repitan cuando vayamos a 
# a imprimirlos por pantalla, por eso usamos esta lista
lista_rankin = []
lista_rankin_puntajes = []

db_actores_counters = {}
objeto_ = {}



def ranking(actor):
    split = ", "
    lista_actores = actor.split(split)
    for act in lista_actores:
        lista_rankin.append(act)
        
    print(lista_rankin)

def conteo():
    print("lista conteo %s"%lista_rankin)
    for value in lista_rankin:
        if(value not in nueva_lista):
            
            db_actores_counters[value] = lista_rankin.count(value)
            nueva_lista.append(value)


    for actors_4 in nueva_lista:
        #print(actors_4)
        #print(db_actores_counters[actors_4])
        lista_rankin_puntajes.append(db_actores_counters[actors_4])

    lista_rankin_puntajes.sort()
    for w in  nueva_lista:
        if(db_actores_counters[w] == lista_rankin_puntajes[len(lista_rankin_puntajes)-1]):
            print(">>Esste es el actor %s con mas veces %s"%(w,db_actores_counters[w]))
    
    for loop  in lista_rankin:
        print(loop)
        
    #print(nueva_lista)
    #print("lista_rankin_puntajes",lista_rankin_puntajes)
    print(db_actores_counters)

#==================================4
















# ================================================================================================================================

while(True):
    try:
        show_options()
        option =  int(input(">>Ingrese una opcion: "))
        if(option == 1):
            print("INGRESO DE PELICULAS.")
            while(True):
                try:
                    nombre_pelicula = input(">>Ingrese el nombre de una pelicula: ")
                    nombre_pelicula_ = nombre_pelicula.lower()
                    if(nombre_pelicula_ =="ninguna"):
                        break
                    
                    while(True):
                        valores =  input(">>ingrese la puntuacion de cada pelicula separada por una coma: ")
                        if(validator(valores) is  True):
                            print(">>option 1: ",OPTION_1(nombre_pelicula,valores))
                            break
                        else:
                            print(">>los valores ingresados deben ser menores o iguales a 10")

                except:
                    print(">>Error al ingresar numeros de calificaciones")
            sort_list() # llamamos a esta funcion para que indique cual es el top de peliculas basándose en el puntjae

        elif(option == 2):
            print("INGRESO DE ACTORES DE PELÍCULAS.")
            while(True):
                for pelicula in lista_peliculas:
                    
                    while(True):
                        print(">>ingrese los actores de %s"%pelicula)
                        actores = input(">>: ")
                        if(validator_actor(actores)is True):
                            break
                        else:
                            print(">>Debe colocar F o M seguido de la | para indicar el genero del actor...")
                    
                    
                    # ESTO ES PARA ORDENAR LAS PELICULAS CON SUS RESPECTIVOS ACTORES.  
                    split = ", "
                    lista_actores = actores.split(split)
                    peliculas_actores[pelicula] = lista_actores
                    OPTION_2(actores)
                    ranking(actores)
                break
            incorporar_actores()
        elif(option == 3):
            print("3. REPORTE DE ACTORES.")
            conteo()
        elif(option == 4):
            print("4. CALIFICACION DE PROTAGONISTAS")

            for caracter in lista_TOP:
                print(caracter, peliculas_actores[caracter])
                for caracter_y in peliculas_actores[caracter]:
                    
                    while (True):
                        try:
                            while(True):
                                print("actor: ",caracter_y)
                                calificar = int(input("ingrese una calificacion de 1 a 5 para cada actor: "))
                                print(calificar)
                                if(calificar > 5 or calificar < 1):
                                    print("calificacion debe ser entre 1 a 5")
                                else:
                                    break
                                    
                            final = calificar + db_actores_counters[caracter_y]
                            calificacion_de_audiencia[caracter_y] = str(final)
                            #print("Calificacion por audiencia a cada actor: ",calificacion_de_audiencia)
                            break
                        except :
                            print("Error en el ingreso de calificacion")

            print("Calificacion por audiencia a cada actor: ",calificacion_de_audiencia)
        elif(option == 5):
            print("5. RANKING DE PELICULAS.")
            

            #COLOQUE ESTAS OPCIONES PORQUE LA OPCION 5 SE DEBE TRABAJAR CON 10 PELICULAS EL RESTO FUNCIONA

            """
                    SI VAN A TRABAJAR CON 10 PELICULAS DESCOMENTEN ESTO: 

                    for x in lista_TOP: # auqi va la lista top
                        print("%s  "%x,end="")
                        #print(db_movies[x])
                    #db_movies

                    while(True):
                        try:
                            

                            while(True):
                                numero_1 = int(input("ingrese primer numero: "))
                                numero_2 = int(input("ingrese segundo numero:  "))
                                if((numero_1 > 10 or numero_1 < 10) and (numero_2 > 10 or numero_2 < 10)):
                                    break
                                else:
                                    print("numeros deben ser menores a 10 pero mayores a 0")


                            for y in lista_TOP:
                                #print("aqui verificaremos si la funcion cumple")
                                if( (db_movies[y] > numero_1 or  db_movies[y] < numero_1) and (db_movies[y] > numero_2 or  db_movies[y] < numero_2)):
                                    print(y, db_movies[y])
                                    break
                                else:
                                    print("ninguna cumple ")
                            break
                        except:
                            print("error en elegir numeros...")


            """




            print("coleccion de peliculas...")
            option_5 ={'aladdin': 7, 'bobsponja': 7, 'chucky': 8,'aladdin2': 7, 'aladdin3': 4,'aladdin4': 9,
                 'aladdin5': 6,'aladdin6': 8, 'aladdin7': 2,'aladdin8': 7}

            peliculas_lista_option_5 = ["aladdin", "aladdin2", "aladdin3","aladdin4",
                "aladdin5", "aladdin6","aladdin7", "aladdin8", "bobsponja","chucky"]


            #COLOQUE ESTAS OPCIONES PORQUE LA OPCION 5 SE DEBE TRABAJAR CON 10 PELICULAS EL RESTO FUNCIONA



            for x in peliculas_lista_option_5: # auqi va la lista top
                print("%s  "%x,end="")
                #print(db_movies[x])
            #db_movies

            while(True):
                try:
                    

                    while(True):
                        numero_1 = int(input("ingrese primer numero: "))
                        numero_2 = int(input("ingrese segundo numero:  "))
                        if((numero_1 > 10 or numero_1 < 10) and (numero_2 > 10 or numero_2 < 10)):
                            break
                        else:
                            print("numeros deben ser menores a 10 pero mayores a 0")


                    for y in peliculas_lista_option_5:
                        #print("aqui verificaremos si la funcion cumple")
                        if( (option_5[y] > numero_1 or  option_5[y] < numero_1) and (option_5[y] > numero_2 or  option_5[y] < numero_2)):
                            print(y, option_5[y])
                            break
                        else:
                            print("ninguna cumple ")
                    break
                except:
                    print("error en elegir numeros...")
               

        elif(option == 6):
            print(">>Salir")
            break
        else:
            print(">>numero fuera de rango. ")
    except:
        print("Error al ingresar el numero de opcion")


#print("Esta es la lista de peliculas: ", lista_peliculas)
