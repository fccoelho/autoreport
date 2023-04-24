


class Relatorio:
    def __init__(self, titulo, autor) -> None:
        self.cabeçalho=None
        self.titulo = titulo
        self.autor = autor
        self.inicializa()

    def inicializa(self):
        with open('..dados/cabeçalho.tex') as f:
            self.cabeçalho = f.read()

