
import os
libros=[]
libros_prestados=[]
def registrar():
    try:
#Ingreso de datos de los libros
        print("elegiste la opción 1, por favor ingresa los siguientes datos: ")
        titulo=input("Titulo del libro: ")
        autor=input("Quien es el autor del libro: ") #queda la duda de los libros publicados A.C para poder controlarlos habria que hacer un una control que dijera "Es A.C o D.C" y agregar la info al lado del año de publicacion imprimiento las variables juntas o generando una columa de "AC/DC"
        publicacion=int(input("Año en que fue publicado el libro: "))
        sku=input("SKU del libro(El SKU es: (las 6 primeras letras del título del libro)-(las 3 primeras letras del autor)-(año de publicación.)): ")
#Validacion de que los datos estén completamente ingresados.
        if not titulo or not autor or not publicacion or not sku or publicacion<=0:
            print("Faltan datos para poder registrar el libro, por favor intente nuevamente")
    except ValueError: print("El dato ingresado no corresponde, favor intentar de nuevo")


#Creación diccionario de cada libro
    libro={
        'Titulo del libro':titulo,
        'Autor del libro':autor,
        'Año de publicación':publicacion,
        'SKU':sku
    }

#Agregar el diccionario a la lista de libros
    libros.append(libro)
    print("¡Felicidades! El registro del libro ha sido correcto")

def prestar():
    print("Elegiste la opción 2, por favor ingresa los siguientes datos para validar la disponibilidad del libro: ")
#Agregar datos para la validacion de disponibilidad
    usuario=input("Ingresa tu nombre de usuario: ").lower()
    skuA=input("Ingresa el sku del libro que quieres(El SKU es (las 6 primeras letras del título del libro)-(las 3 primeras letras del autor)-(año de publicación.)): ").lower()
    if skuA != libros_prestados:
#diccionario de prestamo
        libro_prestado={
            'nombre usuario prestado':usuario,
            'SKU':skuA
        }
#Agregar a los libros pedidos
        libros_prestados.append(libro_prestado)
        print("El registo de prestamo se realizó correctamente, recuerda devolver el libro en la fecha que corresponda. ¡Disfrutalo!")
    else:  
        print("El libro no se encuentra disponible. Puedes acercarte al personal para consultar la fecha de devolucion y otras opciones similares al libro solicitado.")

def listar():
    print("Haz elegido la opción 3, a continuación se desplegará la lista de libros registrados hasta la fecha: ")
#Se imprimen cabezas de columnas
    print("TITULO\t\tAUTOR\t\tAÑO DE PUBLICACIÓN\t\tSKU")
    for libro in libros:
#Se imprime lista de libros solicitada
        #Version alternativa que tambien funciona: print(f"{libro['Titulo del libro']}\t\t{libro['Autor del libro']}\t\t{libro['Año de publicación']}\t\t{libro['SKU']}")
        print("{:20s}{:10s}{4d}{15s}".format({libro['Titulo del libro']},{libro['Autor del libro']},{libro['Año de publicación']},{libro['SKU']}))



def imprimir():
    print("Haz elegido la opcion 4, a continuacion se generará el archivo solicitado...")
    with open("prestamos.txt","w") as archivo:
        archivo.write("usuario\t\tSKU\n")
        for libro_prestado in libros_prestados:
            archivo.write(f"{libro_prestado['nombre usuario prestado']}\t\t{libro_prestado['SKU']}\n")
    print("El archivo se encuentra en la siguiente ruta para su revisión: ") , os.getcwd

menus=True
def menu():
    try:
        while menus:    
            print("* * * * * MENÚ * * * * *")
            elección=int(input("Bienvenido al portal de nuestra bibliotéca, elige qué deseas hacer: \n1.Registrar un libro\n2.Prestar libro\n3Listar todos los libros\n4.Imprimir reporte de prestamos\n5.Salir del programa\n Tu elección: "))
            if elección==1:
                registrar()
            elif elección==2:
                prestar()
            elif elección==3:
                listar()
            elif elección==4:
                imprimir()
            elif elección==5:
                print("Programa finalizado...\n Desarrollado por Abraham Herrera\nRUN:19.960.85-4")
                break
            else: print("La opción ingresada no es valida, por favor intente nuevamente.")
    except ValueError: print("La opción ingresada no es valida, por favor intente nuevamente.")        
