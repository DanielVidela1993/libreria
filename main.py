from libreria import Biblioteca

GENEROS = [
    "Ficción", "Ciencia Ficción", "Fantasía", "Misterio",
    "Romance", "Thriller", "Horror", "Histórica",
    "Aventura", "Drama", "Doc. Cientifico", "comics", "Anime", "Otros"
]

def mostrar_menu():
    print("\n--- Menú de Biblioteca ---")
    print("1. Agregar Libro")
    print("2. Listar Libros")
    print("3. Actualizar Libro")
    print("4. Eliminar Libro")
    print("5. Salir")

def elegir_genero(actual=None):
    print("\nSeleccione un Género:")
    for i, genero in enumerate(GENEROS, 1):
        print(f"{i}. {genero}")
    print("Presione Enter para mantener el género actual." if actual else "")
    
    while True:
        opcion = input("Ingrese el número del género: ")
        if opcion == "" and actual is not None:
            return actual
        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(GENEROS):
                return GENEROS[opcion - 1]
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def main():
    biblioteca = Biblioteca('dato.json')

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")
            anio = input("Ingrese el año: ")
            genero = elegir_genero()
            biblioteca.agregar_libro(titulo, autor, anio, genero)
            print(" Libro agregado exitosamente.")

        elif opcion == '2':
            biblioteca.listar_libros()

        elif opcion == '3':
            try:
                id_libro = int(input("Ingrese el ID del libro a actualizar: "))
                libro_a_actualizar = next((l for l in biblioteca.libros if l.id == id_libro), None)
                if libro_a_actualizar:
                    nuevo_titulo = input("Nuevo título (Enter para mantener): ") or libro_a_actualizar.titulo
                    nuevo_autor = input("Nuevo autor (Enter para mantener): ") or libro_a_actualizar.autor
                    nuevo_anio = input("Nuevo año (Enter para mantener): ") or libro_a_actualizar.anio
                    nuevo_genero = elegir_genero(actual=libro_a_actualizar.genero)
                    
                    if biblioteca.actualizar_libro(id_libro, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero):
                        print(" Libro actualizado exitosamente.")
                    else:
                        print(" Error al actualizar el libro.")
                else:
                    print(" No se encontró un libro con ese ID.")
            except ValueError:
                print(" Error: Ingrese un número válido.")

        elif opcion == '4':
            try:
                id_libro = int(input("Ingrese el ID del libro a eliminar: "))
                if biblioteca.eliminar_libro(id_libro):
                    print(" Libro eliminado exitosamente.")
                else:
                    print(" No se encontró un libro con ese ID.")
            except ValueError:
                print(" Error: Ingrese un número válido.")

        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
