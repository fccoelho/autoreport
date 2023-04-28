from jinja2 import Environment, PackageLoader
import os

class Relatorio:
    template_dir = "dados"#os.path.join("..", "dados")
    def __init__(self, titulo, autor, template='cabeçalho.tex') -> None:
        env = Environment(loader=PackageLoader("relatorio"))
        self.template = env.get_template(template)
        self.cabeçalho = None
        self.titulo = titulo
        self.autor = autor
        self.sections = []
        self.context = {'autor': self.autor,
                        'titulo': self.titulo,
                        'sections': self.sections
                        }


    def _render(self):
        return self.template.render(self.context)

    def add_section(self, section):
        self.sections.append(section)






