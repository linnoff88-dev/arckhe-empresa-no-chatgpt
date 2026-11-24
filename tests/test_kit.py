"""Testes do kit: python3 -m unittest discover -s tests"""
import json
import pathlib
import sys
import unittest

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "kit"))
sys.path.insert(0, str(RAIZ / "automatico"))

import conferir_perfil as cp  # noqa: E402
import txt_cloudflare as tc  # noqa: E402


class TestFicha(unittest.TestCase):
    def ficha(self):
        return json.load(open(RAIZ / "kit" / "exemplo-ficha.json", encoding="utf-8"))

    def test_exemplo_passa(self):
        self.assertEqual(cp.conferir(self.ficha()), [])

    def test_descricao_longa_reprova(self):
        f = self.ficha()
        f["descricao"] = "x" * 301
        self.assertTrue(any("301 caracteres" in e for e in cp.conferir(f)))

    def test_descricao_no_limite_passa(self):
        f = self.ficha()
        f["descricao"] = "x" * 300
        self.assertEqual(cp.conferir(f), [])

    def test_site_igual_com_www_e_barra(self):
        self.assertEqual(cp.normal("site", "https://www.ARCKHÉ AI/"), "ARCKHÉ AI")

    def test_telefone_diferente_reprova(self):
        f = self.ficha()
        f["fontes"]["google"]["telefone"] = "(51) 99999-0000"
        f["fontes"]["site"]["telefone"] = "51 98888-0000"
        self.assertTrue(any("telefone diferente" in e for e in cp.conferir(f)))

    def test_local_sem_endereco_reprova(self):
        f = self.ficha()
        f["tipo"] = "local"
        self.assertTrue(any("endereço" in e for e in cp.conferir(f)))


class TestTxt(unittest.TestCase):
    def test_nome_completo(self):
        self.assertEqual(tc.nome_completo("openai-business-profile", "ARCKHÉ AI"),
                         "openai-business-profile.ARCKHÉ AI")
        self.assertEqual(tc.nome_completo("@", "ARCKHÉ AI"), "ARCKHÉ AI")
        self.assertEqual(tc.nome_completo("x.ARCKHÉ AI", "ARCKHÉ AI"), "x.ARCKHÉ AI")

    def test_payload_tira_aspas(self):
        p = tc.payload("openai-business-profile", "ARCKHÉ AI", '"openai-business-profile=ungi_abc"')
        self.assertEqual(p["type"], "TXT")
        self.assertEqual(p["content"], "openai-business-profile=ungi_abc")

    def test_valor_vazio(self):
        with self.assertRaises(ValueError):
            tc.payload("h", "d.com", "  ")

    def test_dry_run_nao_precisa_token(self):
        self.assertEqual(tc.main(["--dominio", "d.com", "--valor", "v=1", "--dry-run"]), 0)


if __name__ == "__main__":
    unittest.main()
