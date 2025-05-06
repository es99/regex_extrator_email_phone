"""Funções e variáveis regex."""

import re

emailRegex = re.compile(
    r"""
    [a-zA-Z0-9._%+-]+   # nome de usuário
    @                   # simbolo @
    [a-zA-Z0-9.-]+      # nome de domínio
    \.[a-zA-Z]{2,4}     # ponto seguido de outros caracteres
""",
    re.VERBOSE,
)

telRegex = re.compile(
    r"""
    (?:\d{2}|\(\d{2}\))?
    (?:\s|-|\.)?9?(?:\s|-|\.)?
    (?:\d{4,5})(\s|-|\.)?
    (?:\d{4})
""",
    re.VERBOSE,
)


def regexEmail(text, regex=emailRegex):
    """Recebe um texto e um objeto regex e retorna os objetos \
    correspondentes de forma tratata com quebras de linha."""
    matches = regex.findall(text)
    return "\n".join(matches) if matches else None


def regexPhone(text, regex=telRegex):
    """Recebe um texto e um objeto regex e retorna uma lista \
    das correspondências."""
    telsFound = []
    matches = regex.finditer(text)
    for match in matches:
        telsFound.append(match.group(0).strip())
    return telsFound if matches else None
