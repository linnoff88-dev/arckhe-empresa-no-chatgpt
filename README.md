# Empresa no ChatGPT

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Empresa no ChatGPT](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

**Empresa no ChatGPT** êÂ© um kit grêÂ¡tis para vocêÂª reivindicar o perfil da sua empresa na **Central de NegêÂ³cios do ChatGPT** (o "Business Hub", lanêÂ§ado pela OpenAI em novembro de 2026), igual ao perfil de empresa do Google. Serve para quem tem loja, consultêÂ³rio, escritêÂ³rio ou vende pela internet. Traz o teste do que o ChatGPT diz de vocêÂª hoje, a ficha para preencher, as dicas do que deu errado com a gente e um pedido pronto para um agente de IA fazer o cadastro no seu navegador. êâ¬ mêÂ£o, precisa sêÂ³ de uma conta do ChatGPT, mesmo a grêÂ¡tis, e êÂ© de graêÂ§a. O caminho com o agente êÂ© opcional e usa o Claude Code (Anthropic), que pede um plano pago do Claude e um computador com o Chrome.

**VocêÂª pode recuperar sua empresa no ChatGPT.** Hoje, quem responde por ela êÂ© o que ele achou por aêÂ­. Quando procuramos "ARCKHê", ele mostrou o instituto do meio ambiente da Bahia, com 6 endereêÂ§os. Nenhum era o nosso.

## ê°Å¸ââ Guia de uso

Guia completo (landing + passo a passo, com as telas reais): **https://linnoff88-dev.github.io/

## Os 3 passos

1. **Ache a sua empresa:** `chatgpt.com/business-hub` ê¢â â pesquise o nome curto e o completo ê¢â â escolha a do seu endereêÂ§o ou **Criar**.
2. **Prove que êÂ© sua:** local fêÂ­sico = cêÂ³digo no telefone comercial; loja online = um registro TXT no DNS do site (tambêÂ©m hêÂ¡ e-mail da empresa e Shopify).
3. **Diga quem vocêÂª êÂ©:** categoria, descriêÂ§êÂ£o de atêÂ© 300 caracteres, entrega, devoluêÂ§êÂ£o ê¢â â identidade (documento + selfie) ê¢â â convide a equipe.

## PeêÂ§a para o agente fazer (o pedido)

Opcional e pago êÂ  parte: cole no [Claude Code](https://claude.com/claude-code) com a extensêÂ£o [Claude in Chrome](https://claude.com/claude-in-chrome) (ele usa o seu navegador jêÂ¡ logado; pede um plano pago do Claude). Sem agente, siga os 3 passos acima êÂ  mêÂ£o, de graêÂ§a. O pedido completo e o que o agente fez no nosso caso estêÂ£o em [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md).

```text
Quero cadastrar a minha empresa no ChatGPT (Central de NegêÂ³cios, chatgpt.com/business-hub).
Leia o kit em https://github.com/linnoff88-dev/empresa-no-chatgpt (as dicas e a ficha do perfil).
Dados: nome <NOME>, <local fêÂ­sico ou loja online>, site <SITE>, endereêÂ§o <ENDEREêâ¡O>, o que fazemos <2 ou 3 frases>.
Use o meu navegador logado na conta da EMPRESA. FaêÂ§a antes o teste do kit. DescriêÂ§êÂ£o com no mêÂ¡ximo 300 caracteres.
Pare e me pergunte antes de aceitar termos, mexer no DNS, pêÂ´r telefone/e-mail pêÂºblico e enviar.
CêÂ³digo do telefone, documento e selfie sêÂ£o comigo. No fim, prints e o que falta.
```

## O kit

| Arquivo | Para quêÂª |
|---|---|
| [`kit/1-teste-o-que-o-chatgpt-diz.md`](kit/1-teste-o-que-o-chatgpt-diz.md) | 8 perguntas para ver o que o ChatGPT diz de vocêÂª + ficha antes/depois |
| [`kit/2-ficha-do-perfil.md`](kit/2-ficha-do-perfil.md) | todos os campos que o cadastro pede + modelo de descriêÂ§êÂ£o ê¢â°Â¤ 300 caracteres |
| [`kit/3-dicas.md`](kit/3-dicas.md) | 19 dicas do nosso cadastro real (o que deu errado e como evitar) |
| [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md) | como o agente fez o cadastro sozinho e o pedido para colar |
| [`kit/conferir_perfil.py`](kit/conferir_perfil.py) | confere a ficha: descriêÂ§êÂ£o ê¢â°Â¤ 300 e nome/site/telefone iguais em todo lugar |
| [`automatico/txt_cloudflare.py`](automatico/txt_cloudflare.py) | cria o registro TXT no Cloudflare e espera aparecer no DNS pêÂºblico |
| [`automatico/conferir_txt.sh`](automatico/conferir_txt.sh) | confere se o TXT jêÂ¡ aparece (qualquer provedor de DNS) |

## A prova (22/11/2026)

- **Antes:** "linnoff88-dev" ê¢â â nenhuma empresa; "ARCKHê" ê¢â â instituto do meio ambiente da Bahia, 6 endereêÂ§os.
- **Depois:** linnoff88-dev LTDA criada pelo agente em ~10 minutos, loja online, **ARCKHê AI verificado** por DNS, categoria "Empresa de IA". Status: rascunho atêÂ© a verificaêÂ§êÂ£o de identidade do dono.
- Fonte do recurso: [OpenAI, "Empresas no ChatGPT"](https://openai.com/pt-BR/index/introducing-businesses-chatgpt/) (beta; regras podem mudar).

---

## InstalaêÂ§êÂ£o têÂ©cnica

PrêÂ©-requisitos: Python 3.10+, `dig` (pacote `dnsutils`/`bind-utils`) para conferir o DNS. Para criar o TXT pelo script: domêÂ­nio no Cloudflare e um token com permissêÂ£o *Zone ê¢â â DNS ê¢â â Edit*. Sem dependêÂªncias externas.

```bash
git clone https://github.com/linnoff88-dev/empresa-no-chatgpt && cd empresa-no-chatgpt

# conferir a ficha antes do cadastro
python3 kit/conferir_perfil.py kit/exemplo-ficha.json          # copie e edite o exemplo

# criar o TXT de verificaêÂ§êÂ£o no Cloudflare (token sêÂ³ no ambiente, nunca no cêÂ³digo)
export CLOUDFLARE_API_TOKEN=...
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..." --dry-run          # mostra o que vai fazer
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..."                    # cria e espera aparecer

# conferir o TXT em qualquer provedor
bash automatico/conferir_txt.sh seusite.com.br

# testes (10 casos: limite de 300, divergêÂªncias de site/telefone, tipo local sem endereêÂ§o, nome do TXT, dry-run)
python3 -m unittest discover -s tests
```

`txt_cloudflare.py` sai 0 quando o TXT aparece no DNS pêÂºblico, 1 em erro e 2 se criou mas ainda nêÂ£o propagou.

## O processo, do inêÂ­cio ao fim

| # | Passo | Comando / onde | Quem |
|---|---|---|---|
| 1 | Teste do "antes" | 8 perguntas de `kit/1-teste-o-que-o-chatgpt-diz.md` no ChatGPT | ê°Å¸Â§Â  dono (ou o agente) |
| 2 | Ficha do perfil | `python3 kit/conferir_perfil.py minha-ficha.json` | ê°Å¸Â§Â  dono |
| 3 | Abrir a Central e pesquisar | `chatgpt.com/business-hub` no navegador logado na conta da empresa | ê°Å¸Â¤â agente (Claude in Chrome) |
| 4 | Criar ou escolher a empresa | "Criar '<nome>'" ê¢â â ComeêÂ§ar ê¢â â local fêÂ­sico / loja online | ê°Å¸Â¤â agente |
| 5 | Provar que êÂ© sua | DNS: `python3 automatico/txt_cloudflare.py ê¢â¬Â¦` ê¢â â "Verificar domêÂ­nio" êÂ· telefone: cêÂ³digo | ê¢Å¡â¢ê¯Â¸Â script (com o sim do dono) / ê°Å¸Â§Â  dono |
| 6 | Categoria, descriêÂ§êÂ£o, entrega, devoluêÂ§êÂ£o ê¢â â Enviar | formulêÂ¡rio | ê°Å¸Â¤â agente (mostra antes de enviar) |
| 7 | Identidade (Persona: documento + selfie) | botêÂ£o "Verificar" na visêÂ£o geral | ê°Å¸Â§Â  dono |
| 8 | Convidar a equipe | "Convidar" na Central | ê°Å¸Â§Â  dono |
| 9 | Teste do "depois" (7 dias) | as mesmas 8 perguntas | ê°Å¸Â§Â  dono |

## Uso responsêÂ¡vel

Reivindique sêÂ³ empresa que êÂ© sua ou que vocêÂª representa. NêÂ£o publique telefone ou e-mail que nêÂ£o podem receber cliente. O kit nêÂ£o promete posiêÂ§êÂ£o nas respostas do ChatGPT.

Projetos e cursos gratuitos: https://ARCKHê AI êÂ· LicenêÂ§a MIT.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>