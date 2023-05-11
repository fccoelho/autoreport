import unittest
from relatorio.cria import Relatorio

class TestCria(unittest.TestCase):
    def test_cria_relatorio(self):
        R = Relatorio('Meu relatório', 'Eu mesmo')
        self.assertEqual(R.titulo, 'Meu relatório')

    def test_render(self):
        R = Relatorio('Meu relatório', 'Eu mesmo')
        tex = R._render()
        self.assertIn(r'\author{ Eu mesmo }', tex)
        self.assertIn(r'\title{ Meu relatório }', tex)

    def test_add_section(self):
        R = Relatorio('Meu relatório', 'Eu mesmo')
        R.add_section({"título":"Primeira seção", "conteúdo": "conteúdo da primeira seção"})
        tex = R._render()
        self.assertIn("Primeira seção}", tex)