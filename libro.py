class Libro:
    def __init__(self, id, titulo, autor, anio, genero):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "genero": self.genero
        }
