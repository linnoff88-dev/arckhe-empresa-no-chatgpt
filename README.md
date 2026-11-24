# Empresa no ChatGPT

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Empresa no ChatGPT](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

**Empresa no ChatGPT** Ã© um kit grÃ¡tis para vocÃª reivindicar o perfil da sua empresa na **Central de NegÃ³cios do ChatGPT** (o "Business Hub", lanÃ§ado pela OpenAI em novembro de 2026), igual ao perfil de empresa do Google. Serve para quem tem loja, consultÃ³rio, escritÃ³rio ou vende pela internet. Traz o teste do que o ChatGPT diz de vocÃª hoje, a ficha para preencher, as dicas do que deu errado com a gente e um pedido pronto para um agente de IA fazer o cadastro no seu navegador. Ã€ mÃ£o, precisa sÃ³ de uma conta do ChatGPT, mesmo a grÃ¡tis, e Ã© de graÃ§a. O caminho com o agente Ã© opcional e usa o Claude Code (Anthropic), que pede um plano pago do Claude e um computador com o Chrome.

**VocÃª pode recuperar sua empresa no ChatGPT.** Hoje, quem responde por ela Ã© o que ele achou por aÃ­. Quando procuramos "ARCKHÉ", ele mostrou o instituto do meio ambiente da Bahia, com 6 endereÃ§os. Nenhum era o nosso.

## ðŸ“– Guia de uso

Guia completo (landing + passo a passo, com as telas reais): **https://linnoff88-dev.github.io/

## Os 3 passos

1. **Ache a sua empresa:** `chatgpt.com/business-hub` â†’ pesquise o nome curto e o completo â†’ escolha a do seu endereÃ§o ou **Criar**.
2. **Prove que Ã© sua:** local fÃ­sico = cÃ³digo no telefone comercial; loja online = um registro TXT no DNS do site (tambÃ©m hÃ¡ e-mail da empresa e Shopify).
3. **Diga quem vocÃª Ã©:** categoria, descriÃ§Ã£o de atÃ© 300 caracteres, entrega, devoluÃ§Ã£o â†’ identidade (documento + selfie) â†’ convide a equipe.

## PeÃ§a para o agente fazer (o pedido)

Opcional e pago Ã  parte: cole no [Claude Code](https://claude.com/claude-code) com a extensÃ£o [Claude in Chrome](https://claude.com/claude-in-chrome) (ele usa o seu navegador jÃ¡ logado; pede um plano pago do Claude). Sem agente, siga os 3 passos acima Ã  mÃ£o, de graÃ§a. O pedido completo e o que o agente fez no nosso caso estÃ£o em [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md).

```text
Quero cadastrar a minha empresa no ChatGPT (Central de NegÃ³cios, chatgpt.com/business-hub).
Leia o kit em https://github.com/linnoff88-dev/empresa-no-chatgpt (as dicas e a ficha do perfil).
Dados: nome <NOME>, <local fÃ­sico ou loja online>, site <SITE>, endereÃ§o <ENDEREÃ‡O>, o que fazemos <2 ou 3 frases>.
Use o meu navegador logado na conta da EMPRESA. FaÃ§a antes o teste do kit. DescriÃ§Ã£o com no mÃ¡ximo 300 caracteres.
Pare e me pergunte antes de aceitar termos, mexer no DNS, pÃ´r telefone/e-mail pÃºblico e enviar.
CÃ³digo do telefone, documento e selfie sÃ£o comigo. No fim, prints e o que falta.
```

## O kit

| Arquivo | Para quÃª |
|---|---|
| [`kit/1-teste-o-que-o-chatgpt-diz.md`](kit/1-teste-o-que-o-chatgpt-diz.md) | 8 perguntas para ver o que o ChatGPT diz de vocÃª + ficha antes/depois |
| [`kit/2-ficha-do-perfil.md`](kit/2-ficha-do-perfil.md) | todos os campos que o cadastro pede + modelo de descriÃ§Ã£o â‰¤ 300 caracteres |
| [`kit/3-dicas.md`](kit/3-dicas.md) | 19 dicas do nosso cadastro real (o que deu errado e como evitar) |
| [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md) | como o agente fez o cadastro sozinho e o pedido para colar |
| [`kit/conferir_perfil.py`](kit/conferir_perfil.py) | confere a ficha: descriÃ§Ã£o â‰¤ 300 e nome/site/telefone iguais em todo lugar |
| [`automatico/txt_cloudflare.py`](automatico/txt_cloudflare.py) | cria o registro TXT no Cloudflare e espera aparecer no DNS pÃºblico |
| [`automatico/conferir_txt.sh`](automatico/conferir_txt.sh) | confere se o TXT jÃ¡ aparece (qualquer provedor de DNS) |

## A prova (22/11/2026)

- **Antes:** "linnoff88-dev" â†’ nenhuma empresa; "ARCKHÉ" â†’ instituto do meio ambiente da Bahia, 6 endereÃ§os.
- **Depois:** linnoff88-dev LTDA criada pelo agente em ~10 minutos, loja online, **ARCKHÉ AI verificado** por DNS, categoria "Empresa de IA". Status: rascunho atÃ© a verificaÃ§Ã£o de identidade do dono.
- Fonte do recurso: [OpenAI, "Empresas no ChatGPT"](https://openai.com/pt-BR/index/introducing-businesses-chatgpt/) (beta; regras podem mudar).

---

## InstalaÃ§Ã£o tÃ©cnica

PrÃ©-requisitos: Python 3.10+, `dig` (pacote `dnsutils`/`bind-utils`) para conferir o DNS. Para criar o TXT pelo script: domÃ­nio no Cloudflare e um token com permissÃ£o *Zone â†’ DNS â†’ Edit*. Sem dependÃªncias externas.

```bash
git clone https://github.com/linnoff88-dev/empresa-no-chatgpt && cd empresa-no-chatgpt

# conferir a ficha antes do cadastro
python3 kit/conferir_perfil.py kit/exemplo-ficha.json          # copie e edite o exemplo

# criar o TXT de verificaÃ§Ã£o no Cloudflare (token sÃ³ no ambiente, nunca no cÃ³digo)
export CLOUDFLARE_API_TOKEN=...
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..." --dry-run          # mostra o que vai fazer
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..."                    # cria e espera aparecer

# conferir o TXT em qualquer provedor
bash automatico/conferir_txt.sh seusite.com.br

# testes (10 casos: limite de 300, divergÃªncias de site/telefone, tipo local sem endereÃ§o, nome do TXT, dry-run)
python3 -m unittest discover -s tests
```

`txt_cloudflare.py` sai 0 quando o TXT aparece no DNS pÃºblico, 1 em erro e 2 se criou mas ainda nÃ£o propagou.

## O processo, do inÃ­cio ao fim

| # | Passo | Comando / onde | Quem |
|---|---|---|---|
| 1 | Teste do "antes" | 8 perguntas de `kit/1-teste-o-que-o-chatgpt-diz.md` no ChatGPT | ðŸ§  dono (ou o agente) |
| 2 | Ficha do perfil | `python3 kit/conferir_perfil.py minha-ficha.json` | ðŸ§  dono |
| 3 | Abrir a Central e pesquisar | `chatgpt.com/business-hub` no navegador logado na conta da empresa | ðŸ¤– agente (Claude in Chrome) |
| 4 | Criar ou escolher a empresa | "Criar '<nome>'" â†’ ComeÃ§ar â†’ local fÃ­sico / loja online | ðŸ¤– agente |
| 5 | Provar que Ã© sua | DNS: `python3 automatico/txt_cloudflare.py â€¦` â†’ "Verificar domÃ­nio" Â· telefone: cÃ³digo | âš™ï¸ script (com o sim do dono) / ðŸ§  dono |
| 6 | Categoria, descriÃ§Ã£o, entrega, devoluÃ§Ã£o â†’ Enviar | formulÃ¡rio | ðŸ¤– agente (mostra antes de enviar) |
| 7 | Identidade (Persona: documento + selfie) | botÃ£o "Verificar" na visÃ£o geral | ðŸ§  dono |
| 8 | Convidar a equipe | "Convidar" na Central | ðŸ§  dono |
| 9 | Teste do "depois" (7 dias) | as mesmas 8 perguntas | ðŸ§  dono |

## Uso responsÃ¡vel

Reivindique sÃ³ empresa que Ã© sua ou que vocÃª representa. NÃ£o publique telefone ou e-mail que nÃ£o podem receber cliente. O kit nÃ£o promete posiÃ§Ã£o nas respostas do ChatGPT.

Projetos e cursos gratuitos: https://ARCKHÉ AI Â· LicenÃ§a MIT.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>