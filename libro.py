class libro
def __init__(self, id, titulo, autor, año)

self.id = id 
self.titulo = titulo
self.autor = autor
self.año = año
self.genero = genero

def to_dict(self):
    return {
        "id": self.id,
        "titulo": self.titulo,
        "autor" : self.autor
        "año" : self.año
        }
