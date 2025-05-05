"""Encontrar URLs de sites que comecem com http:// ou com https://."""

import re
import pyperclip

urlRegex = re.compile(
    r"""
    http                                    # como com http
    s?                                      # o s é opcional
    ://                                     # separador obrigatório
    (?:[a-zA-Z0-9\-._~%!$&'()*+,;=:@]+@)?   # user:senha@
    (?:[a-zA-Z0-9.-]+                       # captura o host ou dominio ip
    |                                       # ou
    \d{1,3}(?:\.\d{1,3}){3})                # 127.0.0.1
    (?::\d+)?                               # porta opcional
    (?:/[^\s]*)?                            # dps da porta, opcional
""",
    re.VERBOSE,
)

msg = pyperclip.paste()

matches = []
for url in urlRegex.findall(msg):
    matches.append(url)


if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("URLs encontradas")
    print("\n".join(matches))
else:
    print("Não foi encontrado nenhum resultado!.")
