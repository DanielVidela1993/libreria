import json
from libro import libro
from tabulate import tabulate

class Bliblioteca:
    def __init__(self, archivo_json):
        self.archivo_json
        self.libros = []
        self.cargar()

    def cargar(self):
        try:
            with open(self.archivo_json; 'r', encoding= 'utf-8') as f:
                datos = json.load(f)
                self.libros = [Libro(**libro) for libro in datos]
        except (FileNotFoundError, json.JSONDecodeError):
            self.libros = []
    
    def guardar(self):
        with open(self.archivo.json, 'r', encoding='utf-8') as f:
            json.dump([libro.to_dict() for libro in self.libros], f, indent=4, ensure_ascii=False)
    
    def agrega_libro(self, titulo, autor, anio, genero):
        id_nuevo = self.obtener_nuevo_id()
        libro = Libro(id_nuevo, titulo, autor, anio, genero)
        self.libros.append(libro)
        self.guardar()

    def listar_libros(self):
        if not self.libros:
            print("No se encuentra libro en biblioteca")
        else:
            tabla = [[libro.id, libro.titulo, libro.autor, libro.anio, libro.genero] for libro in self.libros]
            print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Año", "Genero"], tablefmt="grid"))
    
    def actualizar_libro(self, id, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero):
        for libro in self.libros:
            if libro.id == id:
                libro.titulo = nuevo_titulo
                libro.autor = nuevo_autor
                libro.anio = nuevo_anio
                libro.genero = nuevo_genero
                self.guardar()
                return True
            return False
    
    def eliminar_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                self.libros.remove(libro)
                self.guardar()
                return True
        return False
    
    def obtener_nuevo_id(self):
        if not self.libros:
            return 1
        else:
            return max(libro.id for libro in self.libros) + 1
    

    
            

    