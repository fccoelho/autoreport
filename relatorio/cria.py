
import os

class Relatorio:
    template_dir = "dados"#os.path.join("..", "dados")
    def __init__(self, titulo, autor, template='cabeçalho.tex') -> None:
        self.template = template
        self.cabeçalho=None
        self.titulo = titulo
        self.autor = autor
        self.inicializa()

    def inicializa(self):
        with open(os.path.join(self.template_dir,'cabeçalho.tex')) as f:
            self.cabeçalho = f.read()

