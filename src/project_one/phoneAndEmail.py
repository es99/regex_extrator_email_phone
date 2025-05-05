"""Projeto: extrator de números de telefone e endereços de email."""

import pyperclip
import re

telRegex = re.compile(
    r"""
    (\d{2}|\(\d{2}\))?  # área
    (\s|-|\.)?          # separador
    (9?                  # separador dígito 9
    (\s|-|\.)?          # separador
    \d{4,5}             # primeira parte
    (\s|-|\.)?          # separador
    \d{4})               # segunda parte
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

textTransferArea = str(pyperclip.paste())

matches = []
for groups in telRegex.findall(textTransferArea):
    phoneNum = "".join([groups[0], groups[2]])
    matches.append(phoneNum)
for email in emailRegex.findall(textTransferArea):
    matches.append(email)

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to Clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email address found.")
