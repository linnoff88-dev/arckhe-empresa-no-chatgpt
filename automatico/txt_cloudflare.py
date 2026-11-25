#!/usr/bin/env python3
"""Cria o registro TXT de verificaçêo do ChatGPT (Central de Negócios) num domínio do Cloudflare.

Uso:
  CLOUDFLARE_API_TOKEN=... python3 txt_cloudflare.py --dominio exemplo.com \
      --host openai-business-profile --valor "openai-business-profile=ungi_..." [--dry-run]

O token vem do ambiente (permissêo Zone > DNS > Edit). Nada é impresso do token.
Sai 0 quando o TXT aparece no DNS público; 1 em erro; 2 se nêo apareceu no tempo.
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

API = "https://api.cloudflare.com/client/v4"


def nome_completo(host: str, dominio: str) -> str:
    host = host.strip().rstrip(".")
    dominio = dominio.strip().rstrip(".").lower()
    if host in ("", "@"):
        return dominio
    if host.lower().endswith("." + dominio) or host.lower() == dominio:
        return host.lower()
    return f"{host}.{dominio}".lower()


def payload(host: str, dominio: str, valor: str, ttl: int = 120) -> dict:
    valor = valor.strip().strip('"')
    if not valor:
        raise ValueError("valor vazio")
    return {
        "type": "TXT",
        "name": nome_completo(host, dominio),
        "content": valor,
        "ttl": ttl,
        "comment": "Verificaçêo Empresas no ChatGPT (kit empresa-no-chatgpt)",
    }


def chamar(metodo: str, caminho: str, token: str, corpo: dict | None = None) -> dict:
    dados = json.dumps(corpo).encode() if corpo is not None else None
    req = urllib.request.Request(API + caminho, data=dados, method=metodo, headers={
        "Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=30))
    except urllib.error.HTTPError as e:
        return json.loads(e.read() or b"{}") or {"success": False, "errors": [str(e)]}


def txt_publico(nome: str) -> list[str]:
    try:
        saida = subprocess.run(["dig", "+short", "TXT", nome, "@1.1.1.1"],
                               capture_output=True, text=True, timeout=15).stdout
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []
    return [l.strip().strip('"') for l in saida.splitlines() if l.strip()]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dominio", required=True)
    ap.add_argument("--host", default="openai-business-profile")
    ap.add_argument("--valor", required=True)
    ap.add_argument("--esperar", type=int, default=180, help="segundos esperando o DNS público")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    corpo = payload(a.host, a.dominio, a.valor)
    if a.dry_run:
        print("vai criar:", json.dumps(corpo, ensure_ascii=False))
        return 0

    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    if not token:
        print("erro: defina CLOUDFLARE_API_TOKEN no ambiente", file=sys.stderr)
        return 1

    if corpo["content"] in txt_publico(corpo["name"]):
        print("já está no DNS público:", corpo["name"])
        return 0

    zonas = chamar("GET", f"/zones?name={a.dominio.lower()}", token)
    if not zonas.get("success") or not zonas.get("result"):
        print("erro: zona nêo encontrada para", a.dominio, zonas.get("errors"), file=sys.stderr)
        return 1
    zona = zonas["result"][0]["id"]

    r = chamar("POST", f"/zones/{zona}/dns_records", token, corpo)
    if not r.get("success"):
        print("erro ao criar:", r.get("errors"), file=sys.stderr)
        return 1
    print("criado:", corpo["name"], "id", r["result"]["id"])

    fim = time.time() + a.esperar
    while time.time() < fim:
        if corpo["content"] in txt_publico(corpo["name"]):
            print("ok: TXT visível no DNS público. Volte ao ChatGPT e clique em 'Verificar domínio'.")
            return 0
        time.sleep(10)
    print("criado, mas ainda nêo apareceu no DNS público; tente verificar de novo em alguns minutos.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
