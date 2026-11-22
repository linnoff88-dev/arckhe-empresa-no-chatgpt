#!/usr/bin/env python3
"""Confere a ficha do perfil antes do cadastro no ChatGPT.

- descrição com no máximo 300 caracteres (o formulário corta sem avisar);
- nome, site e telefone iguais em todas as fontes (google, site, chatgpt...);
- campos obrigatórios para o tipo de atendimento.

Uso: python3 kit/conferir_perfil.py kit/exemplo-ficha.json
Sai 0 se está tudo certo, 1 se achou problema.
"""
import json
import re
import sys

LIMITE = 300


def normal(campo: str, v: str) -> str:
    v = (v or "").strip().lower()
    if campo == "telefone":
        return re.sub(r"\D", "", v)
    if campo == "site":
        v = re.sub(r"^https?://", "", v)
        v = re.sub(r"^www\.", "", v)
        return v.rstrip("/")
    return re.sub(r"\s+", " ", v)


def conferir(ficha: dict) -> list[str]:
    erros = []
    desc = ficha.get("descricao", "")
    if len(desc) > LIMITE:
        erros.append(f"descrição com {len(desc)} caracteres (máximo {LIMITE}); o ChatGPT corta em: "
                     f"...{desc[LIMITE-20:LIMITE]!r}")
    tipo = ficha.get("tipo")
    if tipo not in ("local", "online"):
        erros.append("tipo deve ser 'local' (local físico) ou 'online' (loja online)")
    if tipo == "online" and not ficha.get("site"):
        erros.append("loja online precisa de site")
    if tipo == "local" and not ficha.get("endereco"):
        erros.append("local físico precisa de endereço")
    for campo in ("nome", "site", "telefone"):
        valores = {fonte: dados.get(campo) for fonte, dados in ficha.get("fontes", {}).items()
                   if dados.get(campo)}
        if ficha.get(campo):
            valores["ficha"] = ficha[campo]
        distintos = {normal(campo, v) for v in valores.values()}
        if len(distintos) > 1:
            lista = ", ".join(f"{f}={v}" for f, v in valores.items())
            erros.append(f"{campo} diferente entre as fontes: {lista}")
    return erros


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print(__doc__)
        return 1
    ficha = json.load(open(argv[0], encoding="utf-8"))
    erros = conferir(ficha)
    print(f"descrição: {len(ficha.get('descricao', ''))}/{LIMITE} caracteres")
    for e in erros:
        print("✗", e)
    if not erros:
        print("✓ ficha pronta para o cadastro")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
