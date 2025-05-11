from biblioteca import Biblioteca

GENEROS = [
    "Ficcion", "Ciencia Ficcion", "Fantasia", "Misterio",
     "Romance", "Triller", "Horror", "Historica",
      "Aventura", "Drama", "Art. Cientifico"]

def mostrar_menu():
    print("\n--- Menu de Biblioteca ---")
    print("1. Agregar Libro")
    print("2. Lista de Libro")
    print("3. Actualizar Libro")
    print("4. Eliminar Libro")
    print("5. Salir")

def elegir_genero():
    print("\nSeleccione un Genero")
    for i, genero in enumerate(GENEROS, 1):
        print(f"{i}. {generos}")
    while True:
        try:
            option = int(input("Ingrese el numero del genero: "))
            if 1 <= opcion <= len(GENEROS):
                return GENEROS[OPCION - 1]
            else:
                print("Opcion invalida. Intentelo nuevamente. ")
        except ValueError:
            print("Entrada invalida. Ingrese un numero. ")

def main():
    biblioteca = Biblioteca('data.json')

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            titulo = input("Ingrese el titulo: ")
            autor = input("Ingrese el Autor: ")
            anio = input("Ingrese el año: ")
            genero = elegir_genero()
            biblioteca.agregar_libro(titulo, autor, anio, genero)
            print("Libro agregado exitosamente.")
        elif opcion == '2':
            biblioteca.listar_libros()

        elif opcion == '3':
            try:
                id_libro = int(input("Ingrese el ID del libro a actualizar: "))
                nuevo_titulo = input("Nuevo titulo: ")
                nuevo_autor = input("Nuevo autor: ")
                nuevo_anio = input("Nuevo año: ")
                nuevo_genero = elegir_genero()
                if biblioteca.actualizar_libro(
                    id_libro, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero):
                    print("libro actulizado exitosamente.")

                else:
                    print("no se encontro con ese ID. Intentelo nuevamente")
                except ValueError:
                    print("Por favor, ingrese un numero valido.")
        
        elif opcion == '4':
            try:
                id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                if biblioteca.eliminar_libro(id_libro):
                    print("Libro eliminado exitosamente.")
                else:
                    print("no se encontro un libro con ese ID.")
            except ValueError:
                print("Por favor, ingrese un numero valido.")
        
        elif opcion == '5':
            print("Saliendo del programa. Hasta pronto.")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
    


        
        


    
