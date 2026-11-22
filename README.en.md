# Business on ChatGPT

[![Business on ChatGPT](guia/assets/banner-en.jpg)](https://inematds.github.io/empresa-no-chatgpt/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

**Business on ChatGPT** is a free kit to help you claim your company profile in the **ChatGPT Business Hub** (launched by OpenAI in November 2026), similar to a Google Business Profile. It’s for anyone with a shop, clinic, office, or online business. The kit includes a test to see what ChatGPT says about you today, a form to fill out, tips on what went wrong for us, and a ready-to-use prompt for an AI agent to register your business in your browser. To do it yourself, you only need a ChatGPT account—even a free one—and it costs nothing. The agent-assisted option is optional and uses Claude Code (Anthropic), which requires a paid Claude plan and a computer with Chrome.

**You can reclaim your business on ChatGPT.** Today, ChatGPT speaks for your business based on what it finds online. When we searched for “INEMA,” it showed the Bahia environmental institute, with six locations. None of them were ours.

## 📖 User guide

Full guide (landing page + walkthrough with actual screens): **https://inematds.github.io/empresa-no-chatgpt/guia/en/**

## The 3 steps

1. **Find your business:** `chatgpt.com/business-hub` → search for the short and full names → choose the one at your address or select **Create**.
2. **Prove it’s yours:** physical location = code sent to the business phone; online store = a TXT record in your website’s DNS (business email and Shopify are also available).
3. **Tell them who you are:** category, description of up to 300 characters, shipping, returns → identity verification (document + selfie) → invite your team.

## Ask the agent to do it (the prompt)

Optional and paid separately: paste this into [Claude Code](https://claude.com/claude-code) with the [Claude in Chrome](https://claude.com/claude-in-chrome) extension (it uses your browser, where you’re already logged in; a paid Claude plan is required). Without an agent, follow the 3 steps above yourself for free. The full prompt and what the agent did in our case are in [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md) (in Portuguese).

```text
I want to register my business on ChatGPT (Business Hub, chatgpt.com/business-hub).
Read the kit at https://github.com/inematds/empresa-no-chatgpt (the tips and profile form).
Details: name <NAME>, <physical location or online store>, website <WEBSITE>, address <ADDRESS>, what we do <2 or 3 sentences>.
Use my browser, logged in to the BUSINESS account. Run the kit’s test first. Description: no more than 300 characters.
Stop and ask me before accepting terms, changing DNS, making a phone number/email public, and submitting.
I’ll handle the phone code, document, and selfie. At the end, provide screenshots and what’s left to do.
```

## The kit

| File | What it’s for |
|---|---|
| [`kit/1-teste-o-que-o-chatgpt-diz.md`](kit/1-teste-o-que-o-chatgpt-diz.md) (in Portuguese) | 8 questions to see what ChatGPT says about you + before-and-after form |
| [`kit/2-ficha-do-perfil.md`](kit/2-ficha-do-perfil.md) (in Portuguese) | All the fields required for registration + a description template of ≤ 300 characters |
| [`kit/3-dicas.md`](kit/3-dicas.md) (in Portuguese) | 19 tips from our actual registration (what went wrong and how to avoid it) |
| [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md) (in Portuguese) | How the agent registered the business on its own and the prompt to paste |
| [`kit/conferir_perfil.py`](kit/conferir_perfil.py) | Checks the form: description ≤ 300 characters and matching name/website/phone everywhere |
| [`automatico/txt_cloudflare.py`](automatico/txt_cloudflare.py) | Creates the TXT record in Cloudflare and waits for it to appear in public DNS |
| [`automatico/conferir_txt.sh`](automatico/conferir_txt.sh) | Checks whether the TXT record is visible (any DNS provider) |

## The proof (22/11/2026)

- **Before:** “INEMATDS” → no business; “INEMA” → Bahia environmental institute, 6 locations.
- **After:** INEMATDS LTDA created by the agent in ~10 minutes, online store, **inema.club verified** via DNS, category “AI company.” Status: draft until the owner’s identity is verified.
- Feature source: [OpenAI, “Businesses on ChatGPT”](https://openai.com/pt-BR/index/introducing-businesses-chatgpt/) (beta; rules may change).

---

## Technical setup

Prerequisites: Python 3.10+, `dig` (`dnsutils`/`bind-utils` package) to check DNS. To create the TXT record with the script: a domain on Cloudflare and a token with *Zone → DNS → Edit* permission. No external dependencies.

```bash
git clone https://github.com/inematds/empresa-no-chatgpt && cd empresa-no-chatgpt

# check the form before registration
python3 kit/conferir_perfil.py kit/exemplo-ficha.json          # copy and edit the example

# create the verification TXT record in Cloudflare (token in the environment only, never in code)
export CLOUDFLARE_API_TOKEN=...
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..." --dry-run          # shows what it will do
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..."                    # creates it and waits for it to appear

# check the TXT record with any provider
bash automatico/conferir_txt.sh seusite.com.br

# tests (10 cases: 300-character limit, website/phone mismatches, local type without address, TXT name, dry run)
python3 -m unittest discover -s tests
```

`txt_cloudflare.py` exits with 0 when the TXT record appears in public DNS, 1 on error, and 2 if it was created but hasn’t propagated yet.

## The process, from start to finish

| # | Step | Command / where | Who |
|---|---|---|---|
| 1 | “Before” test | 8 questions from `kit/1-teste-o-que-o-chatgpt-diz.md` (in Portuguese) in ChatGPT | 🧠 owner (or agent) |
| 2 | Profile form | `python3 kit/conferir_perfil.py minha-ficha.json` | 🧠 owner |
| 3 | Open the Hub and search | `chatgpt.com/business-hub` in a browser logged in to the business account | 🤖 agent (Claude in Chrome) |
| 4 | Create or choose the business | “Create ‘<name>’” → Start → physical location / online store | 🤖 agent |
| 5 | Prove it’s yours | DNS: `python3 automatico/txt_cloudflare.py …` → “Verify domain” · phone: code | ⚙️ script (with the owner’s approval) / 🧠 owner |
| 6 | Category, description, shipping, returns → Submit | form | 🤖 agent (shows it before submitting) |
| 7 | Identity (Persona: document + selfie) | “Verify” button on the overview | 🧠 owner |
| 8 | Invite the team | “Invite” in the Hub | 🧠 owner |
| 9 | “After” test (7 days) | the same 8 questions | 🧠 owner |

## Responsible use

Only claim a business you own or represent. Don’t publish a phone number or email address that can’t receive customer inquiries. The kit does not promise a particular position in ChatGPT’s answers.

Free projects and courses: https://inema.club · MIT License.