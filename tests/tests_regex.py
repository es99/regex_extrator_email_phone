"""Testes unitários das funcões regex localizadas no arquivo 'functions.py'."""

import unittest
from src.project_one.functions import regexEmail, regexPhone, regexData


class TestRegexs(unittest.TestCase):
    """Testa as funcoes que recebem as expressoes regulares."""

    def test_regex_email(self):
        """Teste unitario da funcao que recebe a regex de padroes de email."""
        text = "engels@uol.com.br, engels.franca@gmail.com"
        matches = regexEmail(text)
        resultado = "engels@uol.com.br\nengels.franca@gmail.com"
        self.assertEqual(matches, resultado)

    def test_regex_tel(self):
        """Teste unitario da funcao que recebe a \
        regex de padroes de telefones."""
        text = "(11)982013135, 3226-4992, 8398201-3135"
        matches = regexPhone(text)
        resultado = ["(11)982013135", "3226-4992", "8398201-3135"]
        self.assertEqual(matches, resultado)

    def test_regex_data(self):
        """Teste unitario da funcado que recebe a\
        regex de padroes de datas."""
        text = "08.Mai.2025, 8 Maio 2025, 08/05/2025, 08052025"
        listaRetornada = regexData(text)
        resultadoEsperado = "08-Mai-2025, 8-Maio-2025, 08-05-2025, 08-05-2025"
        self.assertEqual(listaRetornada, resultadoEsperado)
