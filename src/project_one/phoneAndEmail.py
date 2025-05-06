"""Projeto: extrator de números de telefone e endereços de email."""

from functions import regexEmail
import pyperclip
import re

telRegex = re.compile(
    r"""
    (?:\d{2}|\(\d{2}\))?
    (?:\s|-|\.)?9?(?:\s|-|\.)?
    (?:\d{4,5})(\s|-|\.)?
    (?:\d{4})
""",
    re.VERBOSE,
)

textTransferArea = str(pyperclip.paste())

result = regexEmail(textTransferArea)

matches = telRegex.finditer(textTransferArea)
for match in matches:
    print(match.group(0))
