"""Projeto: extrator de números de telefone e endereços de email."""

import re

telRegex = re.compile(
    r"""
    (\d{2}|\(\d{2}\))?  # área
    (\s|-|\.)?          # separador
    9?                  # separador dígito 9
    (\s|-|\.)?          # separador
    \d{4,5}             # primeira parte
    (\s|-|\.)?          # separador
    \d{4}               # segunda parte
""",
    re.VERBOSE,
)

emailRegex = re.compile(
    r"""
    [a-zA-Z0-9._%+-]+   # nome de usuário
    @                   # simbolo @
    [a-zA-Z0-9.-]+      # nome de domínio
    \.[a-zA-Z]{2,4}     # ponto seguido de outros caracteres
""",
    re.VERBOSE,
)
